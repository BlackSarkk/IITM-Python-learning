
# ********** Lec 9 [ Printing styles ]

#? print statement accepts another parameters called sep and end


#####################
#? Here it will print statements in a new line 

# for x in range(10):
#     print(x) 


#####################
#? Here it will print statements in the same line seperated with an space 
#! end

# for x in range(10):
#     print(x, end=' ')  # setting delimiter as " "


    
######################
#? Using both end and sep
#! end and sep
#! default value of sep is " "


# d = 10
# m = 5
# y = 2021

#? By default in print() the sep is " "
# print("Today's date is", d, m, y)
#? We can change it tho
# print("Today's date is", d, m, y, sep = "/")
# print("Today's date is", d, m, y, sep = "")

#? tho we can also change what the print statement will end with
#? the default end is "\n"
# print("Today's date is", d, m, y, end = "/")

   
   
    
#######################
#? formatted printing

# print(f"{d} {m} {y}")



########################
#? C style

# d = 10
# m = 5
# y = 2021
# print("%d %d %d" % (d, m, y))             # d coz int


########################
#? Using .format statement

# print("{0} X {1} = {2}".format(2, 3, 6))


########################
#? Using format specifiers, limiting number of digits after decimal

# pi = 22 / 7    
# print(f"Value of PI = {pi:.2f}")          
# print(f"Value of PI = {0:.2f}".format(pi))
# print(f"Value of PI = %.2f" % (pi) )          # This one has some limitations, coz C had that division limitation


########################
#? Shifting orientation of text to right aligned while printing 

#? left aligned
# print("{0}".format(1))       # max 5 characters && d for int
# print("{0}".format(11))
# print("{0}".format(111))
# print("{0}".format(1111))


#? right aligned
# print("{0:5d}".format(1))       # max 5 characters && d for int
# print("{0:5d}".format(11))
# print("{0:5d}".format(111))
# print("{0:5d}".format(1111))

# note: Strings are left alligned by default whereas int are right aligned by default
print("|{0:10s}|{1:5d}|".format("Rahul", 20))   #0th element me 10s ka space add kro and 1st element ko 5d ka space add kro
                                                #then print kro on the default position
                                                
print("|{0:10s}|{1:<5d}|".format("Rahul", 20))  #Print the 0th elem on the default position
                                                #Print the 1st elem on the left position                                                

# < left
# > right
# ^ center