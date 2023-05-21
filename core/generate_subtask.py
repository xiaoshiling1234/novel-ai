from time import sleep

import pandas as pd
from snownlp import SnowNLP

from ai import prompt_generator
from ai.cn_trans_to_en import cn_trans_to_en
from common_config import *
from utils import excel_util


def cut_sentence(text):
    s = SnowNLP(text)
    return s.sentences


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
                en_sentence = cn_trans_to_en(sentences)
                sleep(TRANS_SLEEP_TIME)
                # prompt = ""
                #
                # retry_times = 0
                # while (prompt == "") and (retry_times < MAX_RETRY_TIMES):
                #     if retry_times > 0:
                #         print("提示词:", en_sentence, ",生成失败重试第", retry_times, "次")
                #     prompt = prompt_generator.generate(en_sentence)
                #     retry_times += 1
                record = {'txt': sentences, 'index': i,
                          'prompt': en_sentence+TAG_PREFIX,
                          'negative': NEGATIVE,
                          'keywords_status': '关键词未生成',
                          'picture_status': '图片未生成',
                          'voice_status': '语音未生成',
                          'video_status': '视频未生成',
                          'picture_path': '',
                          'voice_path': '',
                          "video_path": '',
                          "en_sentence": en_sentence}
                records.append(record)
                i += 1
            except Exception as e:
                print("当前句子", sentences, "--错误信息", e)
        excel_util.write_to_excel(records, path)
