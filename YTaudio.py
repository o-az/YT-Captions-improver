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
        'preferredcodec': 'wav', # the format of the audio is here
        'preferredquality': '192',
    }],
    # here add the path where you want the audio to go. No extension need be added for audio file
    'outtmpl': '/Users/Omar/captionsYT/PRES.'
}
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # start at <seconds>: end the link with ?t= <second> s (example: ?t=7s)
        # start at <minutes>: end the link with ?t= <minute> m <second> (example: ?t=1m3s)

        ydl.download(['<youtube-video-link>'])  # here you can put any link
except Exception:
    pass

print('\n\n YT audio is done! :) \n\n')
# we're not going to worry about other implementations
# we're only interested in extracting the audio
