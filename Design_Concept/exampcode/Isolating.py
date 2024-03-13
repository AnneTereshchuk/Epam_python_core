# Isolating a Parameter Request From the User

# Define a function to get a parameter from the user
def get_user_param(prompt_text=''):
    """Get parameter from user."""
    value = input(prompt_text)
    # Check if the input is a valid number
    if value.isdigit():
        return int(value)
    else:
        # If input is not a number, print an error message
        print(f'{value} is not a number')

# Ask user to provide a shape for square calculation
shape_type = input('Please, provide a shape for calculate square: ')

# Check the type of shape
if shape_type == 'square':
    # If square, get the side length from the user
    a = get_user_param('side length:')
    # Calculate and print the area of the square
    s = a ** 2
    print(f'square area: {s}')

elif shape_type == 'rectangle':
    # If rectangle, get the length and width from the user
    a = get_user_param('length:')
    b = get_user_param('width:')
    # Calculate and print the area of the rectangle
    s = a * b
    print(f'rectangle area: {s}')

elif shape_type == 'circle':
    # If circle, get the radius from the user
    r = get_user_param('radius:')
    # Calculate and print the area of the circle
    s = 3.14 * r ** 2
    print(f'circle area: {s}')

else:
    # If the shape is not recognized, print an error message
    print(f"I don't know {shape_type} shape :-(")
