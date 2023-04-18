import speech_recognition as sr
import pyttsx3
from medea_avatar import display_avatar

# define the main function
def main():
    # initialize speech recognizer and text-to-speech engine
    r = sr.Recognizer()
    engine = pyttsx3.init()
    
    # display the avatar
    display_avatar()
    
    # speak a greeting
    engine.say("Hello, I am Medea. How may I assist you?")
    engine.runAndWait()

    # take user input
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # recognize user input
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        engine.say("You said: " + text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        engine.say("Sorry, I could not understand what you said.")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        engine.say("Could not request results. Please try again later.")
        engine.runAndWait()

# call the main function
if __name__ == '__main__':
    main()
