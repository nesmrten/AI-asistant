import random

class Medea:
    def __init__(self):
        self.name = "Medea"
        self.greetings = ["hello", "hi", "hey", "hi there", "hello there"]
        self.farewells = ["bye", "goodbye", "see you later", "farewell", "have a nice day"]
        self.commands = ["what can you do", "help", "commands"]
        self.jokes = ["Why did the tomato turn red? Because it saw the salad dressing!",
                      "Why don’t scientists trust atoms? Because they make up everything!",
                      "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus!",
                      "I told my wife she was drawing her eyebrows too high. She looked surprised.",
                      "Why don’t seagulls fly by the bay? Because then they would be bagels!"]
        self.facts = ["The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
                      "The world’s largest snowflake on record was 15 inches wide and 8 inches thick. It fell in Fort Keogh, Montana on January 28, 1887.",
                      "A cockroach can live for several weeks without its head. It dies eventually because it cannot eat or drink water without a mouth.",
                      "The longest place name in the world is Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu, a hill in New Zealand.",
                      "The first known recipe for ice cream was written in 1665 and included the ingredients: milk, cream, butter, and eggs."]

    def greeting(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def command_list(self):
        return "Here are some commands you can try: " + ", ".join(self.commands)

    def tell_joke(self):
        return random.choice(self.jokes)

    def random_fact(self):
        return random.choice(self.facts)

    def respond(self, message):
        if message.lower() in self.greetings:
            return self.greeting()
        elif message.lower() in self.farewells:
            return self.farewell()
        elif message.lower() in self.commands:
            return self.command_list()
        elif "joke" in message.lower():
            return self.tell_joke()
        elif "fact" in message.lower():
            return self.random_fact()
        else:
            return "I'm sorry, I don't understand. Please try asking me something else."

medea = Medea()
