from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    header = 'Hello'
    return render_template('index.html', header=header)
@app.route('/bye')
def bye():
    header = 'Bye'
    return render_template('index.html', header=header)

