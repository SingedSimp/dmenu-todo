from subprocess import Popen, PIPE
from pathlib import Path

def display_list(menu, title, lines, font):
    proc = Popen(f'dmenu -l {lines} -i -p "{title}" -fn {font}', stdout=PIPE, stdin=PIPE, shell=True, text=True) 
    ans = proc.communicate("\n".join(menu))[0].strip()
    print(ans)

menu = ["1", "2", "3"]
title = ""
font = "JetBrainsMono"
lines = "10"
display_list(menu, title, lines, font)
