
# ********** Lec 10 [ FUNCTIONS ARGS TYPES ]

#! POSITIONAL ARGUMENTS 

def add(a, b, c):         #<-- These are called the function parameters
    return (a + b - c)

print(add(20, 30, 40))      #<-- function call
# The values passed along with the function calls are called args.

#? In this example this type of args. are called postional args.
#? Where position of each args. is essential wrt the execution of the function def

#? We need to remember what is the actual sequence of the parameter


#! KEYWORD ARGUMENTS 

def add(c, a, b):         
    return (a + b - c)

print(add(a = 20, b = 30, c = 40))      


#? In this example this type of args. are called Keyword args.
#? Where position of each args. is not essential wrt the execution of the function def
#? No need to remember what is the actual sequence of the parameter

#? But still need to remember how many parameters are there in the funciton 


#! DEFAULT ARGUMENTS

def add(c, a = 20, b = 30):         
    return (a + b - c)

print(add(40))          # No error
print(add(40, 10))      # No error
print(add(40, 10, 30))  # No error

#? No need to remember the sequence
#? added default arg if something missing, we'll get the default value
#? Our code will execute even with one or two or three args.



#? Keyword parameters: *
def f(a, b, *, c, d=10):
    return a + b + c + d


#? We can use them in combinitions
print(add(40, b = 10, a = 30))  # No error


# Note: Default parameters cannot come before non-default positional parameters.
# In Python, when defining a function, there’s a rule about the order of parameters:
# 1. Positional parameters (without default values) → must come first.
# 2. Default parameters (with default values) → must come after all positional parameters.
# 3. Keyword-only parameters → come after * if used.
