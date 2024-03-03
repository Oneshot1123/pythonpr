import pyttsx3
assist = pyttsx3.init()
text=input("say something : ")
assist.say(text)
assist.runAndWait()
# print("hello")
