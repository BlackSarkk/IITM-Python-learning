
# ********** Lec 8 [ if / else / elif ]

# Let us consider the movie "Avengers". This is 13+ movie.

print("Please enter your date of birth")

birth_year = int(input())
current_year = 2021
age=current_year-birth_year

if (age<13):
    print("You are under age, you cannot watch this movie.")
    print("Wait until you are old enough to watch this movie.")
else:
    print("You are old enough to watch Avengers, enjoy!")
    print("Dont forget to watch the sequels and prequels.")
    
print("Have a nice time")