#!/usr/bin/env bash

# here I should also automate YTaudio.py
# python3 YTaudio.py &
# wait
python3 googleASR.py &
wait
python3 punctuation.py