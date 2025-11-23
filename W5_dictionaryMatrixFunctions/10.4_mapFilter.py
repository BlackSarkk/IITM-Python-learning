

# *************************
# * MAP:
# *************************


a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]

# c = a - b         # ERROR
# c = a[0] - b[0]   # prints single value
# so we have to write a loop to print each char  

# To achieve so we gonna use map


#****** EXAMPLE 1

def sub(x, y):
    return x - y

c = map(sub, a, b)
print(list(c))




#****** EXAMPLE 2

def inc(x):
    return x + 1 

d = map(inc, a)
print(list(d))




#****** EXAMPLE 3

import math

m = [25, -16, 9, 81, -100]


def square_root(n):
    return math.sqrt(n)


def is_positive(n):
    if n >= 0:
        return n

n = map(square_root, filter(is_positive, a))
print(list(n))
