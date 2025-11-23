
# ********** Lec 6 [ MoreOnTuples, Tuple Methods ] 

#? Tuples are immutable
#? Tuples are used for packing and unpacking
#? We can perform slicing 
#? Tuples are iterable

###################
# packing
t = 1, 2, 3
print(t, type(t))   # (1, 2, 3) <class 'tuple'>
#? Computer converted this values as tuples



###################
# unpacking

x, y, z = t
print(x, y, z)

###################

x = 5
y = 10
x, y = y, x    #Here py is actually packing it into a variable in the RHS then unpacking it in the LHS
print(x, y)


###################

t = ([1, 2], ['a', 'b'])
# t[0] = [10, 20]   # error tuple is immutable
t[0][0] = 10        # Not error

#? We cannot modify tuple values, but if a value inside a tuple is a list, then we can modify the values inside that list 
#? In python, this property ika "hashable"
#? If the values inside tuple is also immutable then the tuple is consider as hashable, 
#? whereas if its values are mutable then its non-hashable tuple



# tuples
# methods available: count(), index()