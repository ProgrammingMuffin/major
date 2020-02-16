from gtts import gTTS as gtts
from playsound import playsound
import sys

def playText(text):
    speech = gtts(text)
    speech.save("buffer.mp3")
    playsound("buffer.mp3")
    return 1

playText(sys.argv[1])
print("Done")