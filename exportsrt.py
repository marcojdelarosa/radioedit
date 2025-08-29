import json
import os
from whisper_timestamped import make_subtitles

def exportSrt(input, output):
    out = open(output, 'w')
    # Load the JSON data from the file into a Python object (usually a dictionary or list)
    i = 1
    for segment in input["segments"]:
        for word in segment["words"]:
            print(
                f"{i}\n"
                f"{make_subtitles.format_timestamp(word['start'], always_include_hours=True, decimal_marker=',')} --> "
                f"{make_subtitles.format_timestamp(word['end'], always_include_hours=True, decimal_marker=',')}\n"
                f"{word['text'].strip().replace('-->', '->')}\n",
                file=out
            )
            i += 1