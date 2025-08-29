import whisper_timestamped as whisper
from whisper_timestamped import make_subtitles

import os
def transcribe(input, output, model):
    audio = whisper.load_audio(input)

    model = whisper.load_model(model)

    result = whisper.transcribe(model, audio, language="en")

    import json
    with open(output, 'w') as f:
        print(json.dumps(result, indent = 2, ensure_ascii = False), file=f)
        return(result)
    return(False)
