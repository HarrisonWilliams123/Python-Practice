class Light:

    def __init__(self):
        self.stat = False
    
    def turn_on(self):
        self.stat = True
        print("Light is ON")
    
    def turn_off(self):
        self.stat = False
        print("Light is OFF")

    def status(self):
        if self.stat:
            print("Current status: ON")
        else:
            print("Current Status: OFF")
        
l1 = Light()
l1.turn_on()
l1.status()
l1.turn_off()
l1.status()