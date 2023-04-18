from assistant import Medea

medea = Medea()

while True:
    user_input = input("> ")
    response = medea.respond_to(user_input)
    print(response)
