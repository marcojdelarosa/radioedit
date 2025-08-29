# Radioedit 

Radioedit is a tool for automatically editing music to be played on the radio. Unfortunately, FCC Guidelines require that music must be played censored on radio, and a lot of music never had any censored edits. Using Radioedit, you can generate versions of songs that pass these guidelines using several machine learning implementations.
> This tool is a work in progress! The workflow is not fully complete, so usage will require backup from other tools such as [Audacity](https://www.audacityteam.org/) for the time being.

# Installation
**Python >= 3.13** is required to use this project. Right now, it would be recommended to use [uv](https://github.com/astral-sh/uv). Enter the directory and run `uv run main.py`, and it should work. *However, torch with GPU does not always work by default*, as the given installation of torch might not work with your CUDA. If it starts running with CPU, you should go to the [PyTorch website's Get Started page](https://pytorch.org/get-started/locally/), and get the install script corresponding to the CUDA installation specified with `nvidia-smi`.  Copy the install script, and if using uv, replace the beginning with `uv pip install`.