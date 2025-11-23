
# ********** Lec 5 [ MoreOnSets, Sets Methods ] 

st = {1, 2, 3, 2, 4, 5, 6, 7, 8, 9}  # => {1, 2, 3, 4, 5, 6, 7, 8, 9}

#? Set doesnot allow duplicate values
#? Set is unordered => we cannot say the element 1 is the 0th index

#? Set is mutable, but the values of the set has to be immutable and hashable...
#? that means we cannot add a list, dictonary etc to a set
#? We can iterate over the set


################################
#! Set Methods
#? add, clear, copy, discard, pop, remove, union, intersection, difference

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}

# * issubset: child
A.issubset(B)   # ✅ True — A is child of B (all elements of A are in B)
B.issubset(A)   # ❌ False — B is not child of A (B has extra elements)

# * issuperset: parent
B.issuperset(A)   # ✅ True — B is parent of A (B contains all elements of A)
A.issuperset(B)   # ❌ False — A is not parent of B (A misses some elements)

# * note: if both A and B have the same elements
#   issubset  → True ✅
#   issuperset → True ✅

# * note: if A and B share only some elements (partial overlap)
#   issubset  → False ❌
#   issuperset → False ❌

################################



A = {1, 2, 3}
B = {3, 4, 5}

A.union(B)   # {1, 2, 3, 4, 5}
A | B        # {1, 2, 3, 4, 5}

A.intersection(B)   # {3}
A & B               # {3}

A.difference(B)   # {1, 2}      Elements in A that are not in B (A \ B)
A - B             # {1, 2}

