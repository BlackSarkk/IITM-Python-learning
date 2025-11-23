
# ********** Lec 4 [ Tut: Factorial, DigitsLength, DigitsReverse, DigitsPalindrome ]



#? Factorial

# print("Enter a number")
# n=int(input())
# x=n

# answer=1

# if(n>=0):
#     while(x>0):
#         answer*=x
#         x -= 1
#     print(f"The factorial of {n} is {answer}")    
# else:
#     print("Not defined!")
    


#? Find number of digits in the given number


# num=abs(int(input("Enter a number: ")))
# digits = 1
# while(num>9):
#     num = num // 10
#     digits += 1
# print(digits)

# or
 
# print(len(str(abs(int(input("Enter a number "))))))



#? Reverse the digits in the given number

# ! my approach

inp=int(input("Enter a number: "))
newStr=""

sign=int(inp*(1/abs(inp)))  # sign preserved
newinp=str(abs(inp))        # absolute value in str

length=len(str(abs(inp)))   # length

while(length>0):
    newStr = newStr + newinp[length-1] 
    length -= 1

print(f"{sign*int(newStr)}")


#! IITM approach
# we can use % 10 to get the last digit.. 

# ! cgpt shorter approach

# inp = int(input("Enter a number: "))
# sign = -1 if inp < 0 else 1
# print(f"{sign}{str(abs(inp))[::-1]}")



#? Find whether the entered number is palindrome or not
