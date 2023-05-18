import pandas as pd
import zhon.hanzi
import re
from utils import prompt_generator, excel_util, trans_util


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
        for sentences in task['sentences']:
            prompt, negative = prompt_generator.generate(trans_util.translate(sentences))

            record = {'txt': sentences, 'index': i,
                      'prompt': prompt,
                      'negative': negative}
            records.append(record)
            i += 1

        excel_util.write_to_excel(records, path)
        # todo://有时候会生成失败，到时候针对这类情况重新生成
