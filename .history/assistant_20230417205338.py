import os
import time
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import pytz
import requests
from bs4 import BeautifulSoup
import spacy

# load the large English NLP model
nlp = spacy.load("en_core_web_sm")

# initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# set up speech recognition
r = sr.Recognizer()
r.pause_threshold = 0.7
r.energy_threshold = 4000

# define function for listening to microphone input
def listen():
    with sr.Microphone() as source:
        print("Medea: How can I assist you?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You: {text}")
        except:
            print("Sorry, I did not get that.")
            text = ""
        return text

# define function for speaking response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define function for opening a URL in the default web browser
def open_url(url):
    webbrowser.open(url)

# define function for getting current time
def get_time():
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%I:%M %p")

# define function for getting current date
def get_date():
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%B %d, %Y")

# define function for getting news headlines
def get_news():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    headlines = [i.get_text() for i in soup.find_all("h2")]
    return headlines[:5]

# define function for getting weather information
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY"
    r = requests.get(url)
    data = r.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"] - 273.15
    return f"The temperature in {city} is {temp:.2f}°C with {weather}."

# main program loop
while True:
    # listen for user input
    text = listen().lower()

    # perform NLP on input text
    doc = nlp(text)

    # extract entities from input text
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # check if input contains a greeting
    if any(token.text.lower() in ["hi", "hello", "hey"] for token in doc):
        greetings = ["Hello!", "Hi there!", "Greetings!"]
        greet = random.choice(greetings)
        speak(greet)

    # check if input contains a question about the current time
    elif any(token.text.lower() in ["time", "current time"] for token in doc):
        time = get_time()
        speak(f"The current time is {time}.")

    # check if input contains a question about the current date
    elif any(token.text.lower() in ["date", "today's date"] for token in doc):
        date = get_date()
        speak(f"Today's date is {date}.")

    # check
