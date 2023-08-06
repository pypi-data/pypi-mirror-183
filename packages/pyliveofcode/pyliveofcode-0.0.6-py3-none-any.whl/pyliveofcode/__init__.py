import tkinter 
import random
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition==3.8.0
from googletrans import Translator # pip install googletrans
import webbrowser

def math(n1umber,operators,n2umber):
    if "+" in operators:
        print(int(n1umber)+int(n2umber))
    elif "-" in operators:
        print(int(n1umber)-int(n2umber))
    elif "*" in operators:
        print(int(n1umber)*int(n2umber))
    elif "/" in operators:
        print(int(n1umber)/int(n2umber))
    elif "%" in operators:
        print(int(n1umber)%int(n2umber))
    elif "**" in operators:
        print(int(n1umber)**int(n2umber))
    elif "//" in operators:
        print(int(n1umber)//int(n2umber))

def makepassword():
    passwordmaker = random.random()
    float(passwordmaker)
    str(passwordmaker)
    print("here is the password sir:",passwordmaker)
    print("sir 0. is not in the password")
    password =passwordmaker
def makefile(dx,name,ex):
    fileopen1 = open(dx+name+ex,"w")
    fileopen1.close
def write(text):
    print(text)

def Listen(languagename):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language=languagename)

    except:
        return ""
    
    query = str(query).lower()
    return query
def Speak(Text):
     engine = pyttsx3.init("sapi5")
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     engine.setProperty('rate',170)
     engine.say(Text)
     engine.runAndWait()
def Translatortext(text,languagenameoftranslator):
    line = str(text)
    translate = Translator()
    result = translate.translate(line,languagenameoftranslator)
    data = result.text
    print(data)
    return data
def inputtofile(dx,inputsreen):
    input1 = input(inputsreen)
    d=open(dx,"w")
    d.write(input1)
    d.close()
def search(url):
    webbrowser.open("https://www.google.com/search?q="+url)
def searchwebsite(url):
    webbrowser.open_new_tab(url)
