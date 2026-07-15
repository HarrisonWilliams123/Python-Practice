class Animal():
    def speak(self):
        print("Animal makes a noise")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

dog = Dog()
cat = Cat()

dog.speak()

cat.speak()