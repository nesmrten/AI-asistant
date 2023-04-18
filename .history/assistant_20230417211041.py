import os
import webbrowser
import subprocess
import wikipedia
import speech_recognition as sr
import pyttsx3
import spacy
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize NLP
nlp = spacy.load("en_core_web_sm")


class AssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Medea Assistant")
        self.setGeometry(100, 100, 800, 500)

        # Create GUI elements
        self.title_label = QLabel(self)
        self.title_label.setText("Medea Assistant")
        self.title_label.move(300, 50)
        self.title_label.setStyleSheet("font-size: 30px; font-weight: bold;")

        self.chat_log = QPlainTextEdit(self)
        self.chat_log.move(50, 100)
        self.chat_log.resize(700, 300)
        self.chat_log.setReadOnly(True)

        self.user_input = QLineEdit(self)
        self.user_input.move(50, 420)
        self.user_input.resize(600, 50)
        self.user_input.returnPressed.connect(self.get_input)

        self.send_button = QPushButton(self)
        self.send_button.setText("Send")
        self.send_button.move(670, 420)
        self.send_button.resize(80, 50)
        self.send_button.clicked.connect(self.get_input)

        # Start AI assistant
        self.speak("Hello! I am Medea. How can I assist you?")

    def get_input(self):
        user_input = self.user_input.text()
        self.chat_log.appendPlainText("You: " + user_input)
        self.user_input.setText("")
        self.process_input(user_input)

    def process_input(self, input_text):
        # Perform NLP on input text
        doc = nlp(input_text)

        # Check for specific commands
        if "open" in input_text:
            self.speak("Opening " + input_text.replace("open ", ""))
            webbrowser.open(input_text.replace("open ", ""))
        elif "search" in input_text:
            search_query = input_text.replace("search ", "")
            self.speak("Searching for " + search_query)
            webbrowser.open("https://www.google.com/search?q=" + search_query)
        elif "wiki" in input_text:
            search_query = input_text.replace("wiki ", "")
            self.speak("Searching Wikipedia for " + search_query)
            summary = wikipedia.summary(search_query, sentences=2)
            self.speak(summary)
        elif "run" in input_text:
            script_name = input_text.replace("run ", "")
            self.speak("Running script " + script_name)
            subprocess.Popen(["python", script_name + ".py"])
        elif "exit" in input_text:
            self.speak("Goodbye!")
            QApplication.quit()
        else:
            self.speak("Sorry, I did not understand that.")

    def speak(self, text):
        # Output speech using text-to-speech engine
        engine.say(text)
        engine.runAndWait()
        self.chat_log.appendPlainText("Medea: " + text)


if __name__ == '__main__':
    app = QApplication([])
    window = AssistantGUI()
   
