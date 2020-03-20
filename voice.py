from gtts import gTTS as gtts
from playsound import playsound
import sys

def playText(text):
    speech = gtts(text)
    speech.save("buffer.mp3")
    playsound("buffer.mp3")
    return 1
    
def speechToText():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('say something')
        audio=r.listen(source)
    try:
        print('you said:\n'+r.recognize_google(audio))
    except Exception:
        print("an exception occured!: " + Exception)

#test
speechToText()
