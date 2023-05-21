import pandas as pd

from utils.video_util import merge_mp4_files


def combine_video(task_path, out_root_dir):
    df = pd.read_excel(task_path)
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")
    for task in unfinished_dick:
        input_dir = out_root_dir + task['type'] + "/" + task['en_name'] + "/fragment"
        output_file = out_root_dir + task['type'] + "/" + task['en_name'] + "/result.mp4"
        merge_mp4_files(input_dir, output_file)

        df.iloc[task['index'] - 1, 7] = '已完成'
        df.iloc[task['index'] - 1, 8] = output_file
        df.to_excel(task_path, index=False)
