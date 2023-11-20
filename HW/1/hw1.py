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
            # Invalid -> Contains spaces
#B) x_2
    # Answer:
            # Valid
#C) 3Attempts
    # Answer:
            # Invalid -> Does not start with a letter or underscore '_'
#D) vertical-distance 
    # Answer:
            # Invalid -> Uses a hyphen '-'
#E) B5V
    # Answer:
            # Valid

# 5. Write code that initializes a variable to store the length of a square in inches, calculates the perimeter and area of the square, and prints the results. Test the program by changing the initial value for length to different integer values (15 points).


# 6. Write code that will assign a variable to a given number of seconds and then calculate the equivalent number of hours, minutes and seconds. For example, 300 seconds is 0 hours, 5 minutes and 0 seconds while 4503 seconds is 1 hour, 15 minutes and 3 seconds. Assign separate variables to each of these values (i.e., hours, minutes, seconds). Evaluate your program calculations using different starting times (initial seconds). Be mindful of possible rounding errors, use integers only (15 points).


# 7. Debug the following code which greets a guest and checks if the guest can get on a ride by checking their age and height (10 points) :

name = "Josh
height = 62.4 inches
age = 15

#Greeting :
print(Hello, Name)


# 8. Write code that checks the data types of the following variables and casts them to the proper data type if needed (10 points):

age = 32.4
avgHeight = "73.54"
numOfGuests = 47.0
flightSpeed = "423 miles/hour"
outsideTemp = 73.2