
# ********** Lec 5 [ Inheritance and Method Overriding ]


#**************************************************
#! Inheritance and MethodOverriding
#**************************************************
#**************************************************

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):  # <-- Child class (inherits from Person)
    def __init__(self, name, age, marks):
        super().__init__(name, age)   # Calls parent's constructor
        self.marks = marks
    
    def display(self):  # Method overriding
        super().display()      
        print(self.marks)


class Employee(Person): 
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def display(self):  # Method overriding
        super().display()        
        print(self.salary)


s = Student('Rida', 20, 250)
s.display()

e = Employee('Harsh', 30, 50000)
e.display()


#? Sometimes parent class is referred as super class and child class is referred as sub class
#? Based on number of superClass, subClasses and the relation between them, there are 5 different types of inheritance

#1. Simple Inheritance:                1 parent class - 1 child class
#2. Hirerarchiacal Inheritance:        1 parent class - multiple child classes
#3. Multiple Inheritance:       multiple parent class - 1 child classes
#4. MultiLevel Inheritance:     Parent Class - Intermediate class - Child class
#5. Hybrid Inheritance: Any combination of the above 4 Inheritance