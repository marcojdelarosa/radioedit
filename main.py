import transcribe
import separate
import exportsrt
import os
def main():
    print("Transcribe file: ", end='')
    filename = input()
    print("Separating...")
    separated_files = separate.separate(os.path.basename(filename))
    print(separated_files)
    vocal_files = list(filter(lambda x: "Vocal" in x , separated_files))
    print("Transcribing...")
    transcription = transcribe.transcribe(os.path.basename(vocal_files[0]), os.path.basename("out.json"), "small.en")
    print("Exporting SRT...")
    exportsrt.exportSrt(transcription, os.path.basename("output.srt"))

if __name__ == "__main__":
    main()
