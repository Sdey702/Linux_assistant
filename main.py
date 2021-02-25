import tkinter as tk
#from tkinter import *
import os
import threading
import multiprocessing
from help import baby1,run_baby1
root = tk.Tk()
photo = tk.PhotoImage(file = 'info.png')
root.iconphoto(False,photo)
program = tk.StringVar()
user = tk.StringVar()
lisen = tk.StringVar()

def speak(text):
    #engine.say(text)
    os.system('espeak "{}" '.format(text))

#os access
  
def seeting():
    os.system('gnome-control-center')
def texteditor():
    os.system('gedit')
def terminal():
    os.system('gnome-terminal')
def files():
    os.system('xdg-open /home/subhankar')
def cal():
    os.system('gnome-calculator')

# T2 = threading.Thread(target=seeting) 

try :
    import pywhatkit
except :
    program.set('no internet you have use just some feture')
    root.update()


import socket
def check_internet():
     IPaddress=socket. gethostbyname(socket. gethostname())
     if IPaddress=="127.0.0.2" or IPaddress=="127.0.0.1":
        print("No internet, your localhost is "+ IPaddress)
        return False
     else:
        print("Connected, with the IP address: "+ IPaddress )
        return True
  


def hello():
    if check_internet():
       lisen.set("lisitening...")
       root.update()
       b = baby1()
       run_baby1(b)
    else:
       speak('no internet please use anather button')



def no_internet(i):
  
    #speak('no internet ')
    from vosk import Model, KaldiRecognizer
    import threading
    import datetime
    import time
    from datetime import date
    today = date.today()
    t2 = threading.Thread(target=seeting) 
    t1 = threading.Thread(target=texteditor) 
    t3 = threading.Thread(target=terminal) 
    t4 = threading.Thread(target=files) 
    t5 = threading.Thread(target=cal)                
        

    def text(Text):
        print("hi :",Text[1])
        list = Text.split('"')
        ste = list[-2]
        print("list",list[-2])
        # program.set(ste)
        # root.update()
        return ste
        # x = threading.Thread(target=ext,args=(ste,))
        # x.start()
        #x.join()
        


    if not os.path.exists("model"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)

    import pyaudio

    model = Model("model")
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    print("hi baby",type(p))
    program.set("leassening...")
    root.update()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    while i==1:
        #x = threading.Thread(target=text(),args=(rec.Result()))
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            voice = text(rec.Result())
            if 'setting' in voice or 'seating' in voice :
                voice = voice.replace('open','')
                try:
                    speak('opening setting')
                    program.set("opening setting")
                    root.update()
                    t2.start()
                except:
                    if t2.is_alive() :
                        speak('already opening')
                    else :
                        t2.join()
                        del t2
                        t2 = threading.Thread(target=seeting) 
                        t2.start()
            elif 'text editor' in voice or 'notepad' in voice or 'edit' in voice :
                voice = voice.replace('open','')
                try:
                    speak('opening text editor')
                    program.set("opening text editor")
                    root.update()
                    t1.start()
                except:
                    if t1.is_alive() :
                        speak('already opening')
                    else :
                        t1.join()
                        del t1
                        t1 = threading.Thread(target=texteditor) 
                        t1.start()
            elif 'terminal' in voice or 'cmd' in voice or 'ter' in voice :
                voice = voice.replace('open','')
                try:
                    speak('opening terminal')
                    program.set("opening terminal")
                    root.update()
                    t3.start()
                except:
                    if t3.is_alive() :
                        speak('already opening')
                    else :
                        t3.join()
                        del t3
                        t3 = threading.Thread(target=terminal) 
                        t3.start()
            elif 'calculator' in voice or 'cal' in voice :
                voice = voice.replace('open','')
                try:
                    speak('opening calculator')
                    program.set("opening calculator")
                    root.update()
                    t5.start()
                except:
                    if t5.is_alive() :
                        speak('already opening')
                    else :
                        t5.join()
                        del t5
                        t5 = threading.Thread(target=cal) 
                        t5.start()
            elif 'files' in voice or 'file' in voice :
                voice = voice.replace('open','')
                try:
                    speak('opening file system')
                    program.set("opening files")
                    root.update()
                    t4.start()
                except:
                    if t4.is_alive() :
                        speak('already opening')
                    else :
                        t4.join()
                        del t4
                        t4 = threading.Thread(target=files) 
                        t4.start()
            elif 'exit' in voice or 'tata' in voice or 'goodbye' in voice or 'quit' in voice or 'bye bye' in voice :
                speak("good bye dear have a great day")
                exit(1)
            elif 'time' in voice:
                time = datetime.datetime.now().strftime('%I:%M %p')
                program.set('Current time is =' + time)
                root.update()
                speak('Current time is ' + time)
            elif 'date' in voice or 'day' in voice or 'debt' in voice:
                d2 = today.strftime("%B %d, %Y")
                program.set(d2)
                root.update()
                speak(d2)
                print(d2)
            
            else:
                speak('tell what can i do without internet')
            i=i+1
            print("Rosult",rec.Result())
            #x.start()
        else:
            rec.PartialResult() 

def hi():
  if check_internet() == False:
     no_internet(1)
  else:
    speak('internet present')
     


# main

if __name__ == "__main__":
    
    root.title('Linux Assistant')
    root.geometry('500x300')
    root.configure(bg='white')
    im = tk.PhotoImage(file='images/pause.png')
    im = im.subsample(2,2)
    # label0 = Label(root ,text = 'liseaning....',bg='white')
    # label0.pack()
    label1 = tk.Label(root ,textvariable = user,bg='white')
    label1.pack()
    btn1 = tk.Button(root,width=50,height=60,activebackground='white',bg='green',borderwidth=4,image=im,command = hello)
    btn1.pack()
    label4 = tk.Label(root,text='use when internet present')
    label4.pack()
    label = tk.Label(root ,textvariable = program,bg='white')
    label.pack()
    btn2 = tk.Button(root,width=50,height=60,activebackground='red',bg='yellow',borderwidth=4,image=im,command=hi)
    btn2.pack()
    lable3 = tk.Label(root,text='use when internet not present')
    lable3.pack()
    #p1 = multiprocessing.Process(target=main)
    #ain()
    #label = Label(root ,textvariable = program,bg='white')
    #label.pack()

    root.mainloop()

