
from Person import Person

class Student(Person):  # <-- Child class (inherits from Person)
    def __init__(self, name, age, marks):
        super().__init__(name, age)   # Calls parent's constructor
        self.marks = marks
    
    def display(self):  # Method overriding
        super().display()      
        print(self.marks)
