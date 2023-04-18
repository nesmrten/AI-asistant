import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import random

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

class Medea:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def process_input(self, user_input):
        # Tokenize the input
        tokens = nltk.word_tokenize(user_input)

        # Tag the tokens with their part-of-speech
        tagged_tokens = nltk.pos_tag(tokens)

        # Lemmatize the tokens using their POS tag
        lemmatized_tokens = []
        for token, tag in tagged_tokens:
            pos = self.get_wordnet_pos(tag)
            if pos:
                lemmatized_tokens.append(self.lemmatizer.lemmatize(token, pos))
            else:
                lemmatized_tokens.append(self.lemmatizer.lemmatize(token))

        return lemmatized_tokens

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    def generate_response(self, user_input):
        responses = [
            "I'm sorry, I don't understand.",
            "Can you please rephrase that?",
            "I'm not sure what you're asking.",
            "Could you please provide more context?",
            "I'm afraid I don't have an answer for that.",
        ]

        # Process the input
        tokens = self.process_input(user_input)

        # Check if input contains certain keywords
        if 'hello' in tokens or 'hi' in tokens:
            return "Hello! How can I assist you today?"

        if 'bye' in tokens or 'goodbye' in tokens:
            return "Goodbye! Have a nice day."

        if 'weather' in tokens:
            return "I'm sorry, I'm not currently able to provide weather information."

        # Generate a random response
        response = random.choice(responses)
        return response
