
# ********** Lec 4 [ Attributes and Methods ]

# Attributes = variables stored inside an object or class
# Methods    = functions defined inside a class


#**************************************************
#! Defining variables inside __init__ (Instance Variables)
#**************************************************
#**************************************************


class Student:
    def __init__(self, roll_no, name):        # <-- Parameters (function variables)
        self.roll_no = roll_no                # <-- Instance variable
        self.name = name                      # self.<variable> = instance variable

    def display(self):                         # <-- Instance method
        print(self.roll_no, self.name)


s0 = Student(0, 'Bhawesh')
s0.display()

s1 = Student(1, 'Rahul')
s1.display()

'''
- __init__() is the constructor of the class.
- Python automatically calls __init__ when you create an object.

- self represents the current object.
  When we write s0 = Student(0, "Alex"), inside __init__:
        self → s0

- Variables defined inside __init__ (with self.*) are INSTANCE VARIABLES.
  Each object gets its own separate copy (s0 has its own, s1 has its own).
'''


