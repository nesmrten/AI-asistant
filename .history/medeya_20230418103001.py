from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Medeya:
    
    def __init__(self):
        
        self.chatbot = ChatBot(
            "Medeya",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            preprocessors=[
                "chatterbot.preprocessors.clean_whitespace",
                "chatterbot.preprocessors.unescape_html",
            ],
            database_uri="sqlite:///database.sqlite3"
        )
        
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        
        # Train the chatbot based on the english corpus
        self.trainer.train("chatterbot.corpus.english")
        
    def get_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        return str(response)
