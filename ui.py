import gradio as gr
import transcribe
import separate
import exportsrt
import os

def prepare(filename):
    print("Separating...")
    separated_files = separate.separate(filename)
    print(separated_files)
    vocal_files = list(filter(lambda x: "Vocal" in x , separated_files))
    print("Transcribing...")
    transcription = transcribe.transcribe(os.path.basename(vocal_files[0]), os.path.basename("out.json"), "small.en")
    print("Exporting SRT...")
    exportsrt.exportSrt(transcription, os.path.basename("output.srt"))
    return os.path.basename("output.srt")


prep = gr.Interface(fn=prepare, inputs="file", outputs="file")

prep.launch()