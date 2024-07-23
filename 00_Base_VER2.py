import pandas
import math
from fractions import Fraction
import pandas as pd


# Function to check if user inputted yes or no as their response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR! Please answer yes or no.")


# Function to validate non-blank input
def not_blank(question, error):
    while True:
        response = input(question)
        if response.strip() == "":
            print(error)
        else:
            return response.strip()


# Function to display instructions
def show_instructions():
    print('''\n
    ***** INSTRUCTIONS *****

Please enter...

- The coordinates of:
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


# Function to validate numerical input
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


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])
    return math.sqrt(px ** 2 + py ** 2)


# Function to calculate slope between two points
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("The line is vertical (undefined slope)")
    else:
        return Fraction(y2 - y1, x2 - x1)


# Function to calculate equation of a line
def equation_of_line(x1, y1, x2, y2):
    try:
        slope = calculate_slope(x1, y1, x2, y2)
        intercept = y1 - slope * x1
        return f"y = {slope}x + {intercept}"
    except ValueError as e:
        return str(e)


# Function to prompt user for coordinates and calculate midpoint
def calculate_midpoint():
    x1 = num_check("Enter x1: ", "Please enter a valid positive number: ")
    y1 = num_check("Enter y1: ", "Please enter a valid positive number: ")
    x2 = num_check("Enter x2: ", "Please enter a valid positive number: ")
    y2 = num_check("Enter y2: ", "Please enter a valid positive number: ")
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    return xm, ym


# Main routine
print("-COORDINATE GEOMETRY CALCULATOR-")

# Calculate Distance
print("\n-DISTANCE BETWEEN TWO POINTS-")
x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid positive number: ")
y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid positive number: ")
x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid positive number: ")
y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid positive number: ")
point1 = (x1, y1)
point2 = (x2, y2)
distance = calculate_distance(point1, point2)
print(f"Distance between Point 1 {point1} and Point 2 {point2} is: {distance:.2f}")

# Calculate Midpoint
print("\n-MIDPOINT-")
midpoint = calculate_midpoint()
print(f"Midpoint of the line is: {midpoint}")

# Calculate Equation of a Line
print("\n-EQUATION OF A LINE-")
equation = equation_of_line(x1, y1, x2, y2)
print(f"Equation of the line is: {equation}")

# Calculate Gradient
print("\n-GRADIENT OF THE LINE-")
gradient = calculate_slope(x1, y1, x2, y2)
print(f"Gradient of the line is: {gradient}")

# Create DataFrame
data = {
    "Attribute": [
        "Coordinates given:",
        "Distance between X and Y:",
        "Gradient of the line:",
        "Midpoint of the line:",
        "Equation of the line:"
    ],
    "Value": [
        "_",
        f"{distance:.2f}",
        f"{gradient}",
        f"{midpoint}",
        f"{equation}"
    ]
}

df = pd.DataFrame(data)

# Print DataFrame in desired format
print("\n            -COORDINATE GEOMETRY CALCULATOR-")
for index, row in df.iterrows():
    attribute = row['Attribute']
    value = row['Value']
    print(f"{attribute:<25} {value}")
