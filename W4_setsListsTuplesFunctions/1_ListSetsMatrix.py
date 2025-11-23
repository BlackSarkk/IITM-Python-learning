
# ********** Lec 1 [ Lists, Sets and Matrices ] 


# l=[1, 2, 3, 4, 5]

# l.append(1024)
# l.append(2)     # Adding 2 again in the list
# print(l)        # List is not a set as in set elements donot repeats, but in lists elements can be repeated
# l.remove(1)     # It will remove 1
# l.remove(2)     # It will remove the first occurance of 2






# y = [1, 2, 3]
# m = [10, 20, 30]
# x = []

# x.append(y)
# x.append(m)
# print(x)    # It is a list within a list
# t = []
# t.append(x)
# print(t)    # list of a list of a list
# t.append([100, 101, 102])

# print(t)    # complex list
# print(t[0]) 
# print(t[1])




####################
#? Naive way representing matrix in python

L = []
L.append(1)
L.append(2)
L.append(3)

M = []
M.append(L)
M.append([4, 5, 6])
M.append([7, 8, 9])

print(M)
print(M[1][0])
print(M[0][2])

#? Printing diagonal:
print(M[0][0])
print(M[1][1])
print(M[2][2])



# List methods:
# append, copy, extend, insert, remove, sort, clear, count, index, pop, reverse