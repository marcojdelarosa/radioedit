```
   ▄████████                                            ▄████████
  ███    ███    ▄████████ ████████▄   ▄█   ▄██████▄    ███    ███ ████████▄   ▄█      ███
  ███    ███   ███    ███ ███   ▀███ ███  ███    ███   ███    ███ ███   ▀███ ███  ▀█████████▄
  ███    ███   ███    ███ ███    ███ ███▌ ███    ███   ███    █▀  ███    ███ ███▌    ▀███▀▀██
 ▄███▄▄▄▄██▀   ███    ███ ███    ███ ███▌ ███    ███  ▄███▄▄▄     ███    ███ ███▌     ███   ▀
▀▀███▀▀▀▀▀   ▀███████████ ███    ███ ███▌ ███    ███ ▀▀███▀▀▀     ███    ███ ███▌     ███
▀███████████   ███    ███ ███    ███ ███  ███    ███   ███    █▄  ███    ███ ███      ███
  ███    ███   ███    ███ ███   ▄███ ███  ███    ███   ███    ███ ███   ▄███ ███      ███
  ███    ███   ███    █▀  ████████▀  █▀    ▀██████▀    ███    ███ ████████▀  █▀      ▄████▀
  ███    ███                                           ██████████ 
```

Radioedit is a tool for automatically editing music to be played on the radio. FCC Guidelines require all music played on radio to be censored. If you don't have stems for the song, and there is no pre-existing censored version, you can use Radioedit to generate versions of songs that pass these guidelines.  

> This tool is a work in progress! The workflow is not fully complete, so usage will require backup from other tools such as [Audacity](https://www.audacityteam.org/) for the time being.

# Installation
**Python >= 3.13** is required to use this project. Right now, it would be recommended to use [uv](https://github.com/astral-sh/uv). Enter the directory and run `uv run ui.py`, and it should work.  
*However, torch with GPU does not always work*, as the given installation of torch might not work with your CUDA. If the script runs with CPU, you should visit to the [PyTorch website's Get Started page](https://pytorch.org/get-started/locally/) and find the install script corresponding to your CUDA installation, which you can find  `nvidia-smi`.  Copy the install script, and if using uv, replace the start of the line with `uv pip install`.

# Usage
The workflow is pretty simple right now. You'll want to work in the **Full Edit** tab. Drag an audio file into the Audio input, and click submit. Check the command line, and it should show what's going on. Once it's fully finished, you'll end up with the instrumental, and clean and explicit versions of the main and background vocals. In addition, you'll have a fully clean version of the audio you put in. **Make sure to listen back to it,** because missed words are very common. If there is any, put the audio files into audacity. You'll want to select any unaccounted profanity and hit **(CTRL/CMD) + L** to silence it. Afterwards, output the file and you'll end up with a clean version of the song.
