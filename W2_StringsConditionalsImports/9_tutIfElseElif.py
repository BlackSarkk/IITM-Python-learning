

# ********** Lec 9 [ Tut ]

#? Find whether the given number is even or odd

# print("Check if the number is even or odd")
# num = int(input("Enter a number: "))

# if(num%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")
    
    
    
#? Find whether the given number ends with 0 or 5 or any other

# print("Check if the number ending with 0 or 5 or other")
# num = int(input("Enter a number: "))

# if(num%5!=0):
#     print("Other")
# elif(num%5==0 and (num/5)%2!=0):
#     print("5")
# else:
#     print("0")
    
# Note: we can try dividing with 10 and 5 instead  



#? Find the grade of the student based on the given marks from 0 to 100

# A  - Marks >= 90
# B  - >=80 and >= 90
# C  - >=70 and >= 80
# D  - >=60 and >= 70
# E  - Marks < 60

# print("Check your grade")
# num = int(input("Enter your grade: "))

# if(100>=num>=90):
#     print("A")
# elif(90>num>=80):
#     print("B")
# elif(80>num>=70):
#     print("C")
# elif(70>num>=60):
#     print("D")
# elif(60>num>=0):
#     print("E")
# else:
#     print("Invalid Input")
    
    

#? Convert the given flowchart into a python code

print('Start')
print('Travel from City A to City B')

time = input('enter time as either shorter or longer\t')
time.lower()
if(time == 'shorter'):
  price = input('enter price as either lower or higher\t')
  price.lower()
  if(price == 'lower'):
    print('Red Eye Flight')
    print('Reached City B')
    print('Stop')
  elif(price == 'higher'):
    print('Daytime Flight')
    print('Reached City B')
    print('Stop')
  else:
    print('invalid price input')
elif(time == 'longer'):
  price = input('enter price as either lower or higher\t')
  price.lower()
  if(price == 'lower'):
    print('Coach')
    print('Reached City B')
    print('Stop')
  elif(price == 'higher'):
    print('Train')
    print('Reached City B')
    print('Stop')
else:
    print('invalid price input')

