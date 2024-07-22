import pandas as pd

# Sample data (you can adjust these lists as needed)
distance = [2]
gradient = [1.5]
midpoint = [(1, 2)]
equation = ['y = 2x + 1']

# Ensure all lists have the same number of elements
assert len(distance) == len(gradient) == len(midpoint) == len(equation), "All lists must have the same length."

# Create a DataFrame
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
        distance,
        gradient,
        midpoint,
        equation
    ]
}

df = pd.DataFrame(data)

# Print the formatted output
print("            -COORDINATE GEOMETRY CALCULATOR-")
for index, row in df.iterrows():
    attribute = row['Attribute']
    value = row['Value']
    value_str = ', '.join(map(str, value)) if isinstance(value, list) else str(value)
    print(f"{attribute:<25} {value_str}")
