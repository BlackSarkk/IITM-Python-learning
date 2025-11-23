
# ********** Lec 4 [ Variable - More on Variables, Operators and Expressions ]

#* Variables Naming Convensions

# and = 6   # Error coz Reserved Keyword
# or = 6    # Error coz Reserved Keyword
# if = 6    # Error coz Reserved Keyword
# for = 6   # Error coz Reserved Keyword
# 1_r = 6   # Error coz varable name cant begin with int

# a_ = 3   # valid
#? Variable names are case sensitive



#* Multiple Assignment (have to bit careful while using this)

# x, y = 1, 2        # x = 1, y = 2
# a = b = c = 10     # a = 10, b = 10, c = 10

# x, y = y, x        # swaps the variables



#* Deleting a variable

x = 10
print(x)      # 10
del x
# print(x)    # now it will throw an error



#* ShortHand Operators (Introduced to make our life easier)

count = 0
count += 1
count -= 1
count *= 1
count /= 2



#* "in" Operator

'alpha' in 'A variable name can only contain alpha-numeric characters and underscore'  # True
'alpha' in 'A variable name must start with a letter or the underscore character'      # False

#? The result of "in" operator is always a boolean value



#* Chaining Operators

x = 5

(1 < x < 10)                # T
(10 < x < 20)               # F
(x < 10 < x * 10 < 100)     # T
(10 > x <= 9)               # T
(5 == x > 4)                # T


