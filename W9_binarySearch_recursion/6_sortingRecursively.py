

# ********** Lec 6 [ SORTING RECURSIVELY ]


#************************************************** 
#! SORTING A LIST
#************************************************** 
#************************************************** 

# FIND MINIMUM
def mini(L):
    mini = L[0]

    for x in L:
        if x<mini:
            mini = x
    return mini


# Recursively sort the list L
def Sort(L):
    if (L == []) or (len(L) == 1):
        return L

    m=mini(L)
    L.remove(m)
    return [m]+Sort(L)


print(Sort([12, 94, 20, 44, 39 ]))




