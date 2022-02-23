from subprocess import Popen, PIPE
from pathlib import Path
from os import system
from sys import exit, argv
def display_list(menu, title, lines, font):
    proc = Popen(f'dmenu -l {lines} -i -p "{title}" -fn {font}', stdout=PIPE, stdin=PIPE, shell=True, text=True)
    index = 0
    ans = proc.communicate("\n".join(menu))[0].strip()
    if ans in entries: # Find index and align with the onclick
        for i in range(len(entries)):
            entry = entries[i]
            if ans == entry:
                break
            index+=1
    return onclick[index]

entries = []
onclick = []

with open(str(argv[1::])[2:-2:]) as f:
    lines = f.readlines()
    folder = False
    for l in lines:
        if l.startswith("-"): # If entry
            entries.append(l[2:-1:]) # Remove first & last 2 chars 
        elif l.startswith("+"): # If action
            onclick.append(l[2:-1:])
        elif l.startswith("="):
            entries.append("Folder: "+l[2:-1:])
            onclick.append("python display.py "+l[2:-1:])



menu = entries
title = ""
font = "JetBrainsMono"
lines = "10"
system(display_list(menu, title, lines, font))
exit()
