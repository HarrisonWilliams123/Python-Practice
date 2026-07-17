class Character:
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1
    
    def gain_exp(self, add):
        total = self.exp + add
        if total >= 100:
            self.level += 1
            print(f"{self.name} gained {add} exp. Level up! Now Level {self.level}. (Remaining exp: {total - self.exp})")
            self.exp = total - self.exp
        else:
            self.exp = self.exp + add
            print(f"{self.name} gained {add} exp. (Total: {self.exp})")

c1 = Character("Aria", health=100)
c1.gain_exp(60)
c1.gain_exp(60)