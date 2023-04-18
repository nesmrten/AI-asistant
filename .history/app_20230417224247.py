from flask import Flask, render_template, request
from medea import Medea

app = Flask(__name__)

medea = Medea()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    response = medea.respond_to(user_input)
    return str(response)

if __name__ == "__main__":
    app.run()
