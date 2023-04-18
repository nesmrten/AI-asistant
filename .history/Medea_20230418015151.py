import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Medeya:
    def __init__(self):
        # create a new chatbot
        self.chatbot = ChatBot(
            'Medeya',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.90
                }
            ]
        )

        # train the chatbot based on the english corpus
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train("chatterbot.corpus.english")

    def get_response(self, user_input):
        return str(self.chatbot.get_response(user_input))

