'''
Write a recursive function named count that accepts the following arguments:

L: list of words
word: a word, could be any string
This function should return the number of occurrences of word in L.

(1) You cannot use the built-in count method for lists in this problem.

(2) All words will be in lower case.

(3) You do not have to accept input from the user or print the output to the console. You just have to write the definition of both the functions.

'''


def count(L, word):

    if (len(L)==1):
        if L[0] == word:
            return 1
        else:
            return 0
    
    elif (L[0] != word):
        return count(L[1:], word)
    
    else:
        return 1 + count(L[1:], word)
    

print(count(["do", "re", "si", 'mi', "fa", "si"], "si"))