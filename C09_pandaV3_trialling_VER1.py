import pandas as pd

# Sample data (you can adjust these lists as needed)

point1 = [(2, 3), (3, 4), (4, 5)]
point2 = [(5, 6), (6, 7), (7, 8)]
distance = [2, 3, 4]
gradient = [1.5, 2.0, 2.5]
midpoint = [(1, 2), (2, 3), (3, 4)]
equation = ['y = 2x + 1', 'y = x - 1', 'y = 3x + 2']

# Ensure all lists have the same number of elements
assert len(distance) == len(gradient) == len(midpoint) == len(equation), "All lists must have the same length."

# Create the dictionary with the data
coordinate_geometry_dict = {
    "- POINT 1 - ": point1, "- POINT 2 - ":point2,
    " -DISTANCE BETWEEN X AND Y- ": distance, " -GRADIENT OF THE LINE- ": gradient,
    " -MIDPOINT OF THE LINE- ": midpoint, " -EQUATION OF A LINE- ": equation,
}

# Create the DataFrame
coordinate_geometry_calculator_frame = pd.DataFrame(coordinate_geometry_dict)

# Set pandas display options to show all columns completely
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent the DataFrame from being truncated

print("                                     -COORDINATE GEOMETRY CALCULATOR-")
# Print the DataFrame
print(coordinate_geometry_calculator_frame)

