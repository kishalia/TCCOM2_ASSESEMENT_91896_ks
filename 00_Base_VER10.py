import math
from fractions import Fraction
import pandas as pd


# Function to check yes or no response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in {"yes", "y"}:
            return True
        elif response in {"no", "n"}:
            return False
        else:
            print("ERROR! Please answer yes or no.")


# Function to validate numerical input
def num_check(question, error, num_type=int):
    while True:
        try:
            response = num_type(input(question))
            if response < 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Function to calculate midpoint of a line
def calculate_midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


# Function to calculate slope between two points
def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x2 - x1 == 0:
        return float('inf')  # Vertical line
    else:
        return Fraction(y2 - y1, x2 - x1)


# Function to calculate equation of a line
def equation_of_line(point1, point2):
    try:
        slope = calculate_slope(point1, point2)
        if slope == float('inf'):
            return f"x = {point1[0]}"  # Equation of vertical line
        else:
            intercept = point1[1] - slope * point1[0]
            return f"y = {slope}x + {intercept}"
    except ValueError as e:
        return str(e)


# Main routine
instructions = yes_no("Would you like instructions? (Please answer yeas or no.  ")
if instructions:
    print('''\n
    ***** INSTRUCTIONS *****

Please enter...

- The coordinates of:
  -Your X1 value
  -Your Y1 value
  -Your X2 value
  -Your Y2 value

The code will ask you which answers you would like to calculate. Please answer yes 
for the for the calculations you would like to be done and no for the answers
you do not want to be displayed.

If you have any values that are fractions, please convert them into decimals.

The information will automatically be written to a text file.

  **************************''')
y
print("\n- CALCULATE COORDINATE GEOMETRY -")
x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid positive number.")
y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid positive number.")
x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid positive number.")
y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid positive number.")

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
df = pd.DataFrame(results, columns=["Attribute", "Value"])

# Print the formatted output
print("\n            -COORDINATE GEOMETRY CALCULATOR-")
for index, row in df.iterrows():
    print(f"{row['Attribute']:25} {row['Value']}")
