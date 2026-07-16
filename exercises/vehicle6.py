class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    
    def get_speed(self):
        return self.max_speed

class Bike(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def describe(self):
        print(f"Bike max speed: {self.max_speed} km/h")

class Truck(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def describe(self):
        print(f"Truck max speed: {self.max_speed} km/h")

class Bus(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def describe(self):
        print(f"Bus max speed: {self.max_speed} km/h")


b1 = Bike(120)
t1 = Truck(90)
b2 = Bus(100)

b1.describe()
t1.describe()
b2.describe()