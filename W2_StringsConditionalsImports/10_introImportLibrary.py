

# ********** Lec 9 [ import math, random ]


#? for math
import math

print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(10, 3))
print(math.log(10))



#? for random
import random
print(random.random())  # random numbers btw 1 and 0




#? Simulate coin toss:

a=random.random()           # Generates random float btw 0 and 1  :  range = 0.0 ≤ x < 1.0

if(a<0.5):
    print("Heads")
else:
    print("Tali")
    


#? Simulate the sum of two 6 faces dice:

dice1=(random.randint(1,7))     # Generates random int btw given numbers : range =  1, 2, 3, 4, 5, 6, 7
dice2=(random.randint(1,7))
total=(dice1+dice2)

print(f"Your pair of dice is: {total}")

    
