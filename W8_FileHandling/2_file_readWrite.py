

# ********** Lec 2 [ READING_WRITING_TO_A_FILE ]


#************************************************** 
#! CREATING / WRITING TO A FILE:
#************************************************** 
#************************************************** 

f=open('2_rough.txt',"w")    # Open/Create a text file of name "2_rough.txt" in the current dir in write mode and assign that to f

f.write("Rahul ")
f.write("Cooper ")
f.write("IIT ")
f.write("python ")
f.write("INDIA.")

f.close()                   # Close the file instance


#************************************************** 
#! READING INTO A FILE:
#************************************************** 
#************************************************** 


x=open("2_rough.txt", "r")

s = x.read()

print(s) # --> prints entire text of file
type(s)  # --> str

x.close()                   # Close the file instance


#************************************************** 
#! WRITING MULTILINES TO A FILE:
#************************************************** 
#**************************************************



f=open('2_rough.txt',"w")    # Open/Create a text file of name "2_rough.txt" in the current dir in write mode and assign that to f

f.write("This is the first line")
f.write('\n')
f.write("This is the second line")
f.write('\n')
f.write("This is the third line")
f.write('\n')
f.write("This is the fourth line")
f.write('\n')
f.write("This is the fifth line")

f.close()                   # Close the file instance




#************************************************** 
#! MODES:
#************************************************** 
#**************************************************

#* r   ---  (read only)
#  - Opens file only for reading
#  - File must exist
#  - File pointer starts at beginning
#  - Error if file not found

#* w   ---  (write only, overwrite!)
#  - Opens file for writing
#  - If file exists → entire content is erased
#  - If file does not exist → it is created
#  - File pointer starts at beginning

#* a   ---  (append only)
#  - Opens file for appending new data
#  - File may or may not exist (creates if missing)
#  - File pointer starts at end
#  - Does NOT erase previous content

#* r+  ---  (read + write)
#  - Allows reading and writing
#  - File must exist
#  - Does NOT erase file contents
#  - Writing starts at beginning unless pointer moved

#* w+  ---  (write + read)
#  - Allows writing and reading
#  - File may or may not exist
#  - Erases entire file before writing
#  - File pointer at beginning

#* a+  ---  (append + read)
#  - Allows appending and reading
#  - File may or may not exist
#  - File pointer starts at end for writing
#  - To read old contents → must seek(0)


#! BINARY MODES:
# "rb"	read binary
# "wb"	write binary (overwrite)
# "ab"	append binary
# "rb+"	read + write binary
# "wb+"	write + read binary (truncate)
# "ab+"	append + read binary