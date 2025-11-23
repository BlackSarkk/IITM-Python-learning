
# *********************************
# * ITERATOR
# *********************************

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

# for fruit in fruits:      # It immediately prints the next statement after executing the previous one
#     print(fruit)          # It stops only when the list is exhausted, we donot have the choice when to run the next iteration

# But we want something that doesn't executes immediately and run the next iteration when needed

basket = iter(fruits)   # It converts any iterable entity like list, string, tuple into a list_iterator
# now the basket is an iterator: It gets the job done

print(basket)           # <list_iterator object at 0x74fcfdf7c220>
print(type(basket))     # <class 'list_iterator'>

print(next(basket))     # mango
print(next(basket))     # apple
print(next(basket))     # banana
print(next(basket))     # banana
print(next(basket))     # banana
print(next(basket))     # banana
print(next(basket))     # banana
print(next(basket))     # banana

# * It will give out an error if we call an iterator more times than the number of elements it have

# * readline => reads the line one by one like an iterator wrt number of times we call it
# * readlines => reads all the lines from the file





