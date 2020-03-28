from gtts import gTTS as gtts
from playsound import playsound
import speech_recognition as sr
import sys

def playText(text):
    speech = gtts(text)
    speech.save("buffer.mp3")
    playsound("buffer.mp3")
    return 1
    
def speechToText():
    r=sr.Recognizer()
    r.energy_threshold = 250
    r.non_speaking_duration = 0
    r.pause_threshold = 0.5 #by default 1
    with sr.Microphone() as source:
        print('say something')
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except Exception:
        print("an exception occured!")
        return None