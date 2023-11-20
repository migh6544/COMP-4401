# COMP 4401
# Homework 1 - Variables & Boolean Expressions

# Submit homework 1 responses in a single .py file. Responses to questions 1-4 can be included in Python script files using line comments (# comment) or multiline comments using triple quotes (‘’’comment’’’). 

# For questions 1-4 solve without using python to ensure you understand data types and boolean expression, you can then verify your answers using python.

#--------------------------------------------------------------------------#

# 1. For each of the following expression, identify the data type and value (10 points):
#A) 5+3/5*(4-10)
    # Answer:
            # Type = Float
            # Value = 1.4000000000000004
#B) 17//3**4
    # Answer:
            # Type = Int
            # Value = 0

# 2. Evaluate the following boolean expressions (10 points):
#A) 15 % 4 < 20/3
    # Answer:
            # True
#B) False or not (False or True) and True
    # Answer:
            # False
#C) 3/4==0or5<6
    # Answer:
            # True

# 3. Let a = True, b = True, c = False. Evaluate the following (15 points):
#A) a and not b
    # Answer:
            # False

#B) b or c
    # Answer:
            # True

#C) not b == c
    # Answer:
            # False

#D) a and not c
    # Answer:
            # True

#E) b or c and not a
    # Answer:
            # True

#F) a != b or b != c
    # Answer:
            # True

# 4. Select all invalid variable names below and give reason the variable name is invalid (15 points):
#A) speed Of Light
    # Answer:
            # Invalid -> Contains spaces in the name
#B) x_2
    # Answer:
            # Valid
#C) 3Attempts
    # Answer:
            # Invalid -> Starts with a number and does not start with a letter or underscore '_'
#D) vertical-distance
    # Answer:
            # Invalid -> Uses a hyphen '-' instead of an underscore '_'
#E) B5V
    # Answer:
            # Valid

# 5. Write code that initializes a variable to store the length of a square in inches, calculates the perimeter and area of the square, and prints the results. Test the program by changing the initial value for length to different integer values (15 points).

# Initializing the length of the square
squareLength = 3
# Calculating the perimeter and area
squarePerimeter = (4 * squareLength)
squareArea = (squareLength ** 2)
# Printing results
print(f'The square\'s length is: {squareLength} Inches'
      f'The square\'s perimeter is: {squarePerimeter} Inches'
      f'The square\'s area is: {squareArea} Square-Inches'
)

# 6. Write code that will assign a variable to a given number of seconds and then calculate the equivalent number of hours, minutes and seconds. For example, 300 seconds is 0 hours, 5 minutes and 0 seconds while 4503 seconds is 1 hour, 15 minutes and 3 seconds. Assign separate variables to each of these values (i.e., hours, minutes, seconds). Evaluate your program calculations using different starting times (initial seconds). Be mindful of possible rounding errors, use integers only (15 points).

# Reading the number of seconds from the user input and converting it to int
seconds = int(input("Enter the number of seconds: "))
# Calculating hours from total seconds using floor to avoid floats
hours = int(seconds // 3600)
# Calculating seconds remaining from calculated hours
seconds = int(seconds % 3600)
# Calculating minutes from remaining seconds using floor to avoid floats
minutes = int(seconds // 60)
# Calculating seconds remaining from calculated minutes
seconds = int(seconds % 60)
# Printing the results in time format
print(
    f'The total time in seconds provided is the equivalent of: \n'
    f'{hours} Hour(s), {minutes} Minute(s), and {seconds} Seconds.'
)

# 7. Debug the following code which greets a guest and checks if the guest can get on a ride by checking their age and height (10 points) :

name = "Josh"
heightInches = 62.4
age = 15
print(f"Hello, {name}")

# 8. Write code that checks the data types of the following variables and casts them to the proper data type if needed (10 points):

age = 32.4
avgHeight = "73.54"
numOfGuests = 47.0
flightSpeed = "423 miles/hour"
outsideTemp = 73.2

# Checking and casting the data types assuming the decimal spaces are to be preserved according to conventional use
print(
    f'{age}\n'
    f'Is age an integer: {type(age) == int}, {type(age)}.\n'
    f'Fixed! Is age an integer now: {type(int(age)) == int}.'
)
print(
    f'{avgHeight}\n'
    f'Is avgHeight a float: {type(avgHeight) == float}, {type(avgHeight)}.\n'
    f'Fixed! Is avgHeight an integer now: {type(float(avgHeight)) == float}.'
)
print(
    f'{numOfGuests}\n'
    f'Is numOfGuests a float: {type(numOfGuests) == int}, {type(numOfGuests)}.\n'
    f'Fixed! Is numOfGuests an integer now: {type(int(numOfGuests)) == int}.'
)
print(
    f'{outsideTemp}\n'
    f'Is outsideTemp a float: {type(outsideTemp) == float}, {type(outsideTemp)}.\n'
    f'Fixed! Is outsideTemp an integer now: {type(float(outsideTemp)) == float}.'
)
print(
    f'{flightSpeed}\n'
    f'Is flightSpeed a float: {type(flightSpeed) == int}, {type(flightSpeed)}.\n'
    f'Fixed! Is flightSpeed an integer now: {type(int(flightSpeed[0:3])) == int}.'
)