import math
from fractions import Fraction
import pandas as pd


# Function to check if user inputted yes or no as their response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in {"yes", "y"}:
            return True
        elif response in {"no", "n"}:
            return False
        else:
            print("ERROR! Please answer yes or no.")


# function checks the number
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


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])
    return math.sqrt(px ** 2 + py ** 2)


# Function to calculate midpoint of a line
def calculate_midpoint(point1, point2):
    xm = (point1[0] + point2[0]) / 2
    ym = (point1[1] + point2[1]) / 2
    return (xm, ym)


# Function to calculate slope between two points
def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if x2 - x1 == 0:
        return float('inf')  # show that gradient does not apply
    else:
        return Fraction(y2 - y1, x2 - x1)


# Function to calculate equation of a line
def equation_of_line(point1, point2):
    try:
        slope = calculate_slope(point1, point2)
        if slope == float('inf'):
            return "x = {}".format(point1[0])  # Equation of vertical line
        else:
            intercept = point1[1] - slope * point1[0]
            return f"y = {slope}x + {intercept}"
    except ValueError as e:
        return str(e)


# Main routine
instructions = yes_no("Would you like instructions? ")
if instructions:
    print('''\n
    ***** INSTRUCTIONS *****

Please enter...

- The coordinates of :
  Your "X" value
  Your "Y" value

The code will display the distance, midpoint, gradient, and the equation of a line in the 
format of a panda.

If you have any values that are fractions, please convert it into a decimal.

  **************************''')

print("\n- CALCULATE COORDINATE GEOMETRY -")
x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid positive number: ", int)
y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid positive number: ", int)
x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid positive number: ", int)
y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid positive number: ", int)

point1 = (x1, y1)
point2 = (x2, y2)

# Ask user which calculations they want
print("\nWhich calculations would you like to perform?")
calculate_distance_question = yes_no("Calculate distance? ")
calculate_midpoint_question = yes_no("Calculate midpoint? ")
calculate_gradient_question = yes_no("Calculate gradient? ")
calculate_equation_question = yes_no("Calculate equation of line? ")

# Calculate based on user's choices
results = []
if calculate_distance_question:
    distance = calculate_distance(point1, point2)
    results.append(("Distance between X and Y:", f"{distance:.2f}"))

if calculate_midpoint_question:
    midpoint = calculate_midpoint(point1, point2)
    results.append(("Midpoint of the line:", midpoint))

if calculate_gradient_question:
    gradient = calculate_slope(point1, point2)
    results.append(("Gradient of the line:", gradient))

if calculate_equation_question:
    equation = equation_of_line(point1, point2)
    results.append(("Equation of the line:", equation))

# Create DataFrame
data = {
    "Attribute": [result[0] for result in results],
    "Value": [result[1] for result in results]
}

df = pd.DataFrame(data)

# Print the formatted output
print("\n            -COORDINATE GEOMETRY CALCULATOR-")
for index, row in df.iterrows():
    attribute = row['Attribute']
    value = row['Value']
    value_str = ', '.join(map(str, value)) if isinstance(value, tuple) else str(value)
    print(f"{attribute:<25} {value_str}")
