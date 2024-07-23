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
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# calculates the distance
def calculate_distance(point1, point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])
    return math.sqrt(px ** 2 + py ** 2)


# calculates the gradient
def calculate_slope(x1, x2, y1, y2):
    if x2 - x1 == 0:
        raise ValueError("The line is vertical (undefined slope)")
    else:
        return Fraction(y2 - y1, x2 - x1)


# intercept calculation for equation of a line
def calculate_intercept(x, y, slope):
    return y - slope * x


# calculates the equation of the line
def equation_of_line(x1, x2, y1, y2):
    try:
        slope = calculate_slope(x1, y1, x2, y2)
        intercept = calculate_intercept(x1, y1, slope)
        return f"y = {slope}x + {intercept}"
    except ValueError as e:
        return str(e)


def calculate_midpoint(point1, point2):
    xm = (point1[0] + point2[0]) / 2
    ym = (point1[1] + point2[1]) / 2
    return (xm, ym)
