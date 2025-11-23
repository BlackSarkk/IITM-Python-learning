
# ********** Lec 10 [ Break, Continue, Pass ] 


#! break 
# Seperating username from email

# email=str(input("Type your email: "))
# for c in email:
#     if (c == '@'):
#       break
#     print(c, end="")
# print()     





#! break and continue
# Seperating username and domain from email

# email=str(input("Type your email: "))
# for c in email:
#     if (c == '@'):
#       print()     
#       continue
#     print(c, end="")
# print()     



#! pass

for x in range(11):
  if(x%3==0):
    print(x)
  else:
    pass  # When we're unsure what we'll do, we use pass

# The difference between a comment and pass is that comments are completely ignored by the Python interpreter, while pass is a valid statement that the interpreter executes but does nothing.