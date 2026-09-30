# This function calculates the area and perimeter of a rectangle
def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

#Ask the user to enter the length and width
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

#Call the function and store both returned values
area, perimeter = rectangle_stats(length, width)

#Display the area and perimeter rounded to two decimal places
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")