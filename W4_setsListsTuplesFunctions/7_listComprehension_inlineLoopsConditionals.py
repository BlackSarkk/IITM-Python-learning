

# ********** Lec 7 [ Functional Programming ] 

########## Inline statements

#* IF ELSE inline
a = 10
b = 20

'''
if a < b:
    small = a
else: 
    small = b
'''
small = a if a < b else b    

# both takes same time and equally optimised
# Only adv is to reduce some lines
# inlines are good for small codes
print(small)


###############################
###############################


#* WHILE Loop inline

a = 5

'''
while a > 0:
    print(a)
    a -= 1
'''
while a > 0: print(a); a -= 1

# both takes same time and equally optimised
# Only adv is to reduce some lines
# inlines are good for small codes


###############################
###############################


# List COMPREHENSION

#* FOR Loop inline

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

'''
newList = []

for fruit in fruits:
    if 'n' in fruit:    # only include fruits that contain the letter 'n'
        newList.append(fruit.capitalize())
'''

newList = [fruit.capatilize() for fruit in fruits if 'n' in fruit]

# L = [1 if i % 2 == 0 else 0 for i in range(n)]  this is valid

# both takes same time and equally optimised
# Only adv is to reduce some lines
# inlines are good for small codes


print(newList)













