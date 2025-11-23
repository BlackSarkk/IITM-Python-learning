
# ********** Lec 4 [ MoreOnLists, List Methods ] 


l1 = [1, 2, 3]
l2 = [10, 20, 30]
l12= l1 + l2       # concatincate two list
l21= l2 + l1

print(l12, l21)

###########################

l1= [0, 0, 0, 0, 0, 0]
l2 = [0] * 6

# both l1 and l2 are same

###########################

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, 3, 2]

print(l1==l2)     #T
print(l2==l3)     #F
print(l2<l3)      #T    compares the corresponding elements of both the list
print([] < [1])   #T

##########################
#* Mutability

l = [1, 2, 3]
l[2] = 3

s ="abcd"        
# s[3] = "d"    #error coz strings are immutable

#########################

x = 5
y = x

l1 = [1, 2, 3]
l2 = l1
l1[0] = 100
print(l1, l2)   

# l1 and l2 both are pointing to same memory location
# To create a new memory location instead :

l1 = [1, 2, 3]

#* Three methods to create completely new memory location out of the old one
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()

l1[0] = 100
print(l1, l2, l3, l4)

###########################

#* Figuring out whether two different variable is pointing to same memory location or different memeory location


l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1

print(l1 is l2)     # False : for different memory location
print(l1 is l3)     # True  : for same memory location

###########################
#* Weird Behaviour

def add(x):
    x = x + 1
    return x

x = 5
print(add(x))
print(x)    
#? Both the print statement is givin different outputs coz x which is a variable is immutable

###########################
#* Passing list as an arg to a function

def add(x):
    x.append(1)
    return x

x = [5]         
print(add(x))
print(x)

#? Both the print statement is givin different outputs coz list is mutable
#? If function argument is of mutable type then it is call by reference otherwise it is call by value
#? Thats why in case of list it is call by reference and in case of int it is call by value

# Immutable (int, str, tuple) → new object created → outer variable unchanged.  (orignal object change ni hota h )
# Mutable (list, dict, set) → same object modified → change visible everywhere. (orignal object change ho jaata hai)


###########################

#! List Methods
#? append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

l = [1, 2, 3]
l.append(4)
l.insert(2, 9)


#? Note : 
# Append adds the elements at the end of the list 
# Insert adds the elements at the specified index. (index, value)

l.remove(2) # It will remove the first occurance of 2
l.pop(0)    # It will remove the element at index 0


l = [2, 6, 1, 50, 3, 7, 5]
l.sort()    # It will sort the list in ascending order              # This modifies the orignal list
l.sort(reverse=True)    # It will sort the list in descending order

l.reverse() # It will reverse the list


# use sorted()
m = sorted(l, reverse=True)  # creates new list, orignal list untouched 
