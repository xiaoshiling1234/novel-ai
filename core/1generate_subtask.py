import pandas as pd
import zhon.hanzi
import re
from utils import excel_util
from ai import trans_language, prompt_generator


def cut_sentence(content):
    rst = re.findall(zhon.hanzi.sentence, content)
    return rst


if __name__ == '__main__':
    df = pd.read_excel('../data/input/tasklist/tasklist.xlsx')
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")

    for task in unfinished_dick:
        # 切分句子
        task['sentences'] = cut_sentence(task['content'])
        print(task)

        path = "../data/output/" + task['type'] + "/" + task['en_name'] + "/task.xlsx"
        records = []

        i = 1
        # 关键词未生成->关键词已生成->AI绘图完成->文字图片生成视频完成
        for sentences in task['sentences']:
            prompt, negative = prompt_generator.generate(trans_language.translate(sentences))
            if prompt == '':
                record = {'txt': sentences, 'index': i,
                          'prompt': prompt,
                          'negative': negative,
                          'keywords_status': '关键词未生成',
                          'picture_status': '图片未生成',
                          'voice_status': '语音未生成',
                          'video_status': '视频未生成',
                          'picture_path': '',
                          'voice_path': '',
                          "video_path": ''}
            else:
                record = {'txt': sentences, 'index': i,
                          'prompt': prompt,
                          'negative': negative,
                          'keywords_status': '关键词已生成',
                          'picture_status': '图片未生成',
                          'voice_status': '语音未生成',
                          'video_status': '视频未生成',
                          'picture_path': '',
                          'voice_path': '',
                          "video_path": ''}
            records.append(record)
            i += 1

        excel_util.write_to_excel(records, path)
