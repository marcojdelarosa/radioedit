import gradio as gr
from transcribe import transcribe
import os
from exportsrt import exportSrt
from censor import censor
from prepare import prepare
from titletext import print_title_text
from fulledit import full_edit

# small function for just transcribing and then exporting.
def transcribe_and_export(input, output):
        transcription = transcribe(input,
                                   os.path.basename("x_transcript.json"),
                                   "small.en")
        exportSrt(transcription, output)
        return(0)

# define each interface for gradio
fulleditInterface = gr.Interface(fn=full_edit, inputs=gr.File(label="Audio"), outputs="audio")
prepareInterface = gr.Interface(fn=prepare, inputs=gr.File(label="Audio"), outputs="file")
censorInterface = gr.Interface(fn=censor, inputs=[ \
    gr.File(label="Transcript"), \
    gr.File(label="Vocals"),], \
    outputs="audio")
transcribeInterface = gr.Interface(fn = transcribe_and_export, inputs=["file","text"], outputs="text")

# define the tabs for gradio
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

# print the title text. This is really unnecessary but I like doing it.
print_title_text()

# launch gradio, open in browser
ui.launch(inbrowser=True)