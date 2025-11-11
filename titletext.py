# The title text is a completely unnecessary feature, but I think it's cool.
# Every program used to have ascii art whenever you ran it. It's a lost art.
# Because of this I'm putting this big text in the beginning whenever you open the program.
# Anyway here's the code.
def rgb_bg(r, g, b):
    return(f"\033[48;2;{r};{g};{b}m")

def print_title_text():
    print("\033c"
        "\033[8;42;96t"  # change screen size
        "\033[5m"        # blinking  
        "\033[38;5;52m"  # dark red foreground
                      "\033[48;5;232m"     "   ▄████████                                            ▄████████                            \n"
                      "\033[48;5;233m"     "  ███    ███    ▄████████ ████████▄   ▄█   ▄██████▄    ███    ███ ████████▄   ▄█      ███    \n"
    "\033[38;5;52m",  rgb_bg(21, 26, 23),  "  ███    ███   ███    ███ ███   ▀███ ███  ███    ███   ███    ███ ███   ▀███ ███  ▀█████████▄\n"
    "\033[38;5;88m",  rgb_bg(31, 36, 28),  "  ███    ███   ███    ███ ███    ███ ███▌ ███    ███   ███    █▀  ███    ███ ███▌    ▀███▀▀██\n"
    "\033[38;5;88m",  rgb_bg(32, 40, 30),  " ▄███▄▄▄▄██▀   ███    ███ ███    ███ ███▌ ███    ███  ▄███▄▄▄     ███    ███ ███▌     ███   ▀\n"
    "\033[38;5;88m",  rgb_bg(32, 40, 30),  "▀▀███▀▀▀▀▀   ▀███████████ ███    ███ ███▌ ███    ███ ▀▀███▀▀▀     ███    ███ ███▌     ███    \n"
    "\033[38;5;124m", rgb_bg(31, 36, 28),  "▀███████████   ███    ███ ███    ███ ███  ███    ███   ███    █▄  ███    ███ ███      ███    \n"
    "\033[38;5;160m", rgb_bg(21, 26, 23),  "  ███    ███   ███    ███ ███   ▄███ ███  ███    ███   ███    ███ ███   ▄███ ███      ███    \n"
    "\033[38;5;196m"  "\033[48;5;233m"     "  ███    ███   ███    █▀  ████████▀  █▀    ▀██████▀    ███    ███ ████████▀  █▀      ▄████▀  \n" 
    "\033[38;5;196m"  "\033[48;5;232m"     "  ███    ███                                           ██████████                            \n"
    "\033[0m",          # reset
    sep="")

print_title_text()