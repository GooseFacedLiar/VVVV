#!/usr/bin/env python3
import numpy as np
import sounddevice as sd
from colored import fg
from os import system

duration = 100 #in seconds
ses = 0
allvol = 0
threshold = 20

lowthresh = 15
mediumthresh = 45

def audio_callback(indata, frames, time, status):
    global ses
    global allvol
    ses += 1
    volume_norm = np.linalg.norm(indata) * 10
    allvol += volume_norm

    if ses >= threshold:
        system('clear')
        if allvol < lowthresh * threshold:
            print(fg('green') + """
            0
            O
            O""")
        elif allvol < mediumthresh * threshold:
            print(fg('yellow') + """
            O
            0
            O""")
        else:
            print(fg('red') + """
            O
            O
            0""")
        allvol = 0
        ses = 0



stream = sd.InputStream(callback=audio_callback)
with stream:
    sd.sleep(duration * 1000)