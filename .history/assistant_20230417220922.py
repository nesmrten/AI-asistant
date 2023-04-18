import nltk

class Medea:
    def __init__(self):
        nltk.download('punkt')
        self.greetings = ["hello", "hi", "hey", "what's up", "hey there"]
        self.goodbyes = ["goodbye", "bye", "see you later", "have a nice day"]
        
    def respond(self, user_input):
        if user_input.lower() in self.greetings:
            return "Hello! How can I assist you today?"
        elif user_input.lower() in self.goodbyes:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand what you said."
