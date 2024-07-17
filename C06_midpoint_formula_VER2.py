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


n = num_check("Enter the number of points: ", "ERROR!Please enter a positive integer greater than 0.", int)

sum_x = 0
sum_y = 0

for i in range(n):
    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    sum_x += x
    sum_y += y

xm = sum_x / n
ym = sum_y / n

midpoint = (xm, ym)
print(f"The midpoint of the shape is: {midpoint}")



