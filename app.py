from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "Every moment is a fresh beginning.",
    "Don't watch the clock; do what it does. Keep going.",
    "Act as if what you do makes a difference. It does.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts."
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    quote = random.choice(quotes)
    return render_template('greet.html', name=name, quote=quote)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
