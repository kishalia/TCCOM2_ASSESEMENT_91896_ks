import math


# function check if user responded with yes/no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

    print("Please enter either yes or no...\n")


# checks if user responded with a blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


# number checker that checks if user entered an integer
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# code works out the distance between two points

point1 = 100000000
point2 = 100000000


# distance function that gets the x value and y value of the given shape
def distance(point1,point2):
    px = (point1[0] - point2[0])
    py = (point1[1] - point2[1])

    return math, math.sqrt(px ** 2 + py ** 2)


type_coordinates = []
coordinates = type_coordinates
while point1 and point2 < 0:
    type_coordinates = not_blank("Please enter the coordinates of your shape.('X.Y')")

type_coordinates = not_blank("Coordinates of your shape: (x,y) ", "This cannot be blank."
                                                                  "Please type in the coordinates to continue"
                                                                  "or press 'xxx' to exit the program.")
