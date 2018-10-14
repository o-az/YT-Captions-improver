# CS4980 Topics in Computer Science II: Research and Development of Accessible Computing Technologies
# Final project - Improving YouTube auto-generated captions

YouTube is an amazing place for people to learn new things and be entertained. There is an endless supply of content, which is great, but with this amount of content brings problems. Specifically, YouTube has some problems with its closed captioning. Content creators are given the option to either type their own captions, or have YouTube auto-generate them. Unsurprisingly, most content creators choose the latter. YouTube’s auto-captioning tool works really well most of the time, but has major issues identifying pause breaks, so there are never any periods in the text. Basically, it posts the whole transcript as one really long sentence that goes on for the entire time someone is talking. Additionally, YouTube will sometimes identify the wrong word which was spoken. For example, the content creator could say “of his” during the video, but YouTube might think they said “office”. These mistakes can be very confusing in certain situations. Having improper punctuation and phrases makes following along with YouTube videos much more challenging than it should be for people who use the caption feature. Overall, our motivation for this project is to give people who use YouTube captions an easier to follow, less annoying way to take in YouTube videos because we believe everyone should have equal access to the benefits that can come from these videos.

Steps:
  1. clone this
  2. On YTaudio.py go to line 19 and specify where the file needs to be saved and the name of the file
  2. On YTaudio.py go to line 26 and add the link of the YouTube video you wish to download audabily
  3. On GoogleASR.py go to line 14 and specify the name of the file with the extension (.wav for example)
  4. On GoogleASR.py go to line 28 and specify the name of the file where the Speech2Text would go
  5. On puncuation.py go to line 109 and specify where the .txt file from speech2text is stored
  6. On puncuation.py go to line 145 and specify where the result should be saved
  7. Run the bash file on your terminal like this ~$ sh run.sh
