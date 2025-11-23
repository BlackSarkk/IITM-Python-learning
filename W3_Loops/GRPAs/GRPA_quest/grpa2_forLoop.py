# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>


if task == 'factorial':
    n = int(input())
    result = 1
    i = 1
    while i <=n:
        result*=i
        i+=1

    print(result)
elif task == 'even_numbers':
    n = ...
    while i< n+1:
        print(i)
        i+=2

elif task == 'power_sequence':
    n = ...
    result = 1
    while i<n:
        print(result)
        result*=2
        i+=1

elif task == 'sum_not_divisible':
    ...

elif task == 'from_k':
    ...

elif task == 'string_iter':
    ...

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input

else:
    print("Invalid")    