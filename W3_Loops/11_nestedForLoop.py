
# ********** Lec 10 [ Nested Iteration ] 


# Two brothers Sharath and Tanmay

s="VIBGYOR"
v="VIBGYOR"

count=0
for i in range(7):
    for j in range(7):
        print(f"{s[i]}, {s[j]}")
        count += 1
print(f"The total ways in which the two brothers can wear 7 different colors: {count}")