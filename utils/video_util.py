import subprocess
import random
import os
import json


# 定义一个函数，根据图片文件名，音频文件名，视频文件名和视频尺寸来生成随机动画效果的视频
def image_and_audio_to_video(image_file, audio_file, video_file, width, height):
    # 检查输入的图片和音频文件是否存在和合理
    if not os.path.exists(image_file) or os.path.getsize(image_file) == 0:
        raise FileNotFoundError(f"Image file {image_file} does not exist or is empty")
    if not os.path.exists(audio_file) or os.path.getsize(audio_file) == 0:
        raise FileNotFoundError(f"Audio file {audio_file} does not exist or is empty")

    # 使用ffprobe命令获取音频的时长，并赋值给duration
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", audio_file]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0 or b"error" in result.stderr.lower():
        raise RuntimeError(f"FFprobe command failed with exit code {result.returncode} and output {result.stderr}")
    duration = round(float(json.loads(result.stdout)["format"]["duration"]))  # 四舍五入为整数

    # 定义一些可能的动画效果的参数
    effects = ["fade", "zoompan", "rotate"]
    effect = random.choice(effects)  # 随机选择一个效果
    if effect == "fade":
        # 淡入淡出效果
        vf = f"fade=t=in:st=0:d=1,fade=t=out:st={duration - 1}:d=1"
    elif effect == "zoompan":
        # 缩放平移效果
        vf = f"zoompan=z='min(zoom+0.0015,1.5)':d={duration * 30 - 30}:x='if(gte(zoom,1.5),x,x+1/a)':y='if(gte(zoom,1.5),y,y+1)':s={width}x{height}"
    elif effect == "rotate":
        # 旋转效果
        vf = f"rotate=PI*t/8:ow={width}:oh={height},format=yuv420p"
    # 定义ffmpeg命令行参数列表
    cmd = ["ffmpeg", "-y", "-loop", "1", "-i", image_file, "-i", audio_file, "-c:v", "libx264", "-tune", "stillimage",
           "-c:a",
           "aac", "-pix_fmt", "yuv420p", "-vf", vf, "-shortest", video_file]

    # 调用subprocess模块执行命令，并获取返回值
    result = subprocess.run(cmd, capture_output=True)

    # 检查ffmpeg命令的执行结果是否正常
    if result.returncode != 0 or b"error" in result.stderr.lower():
        raise RuntimeError(f"FFmpeg command failed with exit code {result.returncode} and output {result.stderr}")

    # 检查输出的mp4文件是否存在和合理
    if not os.path.exists(video_file) or os.path.getsize(video_file) == 0:
        raise FileNotFoundError(f"Video file {video_file} does not exist or is empty")


# if __name__ == '__main__':
#     image_path = "../data/output/爽文/story_1/picture/1.png"
#     audio_path = "../data/output/爽文/story_1/voice/1.wav"
#     output_path = "../data/output/爽文/story_1/fragment/1.mp4"
#
#     # 测试一下函数
#     image_and_audio_to_video(image_path, audio_path, output_path, 640, 480)
