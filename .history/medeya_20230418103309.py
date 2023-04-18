from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Medeya(ChatBot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_trainer(ChatterBotCorpusTrainer)
        self.train("chatterbot.corpus.english")

if __name__ == '__main__':
    medeya = Medeya(
        name='Medeya',
        storage_adapter='chatterbot.storage.SQLAlchemyStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

    print('Type something to begin...')

    while True:
        try:
            user_input = input()
            bot_response = medeya.get_response(user_input)
            print(bot_response)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break
