

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

s1 = Student(1, 'Rahul')
s1.display()



#**************************************************
#! Differnce btw having variable inside class and inside __init__ is
#**************************************************
#**************************************************


'''
- Whenever we have something inside __init__ it is owned by / belongs to a specific object either s0 or s1
- Whenever we have something defined directly inside the class (count), then it is owned by the class, not its object 

- Here 'count' is not owned by s0 or s1, we'll not have seperate copies of count in s0 or s1
- There will be only one of "count", which is owned by class "student"
- And it is shared to every object of the class "Student"

'''


Student.count += 1    
Student.count += 1    
print(Student.count)  #2
print(s1.count)       #2 both s1.count and Student.count share the same memory location

s1.count += 1         #3   <--- new instance copy! 
# After s1.count += 1, a new instance attribute is created, pointing to a different memory location, so class variable and instance variable no longer share the same value or memory.

print(Student.count)  #2
print(s1.count)       #3        

