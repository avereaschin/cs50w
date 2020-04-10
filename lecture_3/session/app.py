from flask import Flask, render_template, session, request

app = Flask(__name__)

app.secret_key = 'ayaya'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('notes') is None:
        session['notes'] = [] 
    if request.method == 'POST':
        note = request.form.get('note')
        session['notes'].append(note)

    return render_template('index.html', notes=session['notes'])
