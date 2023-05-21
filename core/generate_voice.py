import pandas as pd

from ai.text_to_speech import text_to_wav


def generate_voice(task_path, out_root_dir):
    df = pd.read_excel(task_path)
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")
    for task in unfinished_dick:
        task['subtask_path'] = out_root_dir + task['type'] + "/" + task['en_name'] + "/task.xlsx"
        task['subtask_voice_dir'] = out_root_dir + task['type'] + "/" + task['en_name'] + "/voice"

    for task in unfinished_dick:
        subtask_df = pd.read_excel(task['subtask_path'])
        subtask_dick = subtask_df[subtask_df['voice_status'] == '语音未生成'].to_dict("records")

        for subtask in subtask_dick:
            out_path = task['subtask_voice_dir'] + "/" + str(subtask['index']) + ".wav"
            voice_json = text_to_wav(subtask['txt'], out_path)
            # 更新状态
            subtask_df.iloc[subtask['index'] - 1, 6] = '语音已生成'
            subtask_df.iloc[subtask['index'] - 1, 9] = out_path
            subtask_df.to_excel(task['subtask_path'], index=False)
