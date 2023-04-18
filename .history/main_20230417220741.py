from assistant import Medea

medea = Medea()

while True:
    user_input = input("> ")
    response = medea.respond(user_input)
    print(response)
