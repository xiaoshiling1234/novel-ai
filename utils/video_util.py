# encoding:utf-8
import subprocess
import random
import os
import json


# 定义一个函数，根据图片文件名，音频文件名，视频文件名和视频尺寸来生成随机动画效果的视频
def image_and_audio_to_video(image_file, audio_file, video_file, width, height):
    directory = os.path.dirname(video_file)
    if not os.path.exists(directory):
        os.makedirs(directory)
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
    effects = ["fade", "rotate", "negate", "hflip"]
    # effects = ["fade"]
    effect = random.choice(effects)  # 随机选择一个效果
    if effect == "fade":
        # 淡入淡出效果
        vf = f"fade=t=in:st=0:d=1,fade=t=out:st={duration - 1}:d=1"
    elif effect == "rotate":
        # 旋转效果
        vf = f"rotate=PI*t/8:ow={width}:oh={height},format=yuv420p"
    elif effect == "negate":
        # 反色效果
        vf = "negate"
    elif effect == "hflip":
        # 水平翻转效果
        vf = "hflip"
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


# def merge_mp4_files(input_dir, output_file):
#     # Get all mp4 files in the input directory
#     input_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]
#
#     # Create a list of input file paths
#     input_paths = [os.path.join(input_dir, f) for f in input_files]
#
#     # Create the ffmpeg command to merge the files
#     command = ['ffmpeg', "-y", '-i', 'concat:' + '|'.join(input_paths), '-c', 'copy', output_file]
#
#     # Run the command
#     subprocess.call(command)


def merge_mp4_files(input_folder, output_file):
    # 检查输入文件夹是否存在
    if not os.path.isdir(input_folder):
        print("输入文件夹不存在")
        return
    # 获取输入文件夹下的所有mp4文件，并按字母顺序排序
    videos = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]
    videos.sort()
    # 如果没有找到mp4文件，退出函数
    if not videos:
        print("输入文件夹中没有mp4文件")
        return
    # 在输入文件夹下创建一个临时的文本文件，用于存储要合并的视频文件列表
    list_file = os.path.join(input_folder, "list.txt")
    with open(list_file, "w") as f:
        for video in videos:
            f.write(f"file {video}\n")
    # 构建ffmpeg命令
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", "-vsync", "2", output_file]
    # 执行ffmpeg命令，并捕获输出和错误信息
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.decode().strip())
        print("合并视频成功")
    except subprocess.CalledProcessError as e:
        print("合并视频失败")
        print(e.output.decode())
    # 删除临时的文本文件
    os.remove(list_file)

# if __name__ == '__main__':
#     merge_mp4_files(r"D:\novelai\data\output\爽文\story_1\fragment",
#                     r"D:\novelai\data\output\爽文\story_1\result.mp4")
# image_path = "../data/output/爽文/story_1/picture/2.png"
# audio_path = "../data/output/爽文/story_1/voice/2.wav"
# output_path = "../data/output/爽文/story_1/fragment/2.mp4"
#
#     # 测试一下函数
#     image_and_audio_to_video(image_path, audio_path, output_path, 640, 480)
