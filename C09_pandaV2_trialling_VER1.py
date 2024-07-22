import pandas

# dictionaries to hold coordinate details

distance = [2]
gradient = [1]
midpoint = [3]
equation = [2]

coordinate_geometry_dict = {
    "-DISTANCE BETWEEN X AND Y-": distance,
    "-GRADIENT OF THE LINE-": gradient,
    "-MIDPOINT OF THE LINE-": midpoint,
    "-EQUATION OF A LINE-": equation
}

coordinate_geometry_calculator_frame = pandas.DataFrame(coordinate_geometry_dict)

print(coordinate_geometry_calculator_frame)


