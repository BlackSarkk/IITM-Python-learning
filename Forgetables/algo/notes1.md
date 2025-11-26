
1. Rotation of letters to right:

2. up each letters by 2:

# Pattern Printing:

1. \   /
    \ /
     x
    / \
   /   \

# binary Search:
def binary_search(n, x, first, last):
    if first > last:
        return False
    
    mid = (first + last) // 2

    if n[mid] == x: 
        return True
    elif n[mid] > x:
        return binary_search(n, x, first, mid - 1)
    else:  # n[mid] < x
        return binary_search(n, x, mid + 1, last)
