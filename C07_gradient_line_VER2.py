from fractions import Fraction


def num_check(question, error, num_type=float):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if x2 - x1 == 0:
        return float('inf')  # show that gradient does not apply
    else:
        return Fraction(y2 - y1, x2 - x1)


x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid positive number: ", int)
y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid positive number: ", int)
x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid positive number: ", int)
y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid positive number: ", int)

point1 = (x1, y1)
point2 = (x2, y2)

gradient = calculate_slope(point1, point2)

print("The Gradient of the line is: ")
print(gradient)
