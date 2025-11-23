

# *************************
# * ZIP:
# *************************

# To couple values from two different lists

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
size = [5, 5, 6, 6, 9, 10, 5, 4]



# note: zip returns an iterable zip object so need to convert it into desired dataStruct before printing

print(list(zip(fruits, size)))
print(dict(zip(fruits, size)))




