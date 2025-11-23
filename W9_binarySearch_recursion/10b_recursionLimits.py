
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)

# print(sum(1000))    # <-- This will exceed the max recursion depth


# Recursion will not always work in python beyond a limit i.e. 999 , but we can change it using import sys and some other commands
# It has been done purposefully, else the python code will keep goin 
# In binary search the limit didnt crossed
