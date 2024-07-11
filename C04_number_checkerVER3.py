# recycled number checker from previous project (Fundraising Calculator)
def number_checker(question):
    while True:

        try:
            response = int(input(question))
            pass

        except ValueError:
            print("Please enter an integer.")
        if response <= 0:
            print(error)


x1 = number_checker("Enter X coordinate: ")

