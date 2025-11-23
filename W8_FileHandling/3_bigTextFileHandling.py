
# ********** Lec 3 [ BIG_TEXT_FILE_HANDLING ]

# BIG video file of 200MB may not overloads the cpu
# but big text file of 200MB cause trouble to the cpu

f=open('3_rough.txt',"w")   
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




#************************************************** 
#! readline():
#************************************************** 
#**************************************************

'''

f=open('3_rough.txt',"r")   

c = f.readline()

print(c)  # reads 1st line
print(c)  # reads 1st line      NOTE: c storing the first call of f.readline() so it will print the same thing no matter how many times we call it

print(f.readline())  # reads 2nd line
print(f.readline())  # reads 3rd line

# Basically the number of times we call it, it reads the next line everytime

f.close()      


'''

#************************************************** 
#! reading file using loop:
#************************************************** 
#**************************************************


f=open('3_rough.txt',"r")  

s=(f.readline()).strip("\n")        # reads the first line

found = False
while(s!=''):       # s='' ==> When the entire file has been read, the next readline() returns ""
    n=int(s)
    
    if (n==423555):
        print("The number was found")
        found = True
        break

    s=(f.readline()).strip("\n")    # reads the next line 

if (found == False):
    print("The number was not found")

