__author__ = "Pandaxyz-xd"
__copyright__ = "Copyright 2023, Coloripy"
__credits__ = ["Pandaxyz-xd", "Pandaxyz"]
__license__ = "GPL"
__version__ = "1.0.4"
__email__ = "contact@tourble.org"

import random
def color_word(text):
    colorWord_text = ""
    for line in text.splitlines():
        for i, word in enumerate(line.split(" ")):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colorWord_text += f"\033[38;2;{r};{g};{b}m{word}\033[0m "
        colorWord_text += "\n"
    return colorWord_text
def color_letter(text):
    colorLetter_text = ""
    for line in text.splitlines():
        for i, char in enumerate(line):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colorLetter_text += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        colorLetter_text += "\n"
    return colorLetter_text
def color_line(text):
    colorLine_text = ""
    for line in text.splitlines():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colorLine_text += f"\033[38;2;{r};{g};{b}m{line}\033[0m\n"
    return colorLine_text