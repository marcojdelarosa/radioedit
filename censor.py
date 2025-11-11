import re
import srt
import os
import json
from pydub import AudioSegment

LANGUAGE = "en"

banned_words = []

def censor(transcriptFilename, audioFilename):

    # load banned words
    with open("bannedwords.json", "r") as banned_words_file:
        banned_words_data = json.load(banned_words_file)
        banned_words = set(banned_words_data[LANGUAGE])

    # open transcript file
    transcriptFile = open(transcriptFilename, "r")

    # open audio file
    vocal_audio = AudioSegment.from_file(os.path.basename(audioFilename), format="wav")
    
    # create an empty audio segment for exporting
    out_audio = AudioSegment.empty()

    last_segment_ms = 0

    # get the list of words from the transcript
    subtitles = srt.parse(transcriptFile)
    sub_list = list(subtitles)

    for subtitle in sub_list:

        # get start and end of each word
        subtitle_start_ms = subtitle.start.total_seconds() * 1000
        subtitle_end_ms = subtitle.end.total_seconds() * 1000
        # strip any whitepace from the text
        word = re.sub(r"[^\w\s]", "", subtitle.content.lower())

        # if there's space between the words, add silence to fill in the gap
        if last_segment_ms < subtitle.start.total_seconds() * 1000:
            vocal_segment = vocal_audio[last_segment_ms:subtitle_start_ms]
            out_audio += vocal_segment

        # if word is banned, replace with silence
        if word in banned_words:
            silence_duration = (subtitle_end_ms) - (subtitle_start_ms)
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment
        # otherwise, just add the word
        else:
            vocal_segment = vocal_audio[subtitle_start_ms:subtitle_end_ms]
            out_audio += vocal_segment
            print(subtitle.content, end = " ")

        # assign the end to last segment time
        last_segment_ms = subtitle_end_ms

    # export the clean audio
    out_audio.export("censored_" + os.path.basename(audioFilename), format="wav")
    print("\nclean audio exported!")

    # repeat to get the explicit only audio 
    out_audio = AudioSegment.empty()
    last_segment_ms = 0

    for subtitle in sub_list:
        subtitle_start_ms = subtitle.start.total_seconds() * 1000
        subtitle_end_ms = subtitle.end.total_seconds() * 1000
        word = re.sub(r"[^\w\s]", "", subtitle.content.lower())


        if last_segment_ms < subtitle.start.total_seconds() * 1000:
            silence_duration = subtitle_start_ms - last_segment_ms
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment

        if word in banned_words:
            vocal_segment = vocal_audio[subtitle_start_ms:subtitle_end_ms]
            out_audio += vocal_segment
            print(subtitle.content, end= " ")
        else:
            silence_duration = (subtitle_end_ms) - (subtitle_start_ms)
            silence_segment = AudioSegment.silent(duration=silence_duration)
            out_audio += silence_segment

        last_segment_ms = subtitle_end_ms

    print("\nexplicit audio exported!")
    out_audio.export("explicit_" + os.path.basename(audioFilename), format="wav")

    return "censored_" + os.path.basename(audioFilename)