from time import sleep

import pandas as pd
from snownlp import SnowNLP

from ai import prompt_generator
from ai.cn_trans_to_en import cn_trans_to_en
from common_config import *
from utils import excel_util
from utils.chat_gpt_util import chat_model_prompt_1, split_sentences


# def cut_sentence(text):
#     s = SnowNLP(text)
#     return s.sentences

def cut_sentence(story):
    story = story.replace("\n", "").replace(" ", "")
    sentences = story.split("。")
    # 考虑有最大长度限制
    mini_sentence = ""
    res = ""
    for sentence in sentences:
        if len(mini_sentence + sentence) > 500:
            res += split_sentences(mini_sentence)+"\n"
            mini_sentence = sentence
        else:
            mini_sentence += sentence
    res += split_sentences(mini_sentence)
    res = res.split('\n')
    res = list(filter(lambda x: x.strip() != '', res))
    return res


def generate_subtask(task_path, out_root_dir):
    df = pd.read_excel(task_path)
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")

    for task in unfinished_dick:
        # 切分句子
        task['sentences'] = cut_sentence(task['content'])
        print(task)

        path = out_root_dir + task['type'] + "/" + task['en_name'] + "/task.xlsx"
        records = []

        i = 1
        # 关键词未生成->关键词已生成->AI绘图完成->文字图片生成视频完成
        for sentences in task['sentences']:
            try:
                prompt = chat_model_prompt_1(sentences) + TAG_PREFIX
                sleep(1)
                record = {'txt': sentences, 'index': i,
                          'prompt': prompt,
                          'negative': NEGATIVE,
                          'keywords_status': '关键词未生成',
                          'picture_status': '图片未生成',
                          'voice_status': '语音未生成',
                          'video_status': '视频未生成',
                          'picture_path': '',
                          'voice_path': '',
                          "video_path": ''}
                records.append(record)
                i += 1
            except Exception as e:
                print("当前句子", sentences, "--错误信息", e)
        excel_util.write_to_excel(records, path)
