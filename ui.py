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
    main_transcription = transcribe.transcribe(os.path.basename("raw_vocals_main.wav"), os.path.basename("main_transcript.json"), "medium.en")
    print("Exporting Main SRT...")
    bg_transcription = transcribe.transcribe(os.path.basename("raw_vocals_bg.wav"), os.path.basename("bg_transcript.json"), "medium.en")
    print("Exporting BG SRT...")
    exportsrt.exportSrt(main_transcription, os.path.basename("transcript_main.srt"))
    exportsrt.exportSrt(bg_transcription, os.path.basename("transcript_bg.srt"))
    # os.remove(os.path.basename("main_transcript.json"))
    # os.remove(os.path.basename("bg_transcript.json"))
    print("Done!")
    return os.path.basename("transcript_main.srt")

def transcribe_and_export(input, output):
        transcription = transcribe.transcribe(input, os.path.basename("x_transcript.json"), "small.en")
        exportsrt.exportSrt(transcription, output)
        return(0)

prep = gr.Interface(fn=prepare, inputs=gr.File(label="Audio"), outputs="file")
censorInterface = gr.Interface(fn=censor.censor, inputs=[ \
    gr.File(label="Transcript"), \
    gr.File(label="Vocals"),], \
    outputs="audio")
transcribeInterface = gr.Interface(fn = transcribe_and_export, inputs=["file","text"], outputs="text")

ui = gr.TabbedInterface([prep, censorInterface, transcribeInterface], ["Prepare", "Censor", "Transcribe"])

ui.launch()