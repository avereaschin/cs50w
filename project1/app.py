from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index', methods=['POST'])
def index():
    
    return render_template('index.html')