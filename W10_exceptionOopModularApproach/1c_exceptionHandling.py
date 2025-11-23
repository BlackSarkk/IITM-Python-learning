


#************************************************** 
#! User defined exceptions - -  Custom exception handling
#************************************************** 
#************************************************** 

a = int(input())
if a < 18:
    raise Exception('You are underage, can not vote')
    # This is not the computer giving exception message, it is us, the user that giving out the exception message



#************************************************** 
#! Writing exceptions in the finally block
#************************************************** 
#************************************************** 

'''
try:
    1 / 0
except ZeroDivisionError:
    print("division by 0")
finally:
    try:
        raise ValueError("error in finally")
    except ValueError:
        print("handled in finally")
'''       


# This will run endlessly