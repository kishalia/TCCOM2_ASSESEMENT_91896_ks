import pandas

# Frames and content for export

coordinate_geometry_calculator_dict = {
    "Coordinates Given": [1],
    "Distance between X and Y": [300],
    "Gradient of the line": [1],
    "Midpoint of the line": [1],
    "Equation of the line": [1]
}

coordinate_geometry_calculator_frame = pandas.DataFrame(coordinate_geometry_calculator_dict)

# Change frames to strings
coordinate_geometry_calculator_txt = pandas.DataFrame.to_string(coordinate_geometry_calculator_frame)


print(coordinate_geometry_calculator_frame)

