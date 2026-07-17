class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        total = 0
        for num in self.marks:
            total = total + num
        return total / len(self.marks)

s1 = Student("Alice", [85, 90, 78, 92, 88])
print("Alice's Average Grade:",s1.average())
