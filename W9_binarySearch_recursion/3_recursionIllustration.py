

# ********** Lec 3 [ RECURSION_Illustration ]


#************************************************** 
#! Sum of n numbers:
#************************************************** 
#************************************************** 

n = 10

#? Method 1: loop

# ans=0
# for i in range(n):
#     ans=ans+(i+1)
# print(ans)


#? Method 2: function

# def sum(n):
#     ans=0
#     for i in range(n):
#         ans = ans + (i+1)
#     return ans


#? Method 3: recursion
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)



#************************************************** 
#! Compound Interest: compute CI by assume the Interest to be 10%
#************************************************** 
#************************************************** 

def comp(principal, year):
    if(year==1):
        return principal * (1.1)
    else: 
        return comp(principal, year-1) * 1.1

print(comp(2000,3))




#************************************************** 
#! Factorial
#************************************************** 
#************************************************** 

def fact(n):
    if(n==1):
        return 1
    else:
        return (fact(n-1))*n





