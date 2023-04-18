import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

class Medea:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.greet()

    def greet(self):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            self.say("Good Morning!")
        elif hour >= 12 and hour < 18:
            self.say("Good Afternoon!")
        else:
            self.say("Good Evening!")
        self.say("I am your digital assistant Medea. How can I help you?")

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'medea' in command:
                    command = command.replace('medea', '')
                    print(command)
        except:
            pass
        return command

    def run_medea(self):
        command = self.listen()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.say('Current time is ' + time)
        elif 'search' in command:
            self.say('What do you want me to search for?')
            search = self.listen()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            self.say('Here is what I found for ' + search)
        elif 'find location' in command:
            self.say('What is the location?')
            location = self.listen()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            self.say('Here is the location of ' + location)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            self.say(info)
        elif 'open' in command:
            app = command.replace('open', '')
            os.startfile(app)
        elif 'email to' in command:
            try:
                self.say('What should I say?')
                content = self.listen()
                to = command.replace('email to', '')
                self.send_email(to, content)
                self.say('Email has been sent!')
            except Exception as e:
                print(e)
                self.say('Sorry, I am not able to send this email at the moment.')
        elif 'quit' in command:
            self.say('Goodbye!')
            quit()
        else:
            self.say('Sorry, I did not understand what you said.')

    def send_email(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email_address@gmail.com', 'your_email_password')
        server.sendmail('your_email_address@gmail.com', to, content)
        server.close()
