import whisper_timestamped as whisper
import os

file = open(os.path.basename("testaudio.mp3"), "r")

audio = whisper.load_audio("C:\\Users\\marco\\Projects\\radioedit\\testaudio.mp3")

model = whisper.load_model("small", device="cpu")

result = whisper.transcribe(model, audio, language="en")

import json
print(json.dumps(result, indent = 2, ensure_ascii = False))