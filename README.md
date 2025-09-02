# Radioedit 

Radioedit is a tool for automatically editing music to be played on the radio. FCC Guidelines require all music played on radio to be censored. Using Radioedit, you can generate versions of songs that pass these guidelines using several machine learning implementations.  

> This tool is a work in progress! The workflow is not fully complete, so usage will require backup from other tools such as [Audacity](https://www.audacityteam.org/) for the time being.

# Installation
**Python >= 3.13** is required to use this project. Right now, it would be recommended to use [uv](https://github.com/astral-sh/uv). Enter the directory and run `uv run main.py`, and it should work.  *However, torch with GPU does not always work*, as the given installation of torch might not work with your CUDA. If the script runs with CPU, you should visit to the [PyTorch website's Get Started page](https://pytorch.org/get-started/locally/) and find the install script corresponding to your CUDA installation, which you can find  `nvidia-smi`.  Copy the install script, and if using uv, replace the start with `uv pip install`.