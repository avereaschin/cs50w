from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:psw@localhost/books')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

app.secret_key = b'ayaya'

@app.route('/')
def login(error=False):
    return render_template('login.html', error=error)

@app.route('/login_attempt', methods=['POST'])
def login_attempt():
    username = request.form.get('username')
    password = request.form.get('password')

    if db.execute('SELECT id FROM users WHERE USERNAME = :USERNAME AND PASSWORD = :PASSWORD', 
                 {'USERNAME': username, 'PASSWORD': password}).rowcount == 1:       
        return render_template('index.html')
    else:
        return render_template('login.html', error=True)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registration', methods=['POST'])
def registration():
    
    username = request.form.get('username')
    password = request.form.get('password')
    db.execute('INSERT INTO users (USERNAME, PASSWORD) VALUES (:USERNAME, :PASSWORD)',
                {'USERNAME': username, 'PASSWORD': password})
    db.commit()
    if db.execute('SELECT * FROM users').rowcount != 0:
        return render_template('success.html', message='YASS', username=username)
    else:
        return render_template('success.html', message='NOOO')

@app.route('/success', methods=['POST'])
def success():
    message = 'Success'
    return render_template('success.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)