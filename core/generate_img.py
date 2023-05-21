import pandas as pd

from ai.text_to_image import text_to_image
from concurrent.futures import ThreadPoolExecutor
from common_config import *


def process_subtask(subtask, task, subtask_df):
    out_path = task['subtask_picture_dir'] + "/" + str(subtask['index']) + ".png"
    text_to_image(prompt=subtask['prompt'], negative_prompt=subtask['negative'], out_path=out_path)
    # 更新状态
    subtask_df.iloc[subtask['index'] - 1, 5] = '图片已生成'
    subtask_df.iloc[subtask['index'] - 1, 8] = out_path
    subtask_df.to_excel(task['subtask_path'], index=False)


def generate_img(task_path, out_root_dir):
    df = pd.read_excel(task_path)
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")
    for task in unfinished_dick:
        task['subtask_path'] = out_root_dir + task['type'] + "/" + task['en_name'] + "/task.xlsx"
        task['subtask_picture_dir'] = out_root_dir + task['type'] + "/" + task['en_name'] + "/picture"

    for task in unfinished_dick:
        subtask_df = pd.read_excel(task['subtask_path'])
        subtask_dick = subtask_df[subtask_df['picture_status'] == '图片未生成'].to_dict("records")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for subtask in subtask_dick:
                executor.submit(process_subtask, subtask, task, subtask_df)
