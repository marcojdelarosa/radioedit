import re
import srt
import os
import json
from pydub import AudioSegment

LANGUAGE = "en"

banned_words = []

with open("bannedwords.json", "r") as banned_words_file:
    banned_words_data = json.load(banned_words_file)
    banned_words = set(banned_words_data[LANGUAGE])

def censor(transcriptFilename, audioFilename):
    transcriptFile = open(transcriptFilename, "r")

    vocal_audio = AudioSegment.from_file(os.path.basename(audioFilename), format="wav")
    out_audio = AudioSegment.empty()
    last_segment_ms = 0

    subtitles = srt.parse(transcriptFile)
    sub_list = list(subtitles)

    for subtitle in sub_list:
        subtitle_start_ms = subtitle.start.total_seconds() * 1000
        subtitle_end_ms = subtitle.end.total_seconds() * 1000
        word = re.sub(r"[^\w\s]", "", subtitle.content.lower())

        # print(subtitle_start_ms, "-", subtitle_end_ms)

        if last_segment_ms < subtitle.start.total_seconds() * 1000:
            vocal_segment = vocal_audio[last_segment_ms:subtitle_start_ms]
            out_audio += vocal_segment
            # print("patching:", last_segment_ms, "-", subtitle_start_ms)

        if word in banned_words:
            silence_duration = (subtitle_end_ms) - (subtitle_start_ms)
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment
        else:
            vocal_segment = vocal_audio[subtitle_start_ms:subtitle_end_ms]
            out_audio += vocal_segment
            print(subtitle.content)

        last_segment_ms = subtitle_end_ms

    print("done with censoring!")
    out_audio.export("censored_" + os.path.basename(audioFilename) + ".wav", format="wav")

    # repeat to get residual 
    out_audio = AudioSegment.empty()
    last_segment_ms = 0

    for subtitle in sub_list:
        subtitle_start_ms = subtitle.start.total_seconds() * 1000
        subtitle_end_ms = subtitle.end.total_seconds() * 1000
        word = re.sub(r"[^\w\s]", "", subtitle.content.lower())

        # print(subtitle_start_ms, "-", subtitle_end_ms)

        if last_segment_ms < subtitle.start.total_seconds() * 1000:
            silence_duration = subtitle_start_ms - last_segment_ms
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment
            # print("patching:", last_segment_ms, "-", subtitle_start_ms)

        if word in banned_words:
            vocal_segment = vocal_audio[subtitle_start_ms:subtitle_end_ms]
            out_audio += vocal_segment
            print("banned word: ", subtitle.content)
        else:
            silence_duration = (subtitle_end_ms) - (subtitle_start_ms)
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment

        last_segment_ms = subtitle_end_ms

    print("done with censoring!")
    out_audio.export("explicit_" + os.path.basename(audioFilename) + ".wav", format="wav")

    return os.path.basename("censored_vocals.wav")