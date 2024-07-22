import pandas as pd

# Sample data
distance = [2, 3, 4]
gradient = [1.5, 2.0, 2.5]
midpoint = [(1, 2), (2, 3), (3, 4)]
equation = ['y = 2x + 1', 'y = x - 1', 'y = 3x + 2']

# Ensure all lists have the same number of elements
assert len(distance) == len(gradient) == len(midpoint) == len(equation), "All lists must have the same length."

# Create a list of tuples for easier DataFrame construction
data = [
    ("Coordinates given:", "_"),
    ("   Distance between X and Y:", distance),
    ("Gradient of the line:", gradient),
    ("Midpoint of the line:", midpoint),
    ("Equation of the line:", equation)
]

# Create a DataFrame from the list of tuples
coordinate_geometry_calculator_frame = pd.DataFrame(data, columns=["Attribute", "Value"])

# Print the formatted output
print("                    COORDINATE GEOMETRY CALCULATOR:")
print(coordinate_geometry_calculator_frame.to_string(index=False, header=False))
