import math
from fractions import Fraction


# function checks if user inputted yes or no as their response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")


def not_blank(question, error):
    while True:
        response = input(question)
        if response.strip() == "":
            print(error)
        else:
            return response.strip()


# Function displays the instructions on how to use the code
def show_instructions():
    print('''\n
    ***** INSTRUCTIONS *****

Please enter...

- The coordinates of :
  Your "X" value
  Your "Y" value

Select the information you would like to work out:
- Distance
- Gradient
- Midpoint
- Equation of a line

Once you have selected what information you would like to input, press enter.
The distance, gradient, midpoint and equation of a line will be displayed.

The information will be written to a text file.

  **************************''')


# Function does not allow user to enter zero as their answer

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


def calculate_distance(point1, point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])
    return math.sqrt(px ** 2 + py ** 2)


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


# Main routine starts here:

# C01: Distance formula
# calculates the distance between two points and displays the coordinates to the user
# Asks user to enter the coordinates of point 1
print("-DISTANCE BETWEEN TWO POINTS-")
print("Enter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.", float)
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.", float)

# Asks user to enter the coordinates of point 2
print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.", float)
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.", float)

point1 = (x1, y1)
point2 = (x2, y2)

# Calculate and display distance
distance = calculate_distance(point1, point2)
print(f"\nDistance between Point 1 {point1} and Point 2 {point2} is: {distance:.2f}")

# C02: Midpoint Formula
# works out the midpoint between two points
print("-MIDPOINT-")
x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))

x2 = int(input("enter x2: "))
y2 = int(input("enter y2: "))

xm = (x1 + x2) / 2
ym = (y1 + y2) / 2

midpoint = xm, ym
print(f"the 2 points are: {midpoint} ")

# CO3: Equation of a line
# code works out the equation of a line
print("-EQUATION OF A LINE-")
# ask for user's coordinates
print("\nEnter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

# displays the equation of a line
equation = equation_of_line(x1, x2, y1, y2)
print("Equation of the line:")
print(equation)

# Works out the gradient of the line
print("-GRADIENT OF THE LINE-")
# asks for user's coordinates
print("\nEnter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.")
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.")

# displays the gradient of the line
gradient = calculate_slope(x1, x2, y1, y2)
print("The Gradient of the line is: ")
print(gradient)



