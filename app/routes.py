from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, Admin, Clients, Airplane, FlightStatus, Gate, Airport, Flights, Bookings, CustomerReviews

main = Blueprint('main', __name__)

# Admin Login Endpoint
@main.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    admin = Admin.query.filter_by(username=data['username']).first()
    
    if admin and check_password_hash(admin.password, data['password']):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Create Client Endpoint
@main.route('/createclient', methods=['POST'])
def create_client():
    data = request.json
    new_client = Clients(
        fname=data['fname'],
        mname=data.get('mname'),
        lname=data['lname'],
        phone=data['phone'],
        email=data['email'],
        passport=data['passport'],
        password=generate_password_hash(data['password'])
    )
    
    db.session.add(new_client)
    db.session.commit()
    
    return jsonify({'client_id': new_client.client_id}), 201

# Get All Clients Endpoint
@main.route('/clients', methods=['GET'])
def get_clients():
    try:
        clients = Clients.query.all()
        return jsonify([{
            'client_id': client.client_id,
            'fname': client.fname,
            'mname': client.mname,
            'lname': client.lname,
            'email': client.email,
            'phone': client.phone,
            'passport': client.passport
        } for client in clients]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get Flight Status Endpoint
@main.route('/flight-status', methods=['GET'])
def get_flight_status():
    try:
        statuses = FlightStatus.query.all()
        return jsonify([{
            'flightStatus_id': status.flightStatus_id,
            'status': status.status
        } for status in statuses]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get Flights Endpoint
@main.route('/flights', methods=['GET'])
def get_flights():
    try:
        flights = Flights.query.all()
        return jsonify([{
            'flight_id': flight.flight_id,
            'flight_number': flight.flight_number,
            'departure_airport_code': flight.departure_airport_code,
            'arrival_airport_code': flight.arrival_airport_code,
            'departure_date': flight.departure_date,
            'arrival_date': flight.arrival_date,
            'airplane_id': flight.airplane_id,
            'flight_status_id': flight.flight_status_id,
            'gate_no': flight.gate_no
        } for flight in flights]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get Customer Reviews Endpoint
@main.route('/customer-reviews', methods=['GET'])
def get_customer_reviews():
    try:
        reviews = CustomerReviews.query.all()
        return jsonify([{
            'review_id': review.review_id,
            'client_id': review.client_id,
            'flight_id': review.flight_id,
            'rating': review.rating,
            'comment': review.comment
        } for review in reviews]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get Airports Endpoint
@main.route('/airports', methods=['GET'])
def get_airports():
    try:
        airports = Airport.query.all()
        return jsonify([{
            'airport_code': airport.airport_code,
            'airport_name': airport.airport_name,
            'city': airport.city,
            'gate_no': airport.gate_no
        } for airport in airports]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get Booking Details Endpoint (Confidential)
@main.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Bookings.query.all()
        return jsonify([{
            'booking_id': booking.booking_id,
            'client_id': booking.client_id,  # Consider masking or omitting sensitive info
            'flight_id': booking.flight_id,
            'seat_number': booking.seat_number,
            'booking_date': booking.booking_date,
            'price': booking.price  # Consider omitting or masking price info if needed
        } for booking in bookings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
