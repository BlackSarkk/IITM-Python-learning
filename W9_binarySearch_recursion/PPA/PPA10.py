'''
Write a recursive function named search that accepts the following arguments:
(1) L: a sorted list of integers
(2) k: integer

The function should return True if k is found in the list L, and False otherwise.

You do not have to accept input from the user or print output to the console. You just have to write the function definition.

'''


def search(L, k):

    if len(L) == 0:
        return False

    mid = len(L)//2

    if L[mid]==k:
        return True
    elif L[mid] > k:
        return search(L[:mid], k)
    elif L[mid] < k:
        return search(L[mid+1:], k)


print(search([1, 2, 3, 4, 5, 6, 7], 5))