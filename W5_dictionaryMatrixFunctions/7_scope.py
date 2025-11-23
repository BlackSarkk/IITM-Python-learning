def myFunction1(x):
    x = x * 2
    print("Value of x in function 1", x)        


def myFunction2(x):
    x = x*3
    print("Value of x in function 2", x)        

def myFunction3():
    global x
    x = x * 2
    print("Value of x in function 3", x)        


x = 5

print("Value of x before function call", x)     # 5  (global)
myFunction1(x)                                  # 10 (local)
myFunction2(x)                                  # 15 (local)
myFunction3()                                   # 10 (global)
print("Value of x after function call", x)      # 10 (global)
    