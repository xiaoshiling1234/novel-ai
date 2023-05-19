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