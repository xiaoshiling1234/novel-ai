import base64
import os
import wave

import common_config


def write_wav_from_json(Audio, path):
    decoded_wav = base64.b64decode(Audio)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with wave.open(path, 'wb') as wav_file:
        wav_file.setnchannels(common_config.WAV_CONFIG_CHANNELS)
        wav_file.setsampwidth(common_config.WAV_CONFIG_BITSPERSAMPLE // 8)
        wav_file.setframerate(common_config.WAV_CONFIG_SAMPLERATE)
        wav_file.writeframes(decoded_wav)
    trim_audio(path, 0.1, 0.1)


def trim_audio(file_path, start_trim, end_trim):
    with wave.open(file_path, 'rb') as wav_file:
        frames = wav_file.readframes(-1)
        rate = wav_file.getframerate()
        wav_file.close()
    sound_info = wave.struct.unpack("<h", frames[:2])[0]
    start_trim = int(start_trim * rate)
    end_trim = int(end_trim * rate)
    trimmed_sound = frames[start_trim: len(frames) - end_trim]
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setparams((1, 2, rate, len(trimmed_sound), "NONE", "not compressed"))
        wav_file.writeframes(trimmed_sound)
        wav_file.close()


def trim_folder(folder_path, start_trim, end_trim):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            file_path = os.path.join(folder_path, file_name)
            trim_audio(file_path, start_trim, end_trim)
