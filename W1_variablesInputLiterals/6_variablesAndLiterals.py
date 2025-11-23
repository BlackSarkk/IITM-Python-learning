
# ********** Lec 5 [ Variables and Literals ]


# * Merging Print and Input statements:

# name=str(input("Hello, type your name: "))
# place=str(input(f"Which place are you in? "))
# weather=str(input(f"Hello {name}, How is the weather in {place}? "))
# age=int(input(f"What is your age? "))
# print(f"Good to know you are {age} years old.")


# ? Literals: The thing which is getting stored in variables
# ?           here variables are: name, place, age. Literals are: rahul, india, 21

# ?           Variables can store different literal values and they cab be modifies as per the requirement
# ?           Literals can only be used on the RHS of the equation
# ?           Whereas Variables can be used on either side of the equation   


# age = 40       # OK
# age = age + 1  # Ok

# 40 = 40 + 1    # Error



# * Area of the circle:

r = int(input("Enter the radius of the circle: "))
area = 3.14 * r * r
print(f"Area of the circle with radius {r} is {area}.")
