class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150
            print(f"Latte Made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")
        
l1 = CoffeeMachine(300, 100, 200)
l1.make_latte()
l1.make_latte()