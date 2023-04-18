from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Medeya(ChatBot):
    """
    A custom chat bot for a healthcare organization.
    """

    def __init__(self, **kwargs):
        super().__init__(
            'Medeya',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.5,
                    'default_response': 'I am sorry, but I do not understand.'
                }
            ],
            **kwargs
        )

        # Start by training our bot with the ChatterBot corpus data
        self.trainer = ChatterBotCorpusTrainer(self)
        self.trainer.train('chatterbot.corpus.english')

