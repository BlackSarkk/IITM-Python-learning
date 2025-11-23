
# ********** Lec 8 [ More on range, forEach ]

for x in range(10):
    print(f"This goes from 0-9 {x}")


for x in range(1, 10):
    print(f"This goes from 1-9 {x}")


for x in range(1, 10, 2):
    print(f"This goes from 1-9, skipping 2 steps {x}")  # note by default step=1


for x in range(10, 1, -2):
    print(f"This goes from 10-1, skipping 2 steps {x}")


#################################
#################################

country = "India"
for letter in country:
    print(letter)
    
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])