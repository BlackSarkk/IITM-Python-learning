

#**************************************************
#! Defining variables directly inside the class (Class Variable)
#**************************************************
#**************************************************


class Student:
    count = 0     # <-- Class variable (shared by all objects)

    def __init__(self, roll_no, name):
        self.roll_no = roll_no      # Instance variable
        self.name = name

    def display(self):
        print(self.roll_no, self.name)


s0 = Student(0, 'Bhawesh')
s0.display()
Student.count += 1

s1 = Student(1, 'Rahul')
s1.display()
Student.count += 1

print(Student.count)

'''
- Variables defined directly inside the class are CLASS VARIABLES.
- A class variable belongs to the CLASS itself, not to any individual object.

- All objects share the same copy of class variables.
  (s0 and s1 do NOT have separate count variables)
'''

