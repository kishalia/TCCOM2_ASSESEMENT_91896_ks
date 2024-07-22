
# Sample data (you can adjust these lists as needed)
distance = [2]
gradient = [1.5]
midpoint = [(1, 2)]
equation = ['y = 2x + 1']

# Print the formatted output
print(" -COORDINATE GEOMETRY CALCULATOR-")
print(f" Coordinates given:        _")
print(f" Distance between X and Y: {','.join(map(str, distance))}")
print(f" Gradient of the line:    {',  '.join(map(str, gradient))}")
print(f" Midpoint of the line:    {', '.join(map(str, midpoint))}")
print(f" Equation of the line:    {',  '.join(map(str, equation))}")
