import voice as voice
import time as time
import threading

#OCR
#Speech to text
#text to speech
#comand handling
#obstacle detection

class voiceThread(threading.Thread):

    def __init__(self, text, lock):
        threading.Thread.__init__(self)
        self.text = text
        self.lock = lock
    
    def run(self):
        while (1):
            x = voice.speechToText()
            if (x != None):
                self.text[0] = str(x)
                time.sleep(1)
                self.text[0] = "wait"
            else:
                self.text[0] = "wait"

class handlerThread(threading.Thread):

    def __init__(self, text, lock):
        threading.Thread.__init__(self)
        self.text = text
        self.lock = lock
    
    def run(self):
        while (1):
            if (text[0] != "wait"):
                print(self.text)
            if (text[0] == "exit"):
                break


text = ["wait"]
lock = threading.Lock()
t1 = voiceThread(text, lock)
t2 = handlerThread(text, lock)
t1.start()
t2.start()
t1.join()
t2.join()