
# ********** Lec 10 [ Operators II ]

# ? In python we have three major types of operators : Arithmatic Op, Relational Op, Logical Op 




# * Arithmatic Op: [ +, -, *. /, //, %, ** ]

# print(f'Addition {2 + 3}')
# print(f'Subtraction {2 - 3}')
# print(f'Multiplication {2 * 3}')
# print(f'Division {2 / 3}')      

# print(f'FloorDivision {7 // 3}')    # Divide and floor it
# print(f"Modulus {3 % 2}")           # Remainder
# print(f"Exponential {2 ** 3}")      # 2^3




#  * Relational Op: [ >, <, >=, <=, ==, != ]

# ? This always has output in boolean (True or False)

# print(f"> : {5 > 10}")
# print(f"< : {5 < 10}")
# print(f">= : {5 >= 5}")
# print(f"<= : {5 <= 5}")
# print(f"== : {5 == 5}")
# print(f"!= : {5 != 5}")




# * Logical Op: [ and, or, not ]

# ? and: both should be true: true, else false
# print(True and True)    # True
# print(True and False)   # True
# print(False and True)   # False
# print(False and False)  # False


# ? or: atlease one should be true: true, else false
# print(True or True)    # True
# print(True or False)   # True
# print(False or True)   # True
# print(False or False)  # False


# ? not: invert the value
print( not (True))   # False 
print( not False)    # True
# ? This can be used with () or without ()






# * Operators Precedence: (Highest to lowest)

# Parentheses:               (...) (grouping)
# Exponentiation:            **
# Unary Operators:           +x, -x, ~x
# Mul/Div/FloorDiv/Modulus:  *, /, //, %
# Addition and Subtraction:  +, -
# Bitwise Shifts:            <<, >>
# Bitwise AND:               &
# Bitwise XOR:               ^
# Bitwise OR:                |
# Comparisons:               <, <=, >, >=, ==, !=, is, is not, in, not in 
# Logical NOT:               not
# Logical and:               and
# Logical or:                or
# Conditional Expression:    x if condition else y
# Assignment Expressions:    =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=, :=
# Comma (Tuple, Argument, etc.)