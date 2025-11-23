
# ********** Lec 10 [ BINARY SEARCH ACTUAL CODE ]


#************************************************** 
#! Binary Search using recursion
#************************************************** 
#************************************************** 



def rBinarySearch(L, k, begin, end):

# if begin and end are same, then we need to check L[begin]
    if (begin==end):
        if(L[begin] ==k):
            return 1
        else:
            return 0

# if begin and end are consecutive, then check them individually
    if (end-begin==1):
        if (L[begin] == k) or ( L[end]==k ):
            return 1
        else:
            return 0

# if end - begin > 1
    if (end-begin > 1):
        mid = (end+begin)//2

        if (L[mid]==k):       
            return 1

        if (L[mid]>k):  
            end = mid -1       # discard the right and retain the left
        
        if (L[mid]<k):  
            begin = mid + 1    # discard the left and retain the right


    if (end - begin) < 0:
        return 0 
        
    return rBinarySearch(L, k, begin, end)



print(rBinarySearch(range(999999999999999999), 999999999999999998, 0, 999999999999999999))      # Fast as fuck