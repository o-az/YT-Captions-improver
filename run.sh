#!/usr/bin/env bash

python3 YTaudio.py &
wait
python3 googleASR.py &
wait
python3 punctuation.py