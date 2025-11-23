

# ********** Lec 4 [ Find 0 in list using recursion ]


#************************************************** 
#! returns 1 if zero is present else returns false (LOGIC)
#************************************************** 
#************************************************** 


L = [11, 12, 16, 2, 3, 4, 0, 5, 6]


'''

#? Using Loops
def check0(m):   
    return any([x == 0 for x in m])

'''



#? Using recursion - check the first element and outsourse the rest of the list