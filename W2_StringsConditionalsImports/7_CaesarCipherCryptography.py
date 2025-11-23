
# ********** Lec 7 [ Cycling up/down 3 letters ]

# This is popularly called the Caesar Cipher in cryptography
alpha="abcdefghijklmnopqrstuvwxyz"


s='rahul'
i=0
t=''

# print(alpha.index(s[0])) # => 17
# print(alpha.index("r"))  # => 17

t = t + (alpha[( (alpha.index(s[i])+1)%26) ]) 
t = t + (alpha[( (alpha.index(s[i+1])+1)%26) ]) 
t = t + (alpha[( (alpha.index(s[i+2])+1)%26) ]) 
t = t + (alpha[( (alpha.index(s[i+3])+1)%26) ]) 
t = t + (alpha[( (alpha.index(s[i+4])+1)%26) ]) 

print(t)

