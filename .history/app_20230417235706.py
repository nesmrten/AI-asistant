from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from Medea import Medea
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
medea = Medea()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def message():
    incoming_msg = request.values["msg"]
    response = medea.reply(incoming_msg)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
