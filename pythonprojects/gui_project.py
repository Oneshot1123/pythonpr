import pyaudio
import speech_recognition as sr
rec = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything : ")
    hear = rec.listen(source)
try:
    gg = recognize_google(hear)
    print("You Said : ")
except:
    print("Sorry Could Not Recognize Your Voice : ")
