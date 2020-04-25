from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.SmallInteger, primary_key=True)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.SmallInteger, nullable=False)

    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()

class Passenger(db.Model):
    __tablename__ = 'passengers'
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
