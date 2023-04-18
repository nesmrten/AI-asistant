import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyautogui

import spacy
nlp = spacy.load('en_core_web_sm')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish user according to current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant. How may I assist you?")  

# Function to take voice command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Function to open applications
def openApps(query):
    if 'open code' in query:
        os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open notepad' in query:
        os.system('notepad')

    elif 'open chrome' in query:
        os.system('chrome')

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com/")

    elif 'open stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com/")        

# Function to search on Wikipedia
def wikipediaSearch(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Function to play music
def playMusic():
    music_dir = 'D:\\Music'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))

# Function to set reminders
def setReminder(query):
    date = ''
    for word in query.split():
        if '-' in word or ':' in word:
            date += word
            date += ' '
    content = query.replace(date, '')
    speak("Reminder set!")
    os.system(f'start cmd /c "timeout /t 5 && echo Reminder: {content}"')

# Function to take screenshot
def takeScreenshot():
    img = pyautogui.screenshot()
    img.save('D:\\AI assistant\\screenshot.png')

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing
