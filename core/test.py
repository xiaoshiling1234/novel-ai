 
import base64
import io
import wave

# Read the base64 encoded wav file
with open(r"E:\novel-ai\data\input\test.json", "r") as f:
    encoded_wav = f.read()

# Decode the base64 string
decoded_wav = base64.b64decode(encoded_wav)

# Write the decoded wav file to disk
with wave.open("decoded_wav.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    f.writeframes(decoded_wav)


