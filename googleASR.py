# !/usr/bin/env python
# -*- coding: utf-8 -*-

# CS:4980 Topics in Computer Science II: Research and Development of Accessible Computing Technologies
# Instructor: Kyle Rector
# Author: Omar Bin Salamah

# https://www.youtube.com/watch?v=XKu_SEDAykw&feature=youtu.be&t=10m54s

import speech_recognition as sr

# get path to "some_audio_file.wav" in the same folder as this
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "PRES.wav") # the name of the YTaudio downloaded

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    result = r.recognize_google(audio)
    #print("\n\nresult: " + result)
    with open('/Users/Omar/captionsYT/result.txt', 'w') as f:
    #with open('result.txt', 'w') as f:
        f.write(result.strip(''))
        f.close()

except Exception:
    pass

print('\nGoogle ASR is done :)   \n\n')

