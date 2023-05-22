
import cv2
import numpy as np
import os

def compose_video(image_path, audio_path, output_path, output_width, output_height):
    # Load image
    img = cv2.imread(image_path)
    img_height, img_width, _ = img.shape

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, 30, (output_width, output_height))

    # Create animation
    for i in range(30):
        # Create black background
        frame = np.zeros((output_height, output_width, 3), np.uint8)

        # Calculate position of image
        x = int((output_width - img_width) / 2)
        y = int((output_height - img_height) / 2)

        # Add image to frame
        if img_height > output_height or img_width > output_width:
            img = cv2.resize(img, (output_width, output_height))
        if img_height != output_height or img_width != output_width:
            os.remove(output_path)
            raise ValueError("Image dimensions do not match output dimensions")
        frame[y:y+img_height, x:x+img_width] = img

        # Add animation
        alpha = i / 30
        overlay = np.zeros((output_height, output_width, 3), np.uint8)
        overlay[:, :, 0] = 255 * alpha
        overlay[:, :, 1] = 255 * alpha
        overlay[:, :, 2] = 255 * alpha
        frame = cv2.addWeighted(frame, 1 - alpha, overlay, alpha, 0)

        # Write frame to video
        video_writer.write(frame)

    # Release video writer
    video_writer.release()

    # Add audio to video
    os.system(f'ffmpeg -i {output_path} -i {audio_path} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 -shortest {output_path}_audio.mp4')


try:
    compose_video(r"E:\novel-ai\core\1.png",r"E:\novel-ai\data\output\西游记\story_3\voice1\1.wav","out1.mp4",640, 480)
except ValueError as e:
    print(e)


