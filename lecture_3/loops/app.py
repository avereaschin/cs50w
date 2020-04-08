from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Alice', 'Bob', 'John']
    return render_template('index.html', names=names)