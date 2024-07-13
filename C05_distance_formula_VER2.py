import math


# Function to prompt user for non-blank input
def not_blank(question, error):
    while True:
        response = input(question)
        if response.strip() == "":
            print(error)
        else:
            return response.strip()


# Function to validate and retrieve a positive integer
def num_check(question, error, num_type=int):
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


# Main program starts here

print("Enter coordinates for Point 1:")
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.", float)
y1 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.", float)

print("\nEnter coordinates for Point 2:")
x2 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.", float)
y2 = num_check("Enter Y coordinate: ", "Please enter a valid positive integer.", float)

point1 = (x1, y1)
point2 = (x2, y2)

# Calculate and display distance
distance = calculate_distance(point1, point2)
print(f"\nDistance between Point 1 {point1} and Point 2 {point2} is: {distance:.2f}")
