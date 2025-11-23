# Q. Write a python code using functions which calculates the number of 
# 1. uppercase letters, 
# 2. lowercase letters,
# 3. total number of characters, 
# 4. number of words

sentence = input('Enter the sentence: ')

#* *********************
#* UPPERCASE LETTERS:
#* *********************
 
def upper(s):
    upper = 0
    for c in s:
        if(c.isupper()):
            upper += 1
    return upper

uLetters = upper(sentence)
print(f"\nTotal number of upperCase characters: {uLetters}")
 

#* *********************
#* LOWERCASE LETTERS:
#* *********************
 
def lower(s):
    lower = 0
    for c in s:
        if(c.islower()):
            lower += 1
    return lower

lLetters = lower(sentence)
print(f"\nTotal number of lowerCase characters: {lLetters}")
 

#* *********************
#* TOTAL NUMBER OF CHAR:
#* *********************
 
def total(s):
    total = 0
    for c in s:
            total += 1
    return total

tLetters = total(sentence)
print(f"\nTotal number of characters: {tLetters}")
 

 

#* *********************
#* TOTAL NUMBER OF WORDS:
#* *********************
 
def word(s):
    words = 1   # any valid sentence will have atleast 1 word
    for c in s:
        if(c == " "):
            words += 1
    return words

wLetters = word(sentence)
print(f"\nTotal number of words: {wLetters}")
 




