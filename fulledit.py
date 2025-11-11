from transcribe import transcribe
from exportsrt import exportSrt
from censor import censor
from prepare import prepare
from titletext import print_title_text
from pydub import AudioSegment


def full_edit(filename):

    # transcribe and censor the file
    prepare(filename)
    censor("transcript_main.srt" ,"raw_vocals_main.wav")
    censor("transcript_bg.srt", "raw_vocals_bg.wav")

    # load vocals and inst
    censored_main_vocals = AudioSegment.from_file("explicit_raw_vocals_main.wav", format="wav")
    censored_bg_vocals = AudioSegment.from_file("explicit_raw_vocals_bg.wav", format="wav")
    instrumental = AudioSegment.from_file("raw_inst.wav", format="wav")

    # put all the audio files together, and export
    combined_vocals = censored_main_vocals.overlay(censored_bg_vocals)
    full_song = instrumental.overlay(combined_vocals)
    full_song.export("censored_song.wav", format="wav")

    # done!
    print("Done!")
    return("censored_song.wav")
