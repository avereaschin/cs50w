class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers
        self.passengers = []

        # Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'Flight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}')

        print('\nPassengers:')
        for passenger in self.passengers:
            print(passenger.name)

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    
    def __init__(self, name):
        self.name = name

def main():

    # Create flight
    f = Flight(origin='New York', destination='Paris', duration=540)

    # Create passenegers
    alice = Passenger(name='Alice')
    bob = Passenger(name='Bob')

    f.add_passenger(alice)
    f.add_passenger(bob)

    f.print_info()

if __name__ == '__main__':
    main()