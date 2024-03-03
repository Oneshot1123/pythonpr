from tkinter import *
import wikipedia as wk 
import pyttsx3

window = Tk()
window.title(" Personal Search Engine")
window.geometry("500x500+600+200")
window.config(bg="lightpink")

f1=Frame(window)
result=Frame(window)    #used for creating frames 


Label(f1,text="SEARCH ENGINE.org",font=('Calibri',15,'bold'),bg ='lightgreen',fg='lightpink',width=600,pady=11).pack(side=TOP)

Label(f1,text="Search Here",font=('Calibri',13,'bold'),bg ='black',fg='lightpink',width=13,pady=5).pack(side=LEFT)

Label(result,text="Search Result",font=('Calibri',13,'bold'),bg ='black',fg='lightpink',width=500).pack(side=TOP)

try_Box=Entry(f1,font=('Arial',13,'bold'),bg='black',fg='lightpink',width=10)
try_Box.pack(side=LEFT,fill=BOTH,expand=5)

txt =Text(result,font=('Calibri',15,'bold'),bg='black',fg='white',padx=12,pady=12) # text creation 

def text_search():
    global querry 
    querry = try_Box.get()

    try:
        sbar = wk.summary(querry)
        txt.insert("1.0",sbar)

    except:
        txt.insert("1.0","Doesnt Exist Please Try Again")


def speak_search():
    global querry 
    querry = try_Box.get()

    try:
        sbar = wk.summary(querry)
        speech=pyttsx3.init()
        speech.say(sbar)
        speech.runAndWait()

    except:
        speech=pyttsx3.init()
        speech.say("Doesnt Exist Please Try Again")
        speech.runAndWait()

button1 = Button(f1,text="Text",command=text_search,font=('Calibri',13,'bold'),bg='gray',fg='white',width=6)# button creation

button2 = Button(f1,text="speak",command=speak_search,font=('Calibri',13,'bold'),bg='gray',fg='white',width=6)# button creation

button1.pack(side=RIGHT)
button2.pack(side=RIGHT)
txt.pack(side=TOP)
f1.pack(side=TOP)
result.pack(side=TOP,padx=55,pady=20)

window.mainloop()    # for parent window 
