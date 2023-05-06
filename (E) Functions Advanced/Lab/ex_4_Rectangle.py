# Create a function called rectangle(). It must have two parameters - length and width.
# First, you need to check if the given arguments are integers:
# •	If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
# Create two inner functions:
# •	area() - returns the area of the rectangle with the given length and width
# •	perimeter() - returns the perimeter of the rectangle with the given length and width
# In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle in the following format:
# "Rectangle area: {ract_area}
# Rectangle perimeter: {rect_perim}"
# Test Code                 	Output
# print(rectangle(2, 10))	    Rectangle area: 20
# Rectangle perimeter: 24
# print(rectangle('2', 10))	    "Enter valid values!"

def rectangle(length, width):
    if type(length) != int:
        return "Enter valid values!"
    if type(width) != int:
        return "Enter valid values!"

    def area(length, width):
        return length * width

    def perimeter(length, width):
        return 2 * (width + length)

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))