import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='psw',
    db='flight_data'
)

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS flights')

create_table = """ CREATE TABLE flights (
                    id SMALLINT AUTO_INCREMENT PRIMARY KEY, 
                    origin VARCHAR(255) NOT NULL,
                    destination VARCHAR(255) NOT NULL,
                    duration SMALLINT NOT NULL
)

"""

c.execute(create_table)

data = [
    ['New York', 'London', '415'],
    ['Shanghai', 'Paris', '760'],
    ['Istanbul', 'Tokyo', '700'],
    ['New York', 'Paris', '435'],
    ['Moscow', 'Paris', '245'],
    ['Lima', 'New York', '455']
]

insert_data = """INSERT INTO flights
    (origin, destination, duration)
    VALUES (%s, %s, %s)
"""

for i in data:
    c.execute(insert_data, tuple(i))

c.execute('UPDATE flights SET duration = 430 WHERE origin = "New York" and destination = "London"')

conn.commit()

