from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+mysqlconnector://root:psw@localhost/flight_data')
db = scoped_session(sessionmaker(bind=engine))

def main():
    query = input('Enter flight ID:\n')

    flight = db.execute('SELECT origin, destination, duration FROM flights WHERE id = :id', 
                        {"id": query}).fetchone()

    if not flight:
        print('Invalid flight id')
        return

    passengers = db.execute('SELECT name FROM passengers WHERE flight_id = :flight_id',
                            {'flight_id': query}).fetchall()

    print('\nPassengers\n')

    if not passengers:
        print('No passengers on this flight')
    else:
        for passenger in passengers:
            print(passenger.name)

if __name__ == '__main__':
    main()

