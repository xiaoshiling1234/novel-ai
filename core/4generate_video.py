import pandas as pd

from ai.text_to_speech import text_to_wav
from utils.video_util import image_and_audio_to_video

if __name__ == '__main__':
    df = pd.read_excel('../data/input/tasklist/tasklist.xlsx')
    unfinished_tasks = df[df['status'] == '未完成']
    unfinished_dick = unfinished_tasks.to_dict("records")
    for task in unfinished_dick:
        task['subtask_path'] = "../data/output/" + task['type'] + "/" + task['en_name'] + "/task.xlsx"
        task['subtask_voice_dir'] = "../data/output/" + task['type'] + "/" + task['en_name'] + "/voice"
        task['subtask_fragment_dir'] = "../data/output/" + task['type'] + "/" + task['en_name'] + "/fragment"

    for task in unfinished_dick:
        subtask_df = pd.read_excel(task['subtask_path'])
        subtask_df = subtask_df[subtask_df['voice_status'] == '语音已生成']
        subtask_df = subtask_df[(subtask_df["voice_status"] == "语音已生成")
                                & (df["picture_status"] == "图片已生成")
                                & (df["video_status"] == "视频未生成")]

        subtask_dick = subtask_df.to_dict("records")

        for subtask in subtask_dick:
            image_path = subtask['picture_path']
            audio_path = subtask['voice_path']
            output_path = task['subtask_fragment_dir'] + "/" + str(subtask['index']) + ".mp4"
            image_and_audio_to_video(image_path, audio_path, output_path, 640, 480)
            # 更新状态
            subtask_df.iloc[subtask['index'] - 1, ] = '视频已生成'
            subtask_df.iloc[subtask['index'] - 1, 10] = task['subtask_fragment_dir'] + "/" + str(subtask['index']) + ".mp4"
            subtask_df.to_excel(task['subtask_path'], index=False)
