# Q. Write a python code using functions to calculate area and perimeter of circle and rectangle

# ******************************************
# * STANDARD CODE: (APPROACH 1)
# ******************************************
   
# PI = 22 / 7

# def circle_area(r):
#     return(PI * r * r)

# def circle_perimeter(r):
#     return(2 * PI * r)

# def rectangle_area(l, b):
#     return(l * b)

# def rectangle_perimeter(l, b):
#     return(2 * (l+b))


# r = float(input('\nEnter the radius of the circle: '))
# cArea = circle_area(r)
# print(f"\nArea of circle with radius {r} = {cArea} sq. units")
# cPerimeter = circle_perimeter(r)
# print(f"\nPerimeter of circle with radius {r} = {cPerimeter} units")

# l = float(input('\nEnter the length of the rectangle: '))
# b = float(input('\nEnter the breadth of the rectangle: '))
# rArea = rectangle_area(l, b)
# print(f"\nArea of rectangle with length {l} and breadth {b} = {cArea} sq. units")
# rPerimater = rectangle_perimeter(l, b)
# print(f"\nPerimeter of rectangle with length {l} and breadth {b} = {cPerimeter} sq. units")



# ******************************************
# * MENU DRIVEN CODE: (APPROACH 2)
# ******************************************


PI = 22 / 7

def circle_area(r):
    return(PI * r * r)

def circle_perimeter(r):
    return(2 * PI * r)

def rectangle_area(l, b):
    return(l * b)

def rectangle_perimeter(l, b):
    return(2 * (l+b))


polygon = ''
while(polygon != 'exit'):
    print("\nPOLYGONS: \n- circle\n- rectangle\n- exit")
    polygon = input('\nChoose the polygon type or exit: ')

    if (polygon.lower() == "circle"):
        r = float(input("\nEnter the radius of circle: "))
        while True:
            property = ''
            print("\nCIRCLE PROPERTIES:\n- area\n- perimeter\n- back")
            property= input("\nChoose the circle property or go back: ")

            if(property.lower() == "area"):
                print(f'\nArea of circle with radius {r} = {circle_area(r)}')
            elif(property.lower() == "perimeter"):
                print(f'\nPerimeter of circle with radius {r} = {circle_perimeter(r)}')
            elif(property.lower() == "back"):
                break
            else:
                print('\n--------------------\nPlease enter a valid input\n--------------------\n')


    elif(polygon.lower() == 'rectangle'):
        l = float(input("\nEnter the length of rectangle: "))
        b = float(input("\nEnter the breadth of rectangle: "))

        while True:
            property = ''
            print("\nRECTANGLE PROPERTIES:\n- area\n- perimeter\n- back")
            property= input("\nChoose the rectangle property or go back: ")

            if(property.lower() == "area"):
                print(f'\nArea of rectangle with length {l} and breadth {b} = {rectangle_area(l, b)}')
            elif(property.lower() == "perimeter"):
                print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rectangle_perimeter(l, b)}')
            elif(property.lower() == "back"):
                break
            else:
                print('\n--------------------\nPlease enter a valid input\n--------------------\n')

    elif(polygon.lower() == 'exit'):
        break

    else:
        print('\n--------------------\nPlease enter a valid input\n--------------------\n')




