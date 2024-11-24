from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(255), nullable=False)  # Store password hash

class Clients(db.Model):
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    mname = db.Column(db.String(25))
    lname = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    passport = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(255), nullable=False)   

class Airplane(db.Model):
    airplane_id = db.Column(db.Integer, primary_key=True)
    max_seats = db.Column(db.Integer, nullable=False)

class FlightStatus(db.Model):
    flightStatus_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))

class Gate(db.Model):
    gate_no = db.Column(db.Integer, primary_key=True)

class Airport(db.Model):
    airport_code = db.Column(db.String(3), primary_key=True)
    airport_name = db.Column(db.String(100))
    city = db.Column(db.String(85))
    gate_no = db.Column(db.Integer, db.ForeignKey('gate.gate_no'))
    
    gate = db.relationship('Gate', backref='airports')

class Flights(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), nullable=False)
    departure_airport_code = db.Column(db.String(3), db.ForeignKey('airport.airport_code'), nullable=False)
    arrival_airport_code = db.Column(db.String(3), db.ForeignKey('airport.airport_code'), nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    arrival_date = db.Column(db.DateTime, nullable=False)
    airplane_id = db.Column(db.Integer, db.ForeignKey('airplane.airplane_id'), nullable=False)
    flight_status_id = db.Column(db.Integer, db.ForeignKey('flight_status.flightStatus_id'), nullable=False)
    gate_no = db.Column(db.Integer, db.ForeignKey('gate.gate_no'))

    departure_airport = db.relationship('Airport', foreign_keys=[departure_airport_code])
    arrival_airport = db.relationship('Airport', foreign_keys=[arrival_airport_code])
    airplane = db.relationship('Airplane')
    flight_status = db.relationship('FlightStatus')
    
class Bookings(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)
    seat_number = db.Column(db.String(5), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)

    client = db.relationship('Clients')
    flight = db.relationship('Flights')

class CustomerReviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Assuming rating is an integer
    comment = db.Column(db.Text)

    client = db.relationship('Clients')
    flight = db.relationship('Flights')
