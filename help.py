#from tkinter import *
from speak import talk
import os
import threading
import multiprocessing
import requests 
import bs4 
# root = Tk()
# user = StringVar()


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

import speech_recognition as sr
import threading
import os
import time
import wikipedia
from gtts import gTTS
import webbrowser
import datetime
import requests
import pyttsx3
from decouple import config
from datetime import date
today = date.today()


try :
    import pywhatkit
except :
    pass
    




listener = sr.Recognizer()
    # engine = pyttsx3.init()
    # engine.setProperty('rate', 185)
    # voices = engine.getProperty('voices')   
    # engine.setProperty('voice', voices[1].id) 
    #os.system('espeak "{}" '.format(text))

    # def speak(text):
    #     #engine.say(text)
    #     os.system('espeak "{}" '.format(text))
    #     # tts = gTTS(text = text,lang ='en')
    #     # tts.save('hello.mp3')
    #     # os.system("mpg321 hello.mp3")
import socket
def check_internet():
     IPaddress=socket. gethostbyname(socket. gethostname())
     if IPaddress=="127.0.0.2" or IPaddress=="127.0.0.1":
        print("No internet, your localhost is "+ IPaddress)
        return False
     else:
        print("Connected, with the IP address: "+ IPaddress )
        return True
  


def baby1():
    statement = ''
    try:
        # with sr.Microphone() as source:
        #     print('listening...')
        #     voice = listener.listen(source,2)
        #     print(voice)
        #     command = listener.recognize_google(voice)  
        #     #command = listener.recognize_sphinx(voice,language="en-US")
        #     command = command.lower()
        #     print(command)
        #     command = command.replace('listening','')
            statement = talk()
            # if 'i am ' in command :
            #     command = command.replace('i am listening','')
            # # if oshan in command than execute
            # if 'covid' in command or 'covit' in command:
            #     command = command.replace('covid','')
            #     command = command.replace('listening','')
            #     statement = command
            #     print(command)
            # else :
            #     #pass
            #     print(command)
            #     command = command.replace('listening','')
            #     statement = command
    except:
        #speak("I can't understand ")
        pass


    return statement

def weather(city):
    user_api = config('KEY')
    location = city

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    if api_data['cod'] == '404':
        speak('check your city name {}'.format(city))
        check_weather()
    else :
        #create variables to store and display data
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        #date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


        # print ("-------------------------------------------------------------")
        # print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        # print ("-------------------------------------------------------------")

        a = "Current temperature is {:.2f} degree".format(temp_city)
        b = "Current weather description is {}".format(weather_desc)
        c = "Current atmosphere Humidity is {} %".format(hmdt)
        d = "Current wind speed is {} kilometar per hour".format(wind_spd)

        weather = a+b+c+d
        print(weather)
        return weather
    
def check_weather() :
    speak('please tell me the city name')
    city = baby1()
    speak(weather(city))
    return
    
# write logic use elif condition and give the solution
def run_baby1(command):
    

    if 'play' in command or 'playing' in command :
        if check_internet():
            import pywhatkit
        song = command.replace('sing','')
        if 'music' in command :
            song = command.replace('play','')
            #song = command.replace('playing','')
            speak('playing'+ song + 'from youtube')
            pywhatkit.playonyt(song)
        else :
            song = command.replace('play','')
            speak('playing'+ song + 'from youtube')
            pywhatkit.playonyt(song)
    elif 'i love you' in command :
        speak("i love you two sir I'm hear all time For you")
    elif 'tell me about' in command :
        speak("i am your friend ocean helping you is my game aske me")
    elif 'prime ministers' in command or 'president' in command or 'ceo' in command or 'chairman' in command or 'pri' in command :
        speak('Here what we found in web') 
        webbrowser.open('https://google.com/search?q='+command)
    elif 'who ' in command or 'wikipedia' in command:
        person = command.replace('who is the','')
        if 'who is' in person :
            person = person.replace('who is','')
            print(person)
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            speak('according to wikipedia'+info)
        except:
            speak('what we found in web')
            webbrowser.open('https://google.com/search?q='+command)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        speak('according to wikipedia'+info)
    elif 'open' in command or 'opening' in command :
        voice = command.replace('open','')
        if 'opening' in command :
                voice = command.replace('opening','')
        speak('opening'+ voice)
        if 'facebook' in voice :
            voice = 'https://www.facebook.com/'
            webbrowser.open(voice)
        elif 'ganna' in voice :
            voice = 'https://gaana.com/'
            webbrowser.open(voice)
        elif 'instagram' in voice :
            voice = 'https://www.instagram.com/'
            webbrowser.open(voice)
        elif 'twiter' in voice :
            voice = 'https://twitter.com/'
            webbrowser.open(voice)
            # for any oppening site folow this step...
        elif 'linkedin' in voice :
            voice = 'https://www.linkedin.com/'
            webbrowser.open(voice)
        elif 'youtube' in voice :
            voice = 'https://www.youtube.com/'
            webbrowser.open(voice)
        elif 'setting' in voice or 'seating' in voice :
            t2 = threading.Thread(target=seeting) 
            t2.start()
            #os.system('gnome-control-center')
        elif 'visual studio' in voice or 'code editor' in voice :
            os.system('code')
        elif 'cal' in voice or 'calculator' in voice :
            t5 = threading.Thread(target=cal) 
            t5.start() 
            # os.system('gnome-calculator')
        elif 'terminal' in voice or 'cmd' in voice or 'cmdportal' in voice :
            t3 = threading.Thread(target=terminal) 
            t3.start()
            # os.system('gnome-terminal')
        elif 'file management' in voice or 'filesystem' in voice or 'files management' in voice or 'files' in voice :
            t4 = threading.Thread(target=files) 
            t4.start()
            # os.system('xdg-open /home/subhankar')
        elif 'notpad' in voice or 'gedit' in voice or 'text editor' in  voice :
            t1 = threading.Thread(target=texteditor) 
            t1.start()
            # os.system('gedit')
        else :
                webbrowser.open('https://google.com/search?q='+voice)
    elif 'exit' in command or 'tata' in command or 'goodbye' in command or 'quit' in command or 'bye bye' in command :
        speak("good bye dear have a great day")
        exit(1)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'date' in command:
        d2 = today.strftime("%B %d, %Y")
        speak(d2)
        print(d2)
    elif 'temperature' in command or 'weather' in command :
        check_weather()
    else : 
        if command != '' :
            speak('Here what we found in web')
            webbrowser.open('https://google.com/search?q='+command)
        else :
            pass
            
   
