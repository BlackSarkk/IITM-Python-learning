
# ********** Lec 11 [ Strings: Replication, Comparison, Indexing, Length ]


# * String Replication

# s  = 'good'

# print(s * 3)     # goodgoodgood
# print(s[0] * 3)  # ggg



# * String Comparison

# x='India'
# x == "India"      # True
# x == "india"      # False


# print("apple" > "one")   # (a=97)  > (o=111): false
# print("four" < "ten")    # (f=102) < (t=116): true  
# print("four" < "five")   # (o=111) < (i=105): false
# ? Python starts comparing character by character based on , left to right. 
# ? If characters are equal, it moves to the next one
# ? The moment it finds a difference, it decides < or > based on the ASCII/Unicode value.
# ? If all characters are equal but one string is shorter, the shorter one is considered smaller.


# print("apple" > 1)     # Error      
# print("apple" == 1)    # Error 
# print("apple" < 1)     # Error 




# * String Indexing

# s='python'

# print(s[-6])    # p
# print(s[-5])    # y
# print(s[-4])    # t
# print(s[-3])    # h
# print(s[-2])    # o
# print(s[-1])    # n
# print(s[0])     # p
# print(s[1])     # y
# print(s[2])     # t
# print(s[3])     # h
# print(s[4])     # o
# print(s[5])     # n


# ? len(s) = n; Allowed indices: -n <= i <= n-1
# print(s[-7])  # error as length is 6 we can 
# print(s[6])  # error as length is 6 we can 



# * String Length

s='asdFJPOSDFAOIPJQWERDvsdfv'

print(len(s))
print(s[35])
