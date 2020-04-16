import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='psw',
    db='flight_data'
)

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS flights')

# flights table
create_table1 = """ CREATE TABLE flights (
                    id SMALLINT AUTO_INCREMENT PRIMARY KEY, 
                    origin VARCHAR(255) NOT NULL,
                    destination VARCHAR(255) NOT NULL,
                    duration SMALLINT NOT NULL
)

"""

c.execute(create_table1)

c.execute('DROP TABLE IF EXISTS passengers')

# passengers table
create_table2 = """ CREATE TABLE passengers (
                    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    flight_id SMALLINT,
                    FOREIGN KEY (flight_id) REFERENCES flights(id)
)

"""

c.execute(create_table2)

# flights table date
flight_data = [
    ['New York', 'London', '415'],
    ['Shanghai', 'Paris', '760'],
    ['Istanbul', 'Tokyo', '700'],
    ['New York', 'Paris', '435'],
    ['Moscow', 'Paris', '245'],
    ['Lima', 'New York', '455']
]

insert_into_flights = """INSERT INTO flights
    (origin, destination, duration)
    VALUES (%s, %s, %s)
"""

for i in flight_data:
    c.execute(insert_into_flights, tuple(i))

# passengers table data
passengers = [
    ['Alice', '1'],
    ['Bob', '1'],
    ['Charlie', '2'],
    ['Dave', '2'],
    ['Erin', '4'],
    ['Frank', '6'],
    ['Grace', '6']
]

insert_into_passengers = """INSERT INTO passengers
    (name, flight_id)
    VALUES (%s, %s)
"""

for i in passengers:
    c.execute(insert_into_passengers, tuple(i))

c.execute('UPDATE flights SET duration = 430 WHERE origin = "New York" and destination = "London"')

conn.commit()

