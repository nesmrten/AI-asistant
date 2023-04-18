import os
from flask import Flask, render_template, request
from medeya import Medeya

app = Flask(__name__)

# initialize the Medeya AI assistant
assistant = Medeya()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = assistant.get_response(user_input)
    return str(bot_response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

