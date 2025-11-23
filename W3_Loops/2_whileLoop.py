
# ********** Lec 2 [ While Loop ]

print("When did India get its Independence (year)?")
year=int(input())

# if (year==1947):
#     print("You're god damn right!")
# else:
#     print("Comeon, don't you know even this")
#     print("That's ok, I will let you attempt this once more")
#     print("When did India get its Indepencence?")
#     year=int(input())
#     if(year==1947):
#         print("You got it")
#     else:
#         print("Failed in your second attempt too? grrrr...")    


#? Writing a piece of code, which lets the use attempt as many times as he wants. 
#? The code will end only when it gets the right answer.

while(year!=1947):
    print("You got this wrong. Enter once again.")
    year=int(input())

print("You're god damn right!")


#  while works like this:
    # while <condition>
        # write whatever you want here
        # write whatever you want here
        # write whatever you want here
