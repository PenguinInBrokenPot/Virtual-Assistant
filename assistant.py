# 18th of March in year 2022
#Status : Failed.
#Reason : due to unavailability of Bluetooth or input device.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def jarvisvoice(audioinput):
    engine.say(audioinput)
    engine.runAndWait()

def wish():
    h=int(datetime.datetime.now().hour)
    print("---->",h)
    if h>=0 and h<=12:
        jarvisvoice("suprabhaatam")
    elif h>=12 and h<=18:
        jarvisvoice("śubhasāyam")
    else :
        jarvisvoice("Shubh Ratri")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        # jarvisvoice("Recognizing....")
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("user said : "+query)
    except Exception as e :
        print(e)
        # jarvisvoice("sorry... Say that again please")
        print("sorry... Say that again please")
        return "None"
    return query


jarvisvoice("Namaskar Saheb")
wish()

status = True
while status:
    query= takecommand().lower()

    if "what is" in query or "who is" in query:
        jarvisvoice("searching in wikipedia")
        query = query.replace("wikipedia","")
        result=wikipedia.summary(query, sentences=2)
        print("AS per wikipedia,\n\t\t"+result)
        jarvisvoice("ACCORDING TO WIKIPEDIA...,")
        jarvisvoice(result)
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open gmail" in query:
        webbrowser.open_new_tab("gmail.com")