import speech_recognition as sr
import pyttsx3
import datetime
import time
import re

budilnick = 0
chas = 0
minuta = 0
x = 0
list_commands = "Скажи время, Сколько время, сложить, умножить, разделить, вычесть, файл, добавить, будильник"

mic = sr.Microphone(device_index=1)
speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()
r.pause_threshold = 0.5

class gs:
    def __init__(self):
        pass

    def read_microphone():
        with mic as sourse:
            audio = r.listen(sourse)

        return audio

    def speak(text):
        print(text)
        speak_engine.say(text)
        speak_engine.runAndWait()
        speak_engine.stop()

    def scan(text, search_text):
        if re.search(search_text, text):
            return True

class Main:
    def __init__(self):
        pass

    def time(command):
        now = datetime.datetime.now()
        if command == "minutes":
            return str(now.minute)

        if command == "hours":
            return str(now.hour)