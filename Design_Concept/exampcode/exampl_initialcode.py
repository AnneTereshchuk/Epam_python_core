# Initial code to calculate the area of different shapes based on user input

# Ask user to provide the type of shape
shape_type = input('Please, provide a shape you want to calculate area: ')

# Check if the shape is square
if shape_type == 'square':
    # If square, ask for the side length
    a = input('side length: ')
    # Check if the input is a valid number
    if a.isdigit():
        a = int(a)
        # Calculate and print the area of the square
        s = a ** 2
        print(f'square area: {s}')
    else:
        # If input is not a number, print an error message
        print(f'{a} is not a number ')

# Check if the shape is rectangle
elif shape_type == 'rectangle':
    # If rectangle, ask for the length and width
    a = input('length:')
    b = input('width:')
    # Check if both inputs are valid numbers
    if a.isdigit():
        a = int(a)
        if b.isdigit():
            b = int(b)
            # Calculate and print the area of the rectangle
            s = a * b
            print(f'rectangle area: {s}')
        else:
            # If width input is not a number, print an error message
            print(f'{b} is not a number ')
    else:
        # If length input is not a number, print an error message
        print(f'{a} is not a number ')

# Check if the shape is circle
elif shape_type == 'circle':
    # If circle, ask for the radius
    r = input('radius:')
    # Check if the input is a valid number
    if r.isdigit():
        r = int(r)
        # Calculate and print the area of the circle
        s = 3.14 * r ** 2
        print(f'circle area: {s}')
    else:
        # If input is not a number, print an error message
        print(f'{r} is not a number')

# If the shape is not recognized
else:
    # Print an error message
    print(f"I don't know {shape_type} shape :-(")
