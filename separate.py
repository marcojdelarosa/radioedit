from audio_separator.separator import Separator
import os

def separate(input):
    # Initialize the Separator class (with optional configuration properties, below)
    separator = Separator()

    # Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
    separator.load_model()

    # Perform the separation on specific audio files without reloading the model
    output_files = separator.separate(input)
    if os.path.exists(os.path.basename("raw_inst.wav")):
        os.remove("raw_inst.wav")
    if os.path.exists(os.path.basename("raw_vocals.wav")):
        os.remove("raw_vocals.wav")
    os.rename(output_files[0], "raw_inst.wav")
    os.rename(output_files[1], "raw_vocals.wav")

    # load karaoke model
    separator.load_model("mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt")

    output_files = separator.separate(os.path.basename("raw_vocals.wav"))

    
    if os.path.exists(os.path.basename("raw_vocals_bg.wav")):
        os.remove("raw_vocals_bg.wav")
    if os.path.exists(os.path.basename("raw_vocals_main.wav")):
        os.remove("raw_vocals_main.wav")
    
    os.rename(output_files[0], "raw_vocals_bg.wav")
    os.rename(output_files[1], "raw_vocals_main.wav")

    print(f"Separation complete! Output file(s): {' '.join(output_files)}")
    return(output_files)