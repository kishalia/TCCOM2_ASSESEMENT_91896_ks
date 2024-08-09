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
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            return response  # Return the response directly
        except ValueError:
            print(error)


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])
    return round(math.sqrt(px ** 2 + py ** 2), 2)


# Function to calculate midpoint of a line
def calculate_midpoint(point1, point2):
    xm = (point1[0] + point2[0]) / 2
    ym = (point1[1] + point2[1]) / 2
    return (round(xm, 2), round(ym, 2))


# Function to calculate slope between two points
def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x2 - x1 == 0:
        return float('inf')  # vertical line
    else:
        return round((y2 - y1) / (x2 - x1), 2)


# Function to calculate equation of a line
def equation_of_line(point1, point2):
    try:
        slope = calculate_slope(point1, point2)
        if slope == float('inf'):
            return None  # Equation of vertical line, handled in printing
        else:
            intercept = point1[1] - slope * point1[0]
            return (slope, intercept)
    except ValueError as e:
        return str(e)


# Main routine

print("\n- CALCULATE COORDINATE GEOMETRY -")
x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid number: ", float)
y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid number: ", float)
x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid number: ", float)
y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid number: ", float)

point1 = (x1, y1)
point2 = (x2, y2)

# Ask user which calculations they want
print("\nWhich calculations would you like to perform?")
print("1. Calculate distance")
print("2. Calculate midpoint")
print("3. Calculate gradient")
print("4. Calculate equation of line")

selected_calculations = []
while True:
    try:
        choice = int(input("Enter the number corresponding to the calculation you want (1-4): "))
        if choice < 1 or choice > 4:
            print("Invalid choice. Please enter a number from 1 to 4.")
        else:
            selected_calculations.append(choice)
            more = yes_no("Do you want to perform another calculation? ")
            if not more:
                break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate based on user's choices
results = []

if 1 in selected_calculations:
    distance = calculate_distance(point1, point2)
    results.append(("Distance between X and Y:", distance))

if 2 in selected_calculations:
    midpoint = calculate_midpoint(point1, point2)
    results.append(("Midpoint of the line:", midpoint))

if 3 in selected_calculations:
    gradient = calculate_slope(point1, point2)
    results.append(("Gradient of the line:", gradient))

if 4 in selected_calculations:
    equation = equation_of_line(point1, point2)
    if equation:
        slope, intercept = equation
        results.append(("Equation of the line:", f"y = {slope}x + {intercept}"))
    else:
        results.append(("Equation of the line:", "x = {}".format(point1[0])))

coordinate_geometry_dict = {
    "- POINT 1 - ": (x1,y1), "- POINT 2 - ": (x2, y2),
    " -Distance between x and y - ": calculate_distance, " -Gradient of the line - ": calculate_slope,
    " -MIDPOINT OF THE LINE- ": calculate_midpoint, " -EQUATION OF A LINE- ": equation_of_line(),
}

# Create DataFrame if there are results
print(coordinate_geometry_calculator_frame)