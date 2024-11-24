CREATE DATABASE airline_management_system_db;

USE airline_management_system_db; 
CREATE TABLE admin (
  username VARCHAR(30) NOT NULL PRIMARY KEY,
  password VARCHAR(255) NOT NULL -- Store password hash, not plain text
);

INSERT INTO admin (username, password) 
VALUES ('cynotryl', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'); 

CREATE TABLE clients (
  client_id INT PRIMARY KEY AUTO_INCREMENT,
  fname VARCHAR(25) NOT NULL,
  mname VARCHAR(25),
  lname VARCHAR(25) NOT NULL,
  phone VARCHAR(14) NOT NULL,
  email VARCHAR(40) NOT NULL,
  passport VARCHAR(40) NOT NULL,
  password VARCHAR(255) NOT NULL -- Store password hash, not plain text
);



INSERT INTO clients (fname, mname, lname, phone, email, passport, password) 
VALUES 
  ('NISHANT', NULL, 'GUPTA', '+918273363640', 'nishantgupta3009@gmail.com', '123', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('AMAN', NULL, 'Kumar', '+923317534907', 'amankumar@gmail.com', '124', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('harsh', NULL, 'verma', '+443317534909', 'harshverma@gmail.com', '126', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('ronit', NULL, 'jaiswal', '+1233317534910', 'ronit@gmail.com', '127', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('ram',null, 'gupta', '+443317534911', 'ram@gmail.com', '128', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('mohan', null, ' ', '+9783317534912', 'ABDULLAHKHAWAJAGHORI@GMAIL.COM', '129', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('krishna', NULL, 'kaushik', '+923317534913', 'MUHAMMADSAAD@GMAIL.COM', '130', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.'),
  ('balram', NULL, ' ', '+943317534914', 'MUHAMMADMARIJ@GMAIL.COM', '131', '$2y$10$8n2c5o33q03eU7F2M7H9OeC0u.89H.u158T0/v9x/M.dU3e9s9E.');

CREATE TABLE airplane (
  airplane_id INT NOT NULL PRIMARY KEY,
  max_seats INT NOT NULL
);

INSERT INTO airplane (airplane_id, max_seats) VALUES
  (41, 100),
  (42, 100),
  (43, 300),
  (44, 100),
  (45, 300),
  (46, 100),
  (47, 100),
  (48, 300),
  (49, 100),
  (50, 300);

CREATE TABLE flightstatus (
  flightStatus_id INT PRIMARY KEY,
  status VARCHAR(100)
);

INSERT INTO flightstatus (flightStatus_id, status) VALUES
  (61, 'Departed'),
  (62, 'Landed'),
  (63, 'Delayed'),
  (64, 'Boarding'),
  (65, 'On Time');
  
SELECT * FROM flightstatus;

CREATE TABLE gates (
  gate_no INT PRIMARY KEY
);

INSERT INTO gates (gate_no) VALUES
  (66), (67), (68), (69), (70), (71), (72), (73), (74), (75);

CREATE TABLE airport (
  airport_code VARCHAR(3) PRIMARY KEY,
  airport_name VARCHAR(100),
  city VARCHAR(85), 
  gate_no INT,
  FOREIGN KEY (gate_no) REFERENCES gates(gate_no) 
);

CREATE TABLE flights (
  flight_id INT PRIMARY KEY AUTO_INCREMENT,
  flight_number VARCHAR(10) NOT NULL,
  departure_airport_code VARCHAR(3) NOT NULL,
  arrival_airport_code VARCHAR(3) NOT NULL,
  departure_date DATETIME NOT NULL,
  arrival_date DATETIME NOT NULL,
  airplane_id INT NOT NULL,
  flight_status_id INT NOT NULL,
  gate_no INT NOT NULL,
  FOREIGN KEY (departure_airport_code) REFERENCES airport(airport_code),
  FOREIGN KEY (arrival_airport_code) REFERENCES airport(airport_code),
  FOREIGN KEY (airplane_id) REFERENCES airplane(airplane_id),
  FOREIGN KEY (flight_status_id) REFERENCES flightstatus(flightStatus_id),
  FOREIGN KEY (gate_no) REFERENCES gates(gate_no)
);

CREATE TABLE bookings (
  booking_id INT PRIMARY KEY AUTO_INCREMENT,
  client_id INT NOT NULL,
  flight_id INT NOT NULL,
  seat_number VARCHAR(5),
  booking_date DATETIME NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE customer_reviews (
  review_id INT PRIMARY KEY AUTO_INCREMENT,
  client_id INT NOT NULL,
  flight_id INT NOT NULL,
  rating INT,
  comment TEXT,
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE airport_employees (
  employee_id INT PRIMARY KEY AUTO_INCREMENT,
  airport_code VARCHAR(3) NOT NULL,
  employee_name VARCHAR(100) NOT NULL,
  role VARCHAR(50) NOT NULL,
  FOREIGN KEY (airport_code) REFERENCES airport(airport_code)
);

INSERT INTO airport (airport_code, airport_name, city, gate_no) VALUES
  ('JFK', 'John F. Kennedy International Airport', 'New York City', 66),
  ('LHR', 'London Heathrow Airport', 'London', 67),
  ('CDG', 'Charles de Gaulle Airport', 'Paris', 68),
  ('DXB', 'Dubai International Airport', 'Dubai', 69);

INSERT INTO flights (
  flight_number, departure_airport_code, arrival_airport_code, departure_date, arrival_date, 
  airplane_id, flight_status_id, gate_no
) VALUES (
  'BA200', 'LHR', 'JFK', '2023-12-01 10:00:00', '2023-12-01 13:00:00', 
  41, 65, 67
);

-- Ensure client with client_id =1 exists before this insert
INSERT INTO bookings (client_id, flight_id, seat_number, booking_date, price) VALUES (
  1, 1, '23A', '2023-11-28 14:30:00', 500.00
);

-- Ensure client with client_id =1 and flight with flight_id =1 exist before this insert
INSERT INTO customer_reviews (client_id, flight_id, rating, comment) VALUES (
  1, 1, 4, 'Good flight, but the food could be better.'
);

SELECT * FROM clients;
SELECT * FROM flightstatus;

