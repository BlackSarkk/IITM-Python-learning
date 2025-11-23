

# ********** Lec 5 [ Find 0 in list using recursion ]


#************************************************** 
#! returns 1 if zero is present else returns false (CODE)
#************************************************** 
#************************************************** 


L = [11, 12, 16, 2, 3, 4, 0, 5, 6]
M = [11, 12, 16, 2, 3, 4, 5, 6]


#? Using recursion - check the first element and outsourse the rest of the list

def find0(L):
    if (len(L) == 0):
        return False
    
    if (L[0]==0):
        return True
    else:
        return find0(L[1:len(L)])       # This code simply outsources

print(find0(L))
print(find0(M))


#? This is an extremely inefficient code, we'll see better code later

