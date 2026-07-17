class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_id, capacity):
        self.passengers = []
        self.capacity = capacity
        self.flight_id = flight_id
    
    def book(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} booked on Flight {self.flight_id}.")
        else:
            print(f"Sorry, Flight {self.flight_id} is fully booked.")
    
f = Flight("AI202", 2)
f.book(Passenger("Alice"))
f.book(Passenger("Bob"))
f.book(Passenger("Charlie"))

