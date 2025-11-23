
# ********** Lec 5 [ Inheritance and Method Overriding ]


#**************************************************
#! Limiting some information to the class level
#**************************************************
#**************************************************


#? Note: Whenever we do inheritance, there is an issue of security,
#? i.e. everything there in the parent class is accessible in the child class 
#? What if we dont want child to access some info


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    #<--- now age wont go to its child, now the age become the private member

    def get_age(self):
        return self.__age   # <-- safe getter

    def display(self):
        print(self.name, self.get_age())


class Student(Person):  
    def __init__(self, name, age, marks):
        super().__init__(name, age) 
        self.marks = marks
    
    def display(self): 
        super().display()      
        print(self.marks)


class Employee(Person): 
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def display(self): 
        super().display()        
        print(self.salary)


s = Student('Rida', 20, 250)
s.display()

e = Employee('Harsh', 30, 50000)
e.display()

