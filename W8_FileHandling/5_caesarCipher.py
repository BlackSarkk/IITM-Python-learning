

# ********** Lec 5 [ CAESAR_CIPHER_IN_A_FILE ]


#************************************************** 
#! Shifting everything by three letters
#************************************************** 
#************************************************** 


import string

def create_caesar_dict(shift=3):
    l = string.ascii_lowercase
    d = {}
    for i, ch in enumerate(l):
        d[ch] = l[(i + shift) % 26]
    return d

f = open("5_rough.txt", "r")
g = open("5_rough_encrypted.txt", "w")


d = create_caesar_dict()

c = f.read(1)                    # read one letter at a time
while c != '':
    if c.lower() in d:           # handle lowercase only
        if c.islower():
            g.write(d[c])
        else:
            # convert uppercase properly
            g.write(d[c.lower()].upper())
    else:
        g.write(c)
    c = f.read(1)

f.close()
g.close()
