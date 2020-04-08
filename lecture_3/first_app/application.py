from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!!!'

@app.route('/andrei')
def andrei():
    return 'Hello, Andrei'

@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f'hello, {name}!'