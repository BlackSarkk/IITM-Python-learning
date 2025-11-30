
'''
Write a recursive function named palindrome that accepts a string word as argument and returns True if it is a palindrome and False otherwise.
You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
'''

def palindrome(string):

    if len(string) <= 1:
        return True
    
    elif string[0] == string[-1]:
        return palindrome(string[1:-1]) 
    else:
        return False 
    
print(palindrome("wowa"))


# NOTE: Here order or validations matter