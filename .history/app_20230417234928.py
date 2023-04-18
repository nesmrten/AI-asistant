import os
from dotenv import load_dotenv
from medea import Medea
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
app.config["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

medea = Medea(app.config["OPENAI_API_KEY"])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["input"]
        medea_output = medea.generate_response(user_input)
        return render_template("index.html", input=user_input, output=medea_output)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
