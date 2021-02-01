'''pip install gTTTS
   pip install playsound''' 
import tkinter as tk
from gtts import gTTS
from playsound import playsound

win=tk.Tk()
win.title("TEXT TO SPEECH")
win.geometry("200x70")

def text_to_speech():
	text=entry.get()
	speech=gTTS(text=text,lang="en")
	speech.save(r'D:\Demo\Python\Project\speech.mp3')
	playsound(r'D:\Demo\Python\Project\speech.mp3')
label=tk.Label(win,text="Enter text: ")
label.grid(row=0,column=0)
entry=tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="Go" ,command=text_to_speech)
button.grid(row=1,column=1)
win.mainloop()