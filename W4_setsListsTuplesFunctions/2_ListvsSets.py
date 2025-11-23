
# ********** Lec 2 [ Lists, Sets ] 

l = list(range(10))
l.append('Sudharshan')
l.append('India')
l.append(2.71)



#! "in" keyword

print(l)
print(5 in l)              # True
print("sudharshan" in l)   # False (case sensitive)
print(2.710 in l)          # True (2.71 == 2.710)



#############################

l = list(range(100000000000))

print(0 in l)       
print(l(9990000)) 
print(l(len(l)-1))  # It goes through every entries of l


#############################

#? SETS

x={1,2,3,4,5,6,2}
type(x)          # Sets    
print(x)         # Sets doesnot have repeated elementes so it removes upcoming repeating elements




#############################

l= list(range(1000000000))
s= set(range(1000000000))      # This will take more time then creation of list

-1 in s    # it is going through all entries and hence will take lots of time
-1 in l    # quick

# List → Fast creation, slow search
# Set → Slow creation, fast search
 
 
 
#############################

import sys

l=[]
l1=[0]
l2=[0,1]

sys.getsizeof(l)
sys.getsizeof(l1)
sys.getsizeof(l2)




#############################

x = list(range(100))
s = set(range(100))

sys.getsizeof(x)    # 856 
sys.getsizeof(s)    # 8408 

# thats why in s is slow creation, x is fast creation

x[21]  
30 in s   
# s[30]       # this will give an error

# note:  sets can only tell us if the element is present or not, it cant tell what is the first or second element
#        coz it dosent have anything like first element or second element

# set uses optimised dsa to search, thats why large size and fast search  

##############################
#? Using Sets

z={'amit', 'neeru', 'anamika', 'varsha', 'nitin'}

'anamika' in z
'amar' in z
'nitin' in z

z.add('karthik')

'karthik' in z