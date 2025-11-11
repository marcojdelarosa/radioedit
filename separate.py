from audio_separator.separator import Separator
import os

def separate(input):
    # initialize the Separator class
    separator = Separator()

    # load the default model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
    separator.load_model()

    # separate the vocals and instrumental
    output_files = separator.separate(input)

    # rename the outputs
    os.rename(output_files[0], "raw_inst.wav")
    os.rename(output_files[1], "raw_vocals.wav")

    # load karaoke model
    separator.load_model("mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt")

    # separate the main vocals and background vocals
    output_files = separator.separate(os.path.basename("raw_vocals.wav"))

    # rename the outputs
    os.rename(output_files[0], "raw_vocals_bg.wav")
    os.rename(output_files[1], "raw_vocals_main.wav")

    # print message
    print(f"Separation complete! Output file(s): {' '.join(output_files)}")
    return(output_files)