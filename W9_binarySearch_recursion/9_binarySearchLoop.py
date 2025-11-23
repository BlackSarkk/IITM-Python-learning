
# ********** Lec 9 [ BINARY SEARCH ACTUAL CODE ]


#************************************************** 
#! Binary Search using loop
#************************************************** 
#************************************************** 

'''
This function is an alternative for obvious search. 
It does eaxactly what is expected from the obvious_search, but in an efficient way. 
This method is popularly called the binary search 
'''

# obvious_search works on any list
# but binary_search will only work on sorted list 
# searching a dict is easy only if it is sorted, otherwise its gonna be impossible


# assuming list L is sorted
def binary_search(L, k):

#? Shrinking our list using while loop
    begin=0       # first element in L, L[0]
    end=len(L)-1  # the last element in L is in len(L). L[len(L)-1]

    while((end-begin)>1):       # It has atleast two elements

        mid=(begin+end)//2      # Calling left one as the middle one when we have even number of elements

        #“You should avoid using else because it will capture all remaining cases. If you haven’t thought through every possible case the else block might run unexpectedly and cause bugs.”
        
        if (L[mid]==k):
            return True           # [            (k)            ]
        
        if (L[mid]>k):
            end=mid-1          # [{begin   k   end}(mid)     ]

        if (L[mid]<k):          
            begin=mid+1        # [     (mid){begin   k   end}]


        # This is outside the while loop. 
        # If we are here, it means that we haven't found the element.
        # If we are here, it meanas that while condition is violated.
        # Which means end-begin is less than or equal to 1


    # If it is equals 1: There is exactly two elements
    if (L[begin]==k) or (L[end]==k):
        return True
    
    else:
        return False
        








print(binary_search(range(999999999999999999), 999999999999999995))      # Fast as fuck