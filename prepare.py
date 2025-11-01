import os
import separate
import transcribe
import exportsrt

FILES_TO_CLEAN = ["censored_raw_vocals_bg.wav", "censored_raw_vocals_main.wav",
                  "explicit_raw_vocals_bg.wav", "explicit_raw_vocals_main.wav",
                  "raw_inst.wav", "raw_vocals.wav", "raw_vocals_bg.wav", 
                  "raw_vocals_main.wav", "transcript_bg.srt", 
                  "transcript_main.srt", "bg_transcript.json", 
                  "main_transcript.json"]

def prepare(filename):
    for file in FILES_TO_CLEAN:
        if os.path.exists(file):
            os.remove(file)

    print("Separating...")
    separated_files = separate.separate(filename)
    print(separated_files)
    vocal_files = list(filter(lambda x: "Vocal" in x , separated_files))
     
    print("Transcribing main vocals...")
    main_transcription = transcribe.transcribe( \
         os.path.basename("raw_vocals_main.wav"), \
         os.path.basename("main_transcript.json"), "medium.en")
    
    print("Transcribing background vocals...")
    bg_transcription = transcribe.transcribe( \
         os.path.basename("raw_vocals_bg.wav"), \
         os.path.basename("bg_transcript.json"), "medium.en")
    
    print("Exporting Main SRT...")
    exportsrt.exportSrt(main_transcription, \
                        os.path.basename("transcript_main.srt"))
    print("Exporting BG SRT...")
    exportsrt.exportSrt(bg_transcription, os.path.basename("transcript_bg.srt"))
    print("Done!")
    return os.path.basename("transcript_main.srt")
