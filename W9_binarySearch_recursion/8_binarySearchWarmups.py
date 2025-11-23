


# ********** Lec 8 [ BINARY SEARCH Warmup ]


#************************************************** 
#! Check if a given element k is present in a list L or not using loops
#************************************************** 
#************************************************** 


def obvious_search(L, k):
    for x in L:
        if x == k:
            return True
    return False


L = list(range(100000000)) 

import time

a = time.time()
print(obvious_search(L, 99999998))    # go through entire list, so more time
b = time.time()

print(b-a)      # Searching time



#? We'll see an algo faster than obvious sort 