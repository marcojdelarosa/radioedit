import gradio as gr
from transcribe import transcribe
import os
from exportsrt import exportSrt
from censor import censor
from prepare import prepare
from pydub import AudioSegment
from titletext import print_title_text

def transcribe_and_export(input, output):
        transcription = transcribe(input, \
                                   os.path.basename("x_transcript.json"), \
                                   "small.en")
        exportSrt(transcription, output)
        return(0)

def full_edit(filename):
    prepare(filename)
    censor("transcript_main.srt" ,"raw_vocals_main.wav")
    censor("transcript_bg.srt", "raw_vocals_bg.wav")

    censored_main_vocals = AudioSegment.from_file("explicit_raw_vocals_main.wav", format="wav")
    censored_bg_vocals = AudioSegment.from_file("explicit_raw_vocals_bg.wav", format="wav")
    instrumental = AudioSegment.from_file("raw_inst.wav", format="wav")

    combined_vocals = censored_main_vocals.overlay(censored_bg_vocals)
    full_song = instrumental.overlay(combined_vocals)
    full_song.export("censored_song.wav", format="wav")
    print("Done!")
    return("censored_song.wav")

fulleditInterface = gr.Interface(fn=full_edit, inputs=gr.File(label="Audio"), outputs="audio")
prepareInterface = gr.Interface(fn=prepare, inputs=gr.File(label="Audio"), outputs="file")
censorInterface = gr.Interface(fn=censor, inputs=[ \
    gr.File(label="Transcript"), \
    gr.File(label="Vocals"),], \
    outputs="audio")
transcribeInterface = gr.Interface(fn = transcribe_and_export, inputs=["file","text"], outputs="text")

ui = gr.TabbedInterface([fulleditInterface, 
                         prepareInterface, 
                         censorInterface, 
                         transcribeInterface], 
                         ["Full Edit", 
                          "Prepare", 
                          "Censor", 
                          "Transcribe"], 
                         title="Radioedit", 
                         theme=gr.themes.Citrus())

print_title_text()

ui.launch(inbrowser=True)