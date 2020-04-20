from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://root:psw@localhost/flight_data')
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    flights = db.execute('SELECT * FROM flights').fetchall()
    return render_template('index.html', flights=flights)

@app.route('/book', methods=['POST'])
def book():
    """Book a flight"""

    name = request.form.get('name')
    try:
        flight_id = request.form.get('flight_id')
    except ValueError:
        return render_template('error.html', message='Invalid flight number')

    if db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).rowcount == 0:
        return render_template('error.html', message='No flight with that id')
    
    db.execute('INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)',
                {'name': name, 'flight_id': flight_id})
    db.commit()
    return render_template('success.html')

@app.route('/flights') 
def flights():
    """Lists all flights"""

    flights = db.execute('SELECT * FROM flights').fetchall()
    return render_template('flights.html', flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    """Lists details about an individual flight."""

    flight = db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).fetchone()
    if flight is None:
        return render_template('error.html', message='Flight does not exist')

    passengers = db.execute('SELECT * FROM passengers WHERE flight_id=:flight_id', 
                            {'flight_id': flight_id}).fetchall()
    return render_template('flight.html', flight=flight, passengers=passengers)
    