from assistant import Medea

medea = Medea()

while True:
    user_input = input("You: ")
    response = medea.generate_response(user_input)
    print("Medea:", response)
