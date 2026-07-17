class Multiplier:
    def __init__(self, num):
        self.num = num

    def __call__(self, other):
        return self.num * other

m1 = Multiplier(3)
print(m1(10))

m2 = Multiplier(5)
print(m2(7))