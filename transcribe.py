import whisper_timestamped as whisper
from whisper_timestamped import make_subtitles
import json

LANGUAGE = "en"

import os
def transcribe(input, output, model):
    # load audio file
    audio = whisper.load_audio(input)

    # load whisper model
    model = whisper.load_model(model)

    # transcribe the audio
    result = whisper.transcribe(model, audio, language=LANGUAGE)

    # export the result as json
    with open(output, 'w') as f:
        print(json.dumps(result, indent = 2, ensure_ascii = False), file=f)
        return(result)
    
    # if nothing was exported, return false
    return(False)
