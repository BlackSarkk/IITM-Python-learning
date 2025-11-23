
# ********** Lec 3 [ Factorial using While loop ]

print("Enter a number")
n=int(input())
x=n

answer=1

if(n>=0):
    while(x>0):
        answer*=x
        x -= 1
    print(f"The factorial of {n} is {answer}")    
else:
    print("Not defined!")
