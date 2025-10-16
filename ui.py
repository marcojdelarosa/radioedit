import gradio as gr
import transcribe
import separate
import exportsrt
import os
import censor

def prepare(filename):
    print("Separating...")
    separated_files = separate.separate(filename)
    print(separated_files)
    vocal_files = list(filter(lambda x: "Vocal" in x , separated_files))
    print("Transcribing...")
    transcription = transcribe.transcribe(os.path.basename("raw_vocals.wav"), os.path.basename("out.json"), "small.en")
    print("Exporting SRT...")
    exportsrt.exportSrt(transcription, os.path.basename("output.srt"))
    os.remove(os.path.basename("out.json"))
    return os.path.basename("output.srt")


prep = gr.Interface(fn=prepare, inputs=gr.File(label="Audio"), outputs="file")
censorInterface = gr.Interface(fn=censor.censor, inputs=[ \
    gr.File(label="Transcript"), \
    gr.File(label="Vocals"),], \
    outputs="audio")

ui = gr.TabbedInterface([prep, censorInterface], ["Prepare", "Censor"])

ui.launch()