

# ********** Lec 4 [ VERY_BIG_TEXT_FILE_HANDLING ]


#************************************************** 
#! READING THROUGH EXTREMELY LARGE FILE SYSTEM
#************************************************** 
#************************************************** 

# Lets say we have a very large text file of 12GB 
# Its obvious basic system cant even open it using file readers


f=open('4_rough.txt',"w")   
f.write("2389035")
f.write('\n')
f.write("4235525")
f.write('\n')
f.write("2349187")
f.write('\n')
f.write("34981423")
f.write('\n')
f.write("90823523")
f.close()      

# Assume we created the 12GB FILE
# So if we try to open the file, it will make system hang 

# NOTE: no matter how big the file is, we can always do f.readline()
#       so we can always go linearly in this fashion, one after the other, without making our system hung
#       thats how the movie files works, it goes linearly one by one pictures

f=open('4_rough.txt',"r")   

print((f.readline()).strip("\n"))   #? always possible independent of file-size
print((f.readline()).strip("\n")) 
print((f.readline()).strip("\n")) 


