from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return f'Thank you {name} for your message: {message}. We will contact you soon at {email}'

if __name__ == '__main__':
    app.run()
