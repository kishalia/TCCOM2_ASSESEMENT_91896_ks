# function goes here

# function checks if user responded with a blank.
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("This cannot be blank.Please try again.")

        else:
            return response


# main routine goes here
while True:
    name = not_blank("Please enter yes or no.").upper()
    if name == 'QUIT':
        break

print("We are done!")
