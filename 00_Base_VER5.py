import math
from fractions import Fraction
import pandas as pd


def num_check(prompt, error_msg):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(error_msg)
            else:
                return value
        except ValueError:
            print(error_msg)


def calculate_distance(point1, point2):
    px, py = point1[0] - point2[0], point1[1] - point2[1]
    return math.sqrt(px ** 2 + py ** 2)


def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Vertical line"
    return Fraction(y2 - y1, x2 - x1)


def calculate_midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def calculate_intercept(x, y, slope):
    return y - slope * x


def equation_of_line(x1, y1, x2, y2):
    slope = calculate_slope(x1, y1, x2, y2)
    if slope == "Vertical line":
        return f"x = {x1}"  # Equation for a vertical line
    intercept = calculate_intercept(x1, y1, slope)
    return f"y = {slope}x + {intercept}"


def main():
    print("-COORDINATE GEOMETRY CALCULATOR-")

    x1 = num_check("Enter X coordinate for Point 1: ", "Please enter a valid positive number: ")
    y1 = num_check("Enter Y coordinate for Point 1: ", "Please enter a valid positive number: ")
    x2 = num_check("Enter X coordinate for Point 2: ", "Please enter a valid positive number: ")
    y2 = num_check("Enter Y coordinate for Point 2: ", "Please enter a valid positive number: ")

    distance = calculate_distance((x1, y1), (x2, y2))
    midpoint = calculate_midpoint(x1, y1, x2, y2)
    gradient = calculate_slope(x1, y1, x2, y2)
    equation = equation_of_line(x1, y1, x2, y2)

    attributes = [
        "Coordinates given:",
        "Distance between X and Y:",
        "Gradient of the line:",
        "Midpoint of the line:",
        "Equation of the line:"
    ]
    values = [
        f"({x1}, {y1}), ({x2}, {y2})",
        f"{distance:.2f}",
        f"{gradient}",
        f"{midpoint}",
        f"{equation}"
    ]

    df = pd.DataFrame({"Attribute": attributes, "Value": values})

    print("\n            -COORDINATE GEOMETRY CALCULATOR-")
    for index, row in df.iterrows():
        print(f"{row['Attribute']:<25} {row['Value']}")


if __name__ == "__main__":
    main()
