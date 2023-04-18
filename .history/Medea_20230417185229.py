import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to listen for user input and return the spoken text
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition service: {e}")
        return ""

# Define a function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Example usage
speak("Hello! How can I help you today?")
text = get_audio()
speak(f"You said: {text}")