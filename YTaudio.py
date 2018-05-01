# !/usr/bin/env python
# -*- coding: utf-8 -*-

# CS:4980 Topics in Computer Science II: Research and Development of Accessible Computing Technologies
# Instructor: Kyle Rector
# Author: Omar Bin Salamah

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': '/Users/Omar/Desktop/Pythonstuff/Joe.'
}
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # start at <seconds>: end the link with ?t= <second> s (example: ?t=7s)
        # start at <minutes>: end the link with ?t= <minute> m <second> (example: ?t=1m3s)

        ydl.download(['https://www.youtube.com/watch?v=29oD-AeDwrk'])  # here you can put any link
except Exception:
    pass
# we're not going to worry about other implementations
# we're only interested in extracting the audio

