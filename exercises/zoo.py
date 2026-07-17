class Animal:
    def eat(self):
        print("Animal eats food.")

class Lion(Animal):
    def eat(self):
        print("Lion eats meat.")

class Elephant(Animal):
    def eat(self):
        print("Elephant eats grass.")

class Parrot(Animal):
    def eat(self):
        print("Parrot eats seeds")


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def feed_all(self):
        for animal in self.animals:
            animal.eat()

z1 = Zoo()
z1.add_animal(Lion())
z1.add_animal(Elephant())
z1.add_animal(Parrot())
z1.feed_all()