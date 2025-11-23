
# ********** Lec 3 [ Classes, Objects and Attributes ]


#************************************************** 
#! Classes
#************************************************** 
#************************************************** 

#? Creating a class
class Student:      # It is an standard practice to start classname with uppercase
    roll_no = None  # here 'None' is the default value initialised inside the class
    name = None




#************************************************** 
#! Objects
#************************************************** 
#************************************************** 

#? Creating an object out of class
s0 = Student()  # <-- This Student() looks like a function
# Student() is a special type of function only coz this function name looks identical to the name of class
# Whenever we create a class with its specific name, python on its own add one function inside it
# And the name of that funciton is always same to the name given to the Class
# And in programming terms, this special function ika Constructor because we use class to construct objects

# s0 is an object of class 'Student'
# s0 is an instance of 'Student'




#************************************************** 
#! Attributes
#************************************************** 
#************************************************** 

#? giving attributes to the object created
s0.roll_no = 0          # <-- This '.' ika dot operator in python language
s0.name = 'Rahul'       # <-- Whenever we want to acess an entity which belongs to an object, we use dot operator in python 
print(s0.roll_no, s0.name)  # <-- objectName dotOperator variableName ==> object.variable
# This is how we access attributes and behaviour of an specific object






##!! Even thought this is working fine, this is not the ideal way for writing objects and classes
##!! remaining bit is the behaviour, we'll see that in upcoming lect