
# ********** Lec 6 [ String Methods ]

#? Notes:
# There are 6 types of in-built string methods in Python, they are:
# 1. lower(), upper(), capitalize(), title(), swapcase()
# 2. islower(), isupper(), istitle()
# 3. isdigit(), isalpha(), isalnum()
# 4. strip(), lstrip(), rstrip()
# 5. startswith(), endswith()
# 6. count(), index(), replace()


a = "rahul"

upper=a.upper()     # Uppercase
lower=a.lower()     # Lowercase
capital=a.capitalize()   # Capitalize
swap=a.swapcase()   # Swap the current case


isLower=a.islower()  # lower=true
isUpper=a.isupper()  # upper=true
isTitle=a.istitle()  # true: All words start with uppercase, rest in lower case, numbers symbols are ignored. ex: Hello World, Hello@123 (here hello must be in title case)
                     # false: not in title case, or empty string. ex: hello world, HELLO WORLD, "", 123Hello

isDigit=a.isdigit()  # Numeric = true
isAlpha=a.isalpha()  # Alphabet = true          ("Rahul Dutta") => space => false
isAlNum=a.isalnum()  # AlphaNumeric = true
                     # @9gju29l9u&# = false


Strip=a.strip('-')  # Returns a trimmed version of the string
                    # x='---Python----' => Python
LStrip=a.lstrip('-')  # Returns a Left trim version of the string
                    # x='---Python----' => Python----
RStrip=a.rstrip('-')  # Returns a Right trim version of the string
                    # x='---Python----' => ---Python


# These method are case sensitive
StartWith=a.startswith('r')  # Returns true if the string starts with the specified value
EndsWith=a.endswith('r')     # Returns true if the string ends with the specified value


# These method are case sensitive
Count=a.count('a')  # Returns the number of times a specific value occur in a string
Index=a.index('h')  # Searches the string for a specific value and reurns the position of where it was found first from L to R
replace=a.replace('r', 'R')  # Returns a string where a specic value is replaced with a specific value


#? More methods:
# .swapcase()
# .join()


text = ['P', 'Y', 'T', 'H', 'O', 'N']
dotted = ".".join(text)     # Output: "P.Y.T.H.O.N"



    
#* Split: breaks a string into parts and returns a list   
text = "apple banana mango"
print(text.split())            # ['apple', 'banana', 'mango']

csv_line = "red,green,blue"
print(csv_line.split(','))     # ['red', 'green', 'blue']

text = "one two three"
print(text.split(' ', 1))      # ['one', 'two three']