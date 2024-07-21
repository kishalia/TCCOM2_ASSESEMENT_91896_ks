from fractions import Fraction


def not_blank(question, error):
    while True:
        response = input(question)
        if response.strip() == "":
            print(error)
        else:
            return response.strip()


# Function to validate and retrieve a positive integer
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


def calculate_intercept(x, y, slope):
    return y - slope * x


def equation_of_line(x1, x2, y1, y2):
    try:
        slope = calculate_slope(x1, y1, x2, y2)
        intercept = calculate_intercept(x1, y1, slope)
        return f"y = {slope}x + {intercept}"
    except ValueError as e:
        return str(e)


print("\nEnter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

equation = equation_of_line(x1, x2, y1, y2)
print("The Equation of the line is: ")
print(equation)
