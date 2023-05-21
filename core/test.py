# Import necessary libraries
import os
import sys

import cv2
import numpy as np
import moviepy.editor as mp

os.chdir(os.path.abspath("../"))
print(os.getcwd())
# Function to concatenate images with transition effect
def concatenate_images(images, transition_duration):
    if len(images) == 0:  # Check if the images list is empty
        return []
    concatenated_images = []
    for i in range(len(images) - 1):
        concatenated_images.append(images[i])
        for t in np.linspace(0, 1, transition_duration):
            alpha = t
            beta = 1 - t
            gamma = 0
            blended_image = cv2.addWeighted(images[i], alpha, images[i + 1], beta, gamma)
            concatenated_images.append(blended_image)
    concatenated_images.append(images[-1])
    return concatenated_images

# Function to concatenate audio files without abruptness
def concatenate_audio(audio_files):
    concatenated_audio = audio_files[0]
    for i in range(1, len(audio_files)):
        concatenated_audio = mp.concatenate_audioclips([concatenated_audio, audio_files[i]])
    return concatenated_audio

import pandas as pd

# Read the Excel file
excel_data = pd.read_excel(r"D:\novel-ai\data\output\爽文\story_1\task.xlsx")

# Extract the picture paths from the Excel file
picture_paths = excel_data["picture_path"].tolist()

audio_paths = excel_data["voice_path"].tolist()

# Load images from the picture paths
images = [cv2.imread(path) for path in picture_paths]
audio_files = [mp.AudioFileClip(path) for path in audio_paths]

# Check if any image is None and remove it from the list
images = [image for image in images if image is not None]

# Concatenate images and audio files
concatenated_images = concatenate_images(images, 30)
concatenated_audio = concatenate_audio(audio_files)

# Save the concatenated images as a video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (concatenated_images[0].shape[1], concatenated_images[0].shape[0]))
for image in concatenated_images:
    out.write(image)
out.release()

# Add the concatenated audio to the video
video = mp.VideoFileClip("output.avi")
video_with_audio = video.set_audio(concatenated_audio)
video_with_audio.write_videofile("final_output.mp4", codec="libx264", audio_codec="aac")
