'''
Write a recursive function named non_decreasing that accepts a non-empty list L of integers as argument and returns True if the elements are sorted in non-decreasing order from left to right, and False otherwise.
You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
'''

def non_decreasing(L):
    if(len(L) <= 1):
        return True
    elif L[0] > L[1]:
        return False
    else:
        return non_decreasing(L[1:])
    


print(non_decreasing([2, 3, 4, 5, 1, 7]))