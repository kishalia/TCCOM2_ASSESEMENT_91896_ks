def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                pass

        except ValueError:
            print(error)


# Main routine goes here
x1 = num_check("Enter X coordinate: ", "Please enter a valid positive integer.", float)