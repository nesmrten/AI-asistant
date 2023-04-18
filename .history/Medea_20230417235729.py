from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Medea:
    def __init__(self):
        self.bot = ChatBot('Medea')
        self.trainer = ListTrainer(self.bot)
        self.train_bot()

    def train_bot(self):
        self.trainer.train([
            "Hi",
            "Hello!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome.",
            "What is your name?",
            "My name is Medea, I'm a chatbot.",
            "Who created you?",
            "I was created by a team of programmers.",
            "What can you do?",
            "I can help you with many things like answering questions, telling jokes and more!",
            "What kind of questions can you answer?",
            "I can answer questions about many things such as food, sports, entertainment and more!",
            "What is the weather like today?",
            "I'm sorry, I am not able to provide real-time weather information at the moment.",
            "What is your favorite color?",
            "I'm sorry, I don't have a favorite color as I am a machine.",
            "What is the meaning of life?",
            "The meaning of life is subjective and varies from person to person.",
            "What is your favorite food?",
            "I'm sorry, I don't eat as I am a machine.",
            "Can you tell me a joke?",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "Goodbye",
            "Bye!"
        ])

    def reply(self, msg):
        response = self.bot.get_response(msg)
        return str(response)
