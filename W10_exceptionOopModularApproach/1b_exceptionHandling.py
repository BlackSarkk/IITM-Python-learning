


#************************************************** 
#! Exception Handled Code
#************************************************** 
#************************************************** 

try:
    f = open('abc.txt', 'r')        # lets say the file does exist
                                    # always a good practise to close an opened file
    a = int(input())
    b = int(input())
    c = a / b       # If an exception error occurs here the below code wont execute and the file will remains open
    print(c)

    #f.close()    # better to put it in finally block       

except ZeroDivisionError:
    print('Invalid Input, divisior cannot be zero')

except NameError:
    print('Variable not defined')

except FileNotFoundError:
    print("Invalid file name, please check again")

else:
    print('Invalid code')

finally:
    print("Execution of try-except-else-finally block completed.")
    f.close()       # <-- special block which runs irrespective of whether we get exception or the code works completely


