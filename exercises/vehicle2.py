class Vehicle:
    color = "White"
    
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed
        
v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.make} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.make} - Color: {v2.color}, Speed: {v2.speed}")

Vehicle.color = "Red"

print(f"{v1.make} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.make} - Color: {v2.color}, Speed: {v2.speed}")