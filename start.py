import time

import common_config
from core import generate_subtask
from core import generate_voice
from core import generate_img
from core import generate_video
from core import combine_video

from common_config import *

if __name__ == '__main__':
    task_path = TASK_PATH
    out_root_dir = OUT_ROOT_DIR
    time_start = time.time()
    time_start_tmp = time_start
    print("-----------------------开始任务-----------------------", "当前时间:", time_start)
    print("-----------------------开始拆分子任务-----------------------")
    # generate_subtask.generate_subtask(task_path, out_root_dir)
    print("拆分子任务运行时长：", time.time() - time_start_tmp)
    time_start_tmp = time.time()
    print("-----------------------开始合成音频-----------------------")
    # generate_voice.generate_voice(task_path, out_root_dir)
    print("合成音频运行时长：", time.time() - time_start_tmp)
    time_start_tmp = time.time()
    print("-----------------------开始AI绘图-----------------------")
    # 可能会失败，直接跑多次，已生成的图片不会重跑
    # for i in range(common_config.MAX_RETRY_TIMES):
    #     generate_img.generate_img(task_path, out_root_dir)
    print("AI绘图运行时长：", time.time() - time_start_tmp)
    time_start_tmp = time.time()
    print("-----------------------开始合成视频片段-----------------------")
    generate_video.generate_video(task_path, out_root_dir)
    print("合成视频片段运行时长：", time.time() - time_start_tmp)
    time_start_tmp = time.time()
    print("-----------------------开始合并视频片段-----------------------")
    combine_video.combine_video(task_path, out_root_dir)
    print("合并视频片段运行时长：", time.time() - time_start_tmp)
    time_end = time.time()
    print("-----------------------任务完成-----------------------", "当前时间:", time_end)
    run_time = time_end - time_start
    print("运行时长：", run_time)
