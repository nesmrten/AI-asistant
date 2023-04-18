import speech_recognition as sr
import pyttsx3
import spacy
import webbrowser
import os
import datetime
import wikipedia
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pyautogui
import psutil
import pyjokes
import pywhatkit
import requests
import json
import sys
from tkinter import *
from PIL import ImageTk, Image
import threading
import time

# create instance of spacy library
nlp = spacy.load("en_core_web_sm")

# create instance of speech recognition library
r = sr.Recognizer()

# set up text-to-speech engine
engine = pyttsx3.init()

# set voice to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# create dictionary of names and their respective emails
contact_dict = {
    "John": "john@example.com",
    "Jane": "jane@example.com"
}

# create dictionary of email providers and their respective SMTP server addresses and port numbers
provider_dict = {
    "gmail": ["smtp.gmail.com", 587],
    "yahoo": ["smtp.mail.yahoo.com", 465],
    "hotmail": ["smtp.live.com", 587],
    "outlook": ["smtp.office365.com", 587],
    "aol": ["smtp.aol.com", 587],
    "protonmail": ["smtp.protonmail.com", 587],
    "zoho": ["smtp.zoho.com", 465]
}

# set up GUI window
window = Tk()
window.geometry("400x400")
window.title("Medea")

# create chat history box
chat_history = Text(window, height=18, width=40, bg="#ffffff", fg="#000000", font=("Arial", 12))
chat_history.config(state=DISABLED)
chat_history.place(x=10, y=10)

# create input box
input_box = Entry(window, width=35, bg="#ffffff", fg="#000000", font=("Arial", 12))
input_box.place(x=10, y=350)


def get_text_input():
    """
    Gets text input from user and processes it
    """
    # get text input from input box
    input_text = input_box.get()

    # clear input box
    input_box.delete(0, END)

    # process input text
    process_text(input_text)


def add_chat_bot_response(response):
    """
    Adds chat bot response to chat history
    """
    # enable chat history editing
    chat_history.config(state=NORMAL)

    # add chat bot response to chat history
    chat_history.insert(END, "Medea: " + response + "\n")

    # disable chat history editing
    chat_history.config(state=DISABLED)

    # scroll chat history to bottom
    chat_history.see(END)


def add_user_input(input_text):
    """
    Adds user input to chat history
    """
    # enable chat history editing
    chat_history.config(state=NORMAL)

    # add user input to chat history
    chat_history.insert(END, "You: " + input_text + "\n")

    # disable chat history editing
    chat_history.config(state=DISABLED)

    # scroll chat history to bottom
    chat_history.see(END)


def process_text(input_text):
    """
    Processes user input text
    """
    # add user input to chat history
    add_user_input(input_text)

    # perform NLP on input text
    doc =
