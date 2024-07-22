from fractions import Fraction


# program works out the gradient of a line
# equation : (y2-y1)/x2 - x1

def num_check(question, error, num_type=int):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def calculate_slope(x1, x2, y1, y2):
    if x2 - x1 == 0:
        raise ValueError("The line is vertical (undefined slope)")
    else:
        return Fraction(y2 - y1, x2 - x1)


print("\nEnter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

gradient = calculate_slope(x1, x2, y1, y2)
print("The Gradient of the line is: ")
print(gradient)

