
# ********** Lec 1 [ Exception Handling ]


#************************************************** 
#! Normal situation
#************************************************** 
#************************************************** 


a = int(input())
b = int(input())
c = a / b
print(c)

#? Error1
# if b is 0                     ==>  error coz division by 0 isnt valid mathematically        ==> exception

#? Error2
# print(d)                      ==>  error coz d has not been defined                         ==> exception

#? Error3
# f = open('abc.txt', 'r')      ==>  error coz the file doesn't extist                        ==> exception




#************************************************** 
#! Exception Handled Code
#************************************************** 
#************************************************** 

try:
    a = int(input())
    b = int(input())
    c = a / b       
    print(c)


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

# In online forms, when we forget to fill a required field, the validation messages inform us about the missing information.
# These messages are meant to help the user understand what they missed or what they need to correct.
# Coz a normal user might not understand the computer generated error



