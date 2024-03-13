# Step 4. Moving the Calculation of an Area Into Different Methods

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


# Define a method to calculate the area for a square
def square_area(side_length):
    """Calculate area for square."""
    return side_length ** 2


# Define a method to calculate the area for a rectangle
def rectangle_area(length, width):
    """Calculate area for rectangle."""
    return length * width


# Define a method to calculate the area for a circle
def circle_area(radius):
    """Calculate area for circle."""
    return 3.14 * radius ** 2


# Ask user to provide a shape for which to calculate the area
shape_type = input('Please, provide a shape you want to calculate area: ')

# Check the type of shape and calculate the area accordingly
if shape_type == 'square':
    a = get_user_param('side length:')
    print(f'square area: {square_area(a)}')

elif shape_type == 'rectangle':
    a = get_user_param('length:')
    b = get_user_param('width:')
    print(f'rectangle area: {rectangle_area(a, b)}')

elif shape_type == 'circle':
    r = get_user_param('radius:')
    print(f'circle area: {circle_area(r)}')

else:
    # If the shape is not recognized, print an error message
    print(f"I don't know {shape_type} shape :-(")
