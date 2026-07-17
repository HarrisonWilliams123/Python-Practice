class Vector:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def __add__(self, other):
        return Vector(self.num1 + other.num1, self.num2 + other.num2)
    
    def __repr__(self):
        return f"Vector({self.num1}, {self.num2})"
    
v1 = Vector(2,3)
v2 = Vector(4,1)

result = v1 + v2
print(result)
