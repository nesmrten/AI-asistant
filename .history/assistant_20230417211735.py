import speech_recognition as sr
import pyttsx3
import spacy
import webbrowser
from datetime import datetime

# initialize the speech recognition engine and NLP
r = sr.Recognizer()
nlp = spacy.load('en_core_web_sm')

# initialize the text-to-speech engine
engine = pyttsx3.init()

# define the function for the assistant's responses
def respond(text):
    print("Medea:", text)
    engine.say(text)
    engine.runAndWait()

# define the function for getting user input
def get_input():
    with sr.Microphone() as source:
        print("You:", end="")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            input_text = r.recognize_google(audio)
            print(input_text)
            return input_text
        except sr.UnknownValueError:
            respond("Sorry, I did not get that. How can I assist you?")
            return get_input()
        except sr.RequestError:
            respond("Sorry, I am having trouble accessing the microphone. How can I assist you?")
            return get_input()

# define the function for handling user commands
def handle_command(command):
    doc = nlp(command)

    # check for specific keywords in the user command
    if "open" in command:
        for ent in doc.ents:
            if ent.label_ == "website":
                webbrowser.open(ent.text)
                respond(f"Opening {ent.text} now.")
                return
        respond("I'm sorry, which website would you like me to open?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        respond(f"The current time is {current_time}.")
    else:
        respond("I'm sorry, I'm not sure how to help with that.")

# main loop for the assistant
while True:
    respond("How can I assist you?")
    command = get_input().lower()
    handle_command(command)
