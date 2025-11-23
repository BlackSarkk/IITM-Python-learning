
# ********** Lec 3 [ Tuples ] 



############################
# lists
# methods available: append, copy, extend, insert, remove, sort, clear, count, index, pop, reverse

l=[5, 7, 8, 9]
l.append(100)
l.remove(7)

############################
# sets
# methods available: add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset issuperset, pop, remove, symmetric_difference, symmetric_difference_update, union, update                  
                      
s={1, 7, 9}
s.add(2)
s.remove(2)

############################
# tuples
# methods available: count(), index()

t=(1,2,4,5,6)
# t.append(111)   #? error
# t.remove(2)     #? error

#? A tuple is unchangeable whereis a list can be changed

############################
# difference btw list and tuple

l=list(range(10))
t=tuple(range(10))

#? A tuple is immutable where a list is mutable
#? Sometimes we may not want things to change, there we use tuple

###########################

import string

alpha=string.ascii_uppercase
alpha=string.ascii_letters

alpha=set(alpha)        #? creating a tuple from existing set

s=string.ascii_letters
tup=tuple(list(s))      #? creating a tuple from existing list

###########################

x='sudarshan#%^&*$IndiaBharath()Karnataka$PunjabTamil Nadu'

l=list(x)  #? creating a list from existing string

# We gonna get all the valid alphabets

r=[]
for p in l:
    if p in alpha:
        r.append(p)

print(r)   # Seperated out alphabets from untidy long string



############################
#? tuple takes up less memory space than list 

l = list(range(10))
t = tuple(range(10))

l.__sizeof__()      # 120
t.__sizeof__()      # 104

############################

#? When we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple 
#? ex: security keys, jwt tokens, or api keys


