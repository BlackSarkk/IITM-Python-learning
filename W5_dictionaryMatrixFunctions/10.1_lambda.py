
# *************************
# * LAMBDA FUNCTIONS:
# *************************

# It is a type of function which is anonymous
# which means without providing any function name we can a function in python
# ADV: it reduces the length of the program
# Use this instead where there is very few number of line inside a function

def add(x, y):
    return x + y

sub = lambda x, y: x - y    # LAMBDA

print(add(10, 20))
print(sub(10, 20))  # LAMBDA FUNCTION CALL

print(type(sub))    # Function



