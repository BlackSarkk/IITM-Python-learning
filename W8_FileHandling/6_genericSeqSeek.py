
# ********** Lec 6 [ GENERIC_SEQUENCE ]


#************************************************** 
#! SEEK 
#************************************************** 
#************************************************** 



f = open("6_rough.txt", "r")

s=f.read(2)     # It will read two characters
s=f.read(3)     # It will the next three characters after reading first two characters


s=f.seek(4)     # this will move the cursor to the 4th index i.e. 5th position (rewinding back while reading)
#? SEEK: Seek moves linearly, doesnot appears there magically, so seek can be costly sometimes



f.close()



#************************************************** 
#! reading HUMAN DNA SEQUENCE
#************************************************** 
#************************************************** 

f = open("6_rough2.txt", "r")
seq = f.read()      #NOTE: read the entire remaining file as one string


# lets say the diabetic gene is: 'CCACAACTACTACTAAAGGATCATACC'
diab = "CCACAACTACTACTAAAGGATCATACC"
print(diab in seq)         # TRUE


# lets say the High BP gene is: "ATAATCCTTTGCTTCTCC"
bp = "ATAATCCTTTGCTTCTCC"
print(bp in seq)           # FALSE




# if the file is a small one, it completes in no time. so this methods works (bp in seq)
# if the file is very large, it might take days to complete the search
# In that case we might go letter by letter searching

# KMP algo is a very efficient algorithm to find a substring in a given string