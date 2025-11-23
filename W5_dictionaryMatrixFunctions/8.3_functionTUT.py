# Q. Write a python code using functions which checks whether the input coordinates form a triangle or not

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

x1 = get_float("Enter x coordinate of 1st point: ")
y1 = get_float("Enter y coordinate of 1st point: ")
x2 = get_float("\nEnter x coordinate of 2nd point: ")
y2 = get_float("Enter y coordinate of 2nd point: ")
x3 = get_float("\nEnter x coordinate of 3rd point: ")
y3 = get_float("Enter y coordinate of 3rd point: ") 



#************************
# * APPROACH-1 ( Using Distance between the points )
#************************


# def distance(xi, yi, xj, yj):
#     return (((xi-xj)**2 + (yi-yj)**2)**0.5)

# d1 = distance(x1, y1, x2, y2)
# d2 = distance(x2, y2, x3, y3)
# d3 = distance(x3, y3, x1, y1)

# print(f"Distance betweeen the points {(x1, y1)} and {(x2, y2)} = {d1}")
# print(f"Distance betweeen the points {(x2, y2)} and {(x3, y3)} = {d2}")
# print(f"Distance betweeen the points {(x3, y3)} and {(x1, y1)} = {d3}")


# def isTriangle(d1, d2, d3):
#     dList = [d1, d2, d3]
#     dList.sort(reverse=True)
#     l1, l2, l3 = dList

#     return l1 < (l2 + l3)
    
# print("Triangle" if isTriangle(d1, d2, d3) else "Not a Triangle")




#************************
# * APPROACH-2 ( Using Slope )
#************************

import math

def slope(xi, yi, xj, yj):
    if(xi == xj):
        return (math.inf)     # infinity
    else:
        return ((yj - yi) / (xj - xi))

s1 = slope(x1, y1, x2, y2)
s2 = slope(x2, y2, x3, y3)
# s3 = slope(x3, y3, x1, y1)     # not required

print("Triangle" if s1 != s2 else "Not a Triangle")




#************************
# * OTHER APPROACHES: Check area using determiant, Check area using herons formula
#************************

