from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class Medeya(ChatBot):
    def __init__(self, **kwargs):
        super().__init__(
            'Medeya',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.5,
                    'default_response': 'I am sorry, but I do not understand.'
                }
            ],
            **kwargs
        )

        self.train()

    def train(self):
        conversation = [
            'Hello',
            'Hi there!',
            'How are you doing?',
            'I\'m doing great.',
            'That is good to hear',
            'Thank you.',
            'You\'re welcome.'
        ]

        self.set_trainer(ListTrainer)
        self.train(conversation)

        self.set_trainer(ChatterBotCorpusTrainer)
        self.train('chatterbot.corpus.english')
