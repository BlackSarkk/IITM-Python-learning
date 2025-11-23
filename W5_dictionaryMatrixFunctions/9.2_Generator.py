

# *********************************
# * GENERATOR (creating custom iterator)
# *********************************

def square(limit):
    x = 0
    while x < limit:        
        yield x * x         # Whenever we create a generator we donot have any return statement, we have yield statement
        yield x * x * x
        x += 1

a = square(5)

print(next(a), next(a))     # 0, 0
print(next(a), next(a))     # 1, 1  
print(next(a), next(a))     # 4, 8

# *We can run next(a) until x is less than than limit i.e. in this case is 5
#  