

# *************************
# * ENUMERATE:
# *************************

# TO Couple values with their index number of a list

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]


# for i in range(len(fruits)):     # INDEX IT WHILE PRINTING
#     print(i, fruits[i])     


for fruit in enumerate(fruits):  # Now it will bind the index number with the elements
    print(fruit)            




for fruit in enumerate(fruits, start=5):  # We can change the index number of start
    print(fruit)            


# for i, j in enumerate(items, start=1):  # To pick out the index as well as value


