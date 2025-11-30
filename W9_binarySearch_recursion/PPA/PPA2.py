
# The factorial of a positive integer n is defined as follows:
# n!=1x2x3⋯n
# Write a recursive function named factorial that accepts a positive integer n as argument and returns the factorial of n.
# You do not have to accept input from the user or print the output to the console. You just have to write the function definition.


def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(1))