import pandas as pd

# Sample data (you can adjust these lists as needed)
distance = [2]
gradient = [1.5]
midpoint = [(1, 2)]
equation = ['y = 2x + 1']

# Ensure all lists have the same number of elements
assert len(distance) == len(gradient) == len(midpoint) == len(equation), "All lists must have the same length."

# Create a dictionary for the DataFrame
data_dict = {
    "Attribute": [
        "Coordinates given:",
        "Distance between X and Y:",
        "Gradient of the line:",
        "Midpoint of the line:",
        "Equation of the line:"
    ],
    "Value": [
        "_",
        distance,
        gradient,
        midpoint,
        equation
    ]
}

# Create the DataFrame
coordinate_geometry_calculator_frame = pd.DataFrame(data_dict)

# Print the formatted output
print("              -COORDINATE GEOMETRY CALCULATOR-")
# Loop through rows to print in the desired format
for index, row in coordinate_geometry_calculator_frame.iterrows():
    attribute = row['Attribute']
    value = row['Value']
    if isinstance(value, list):  # Format lists nicely
        value_str = f"{value}"
    else:  # Keep single values as-is
        value_str = str(value)
    print(f"{attribute:<25} {value_str}")

