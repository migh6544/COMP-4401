'''
COMP 4401
Homework 2 - Functions & Variable Scope

General Homework Guidelines:
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing.
- Use a consistent coding style.
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs.
- Every function must include a docstring for documentation (see:
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is
- All tests of your functions should be commented out in your final submission or
  enclosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.

Homework 2 Instructions:
You should submit two .py files, this file and a new file you create for problem 6 called : extra_functions.py.
'''
#--------------------------------------------------------------------------#


# 1. Create a function called secondsToHMS that takes an argument `seconds`,
# an integer number of seconds, and returns a string in the format "xx h, xx m, xx s",
# where xx is the number of hours, minutes and seconds. This is turning the question
# from last week's homework into a function. (15 points)

def secondsToHMS(seconds):
	'''
	Convert a given number of seconds into a formatted string representing hours, minutes, and seconds.

	Parameters:
	seconds (int): The number of seconds to be converted.

	Returns:
	str: A string in the format "xx h, xx m, xx s" representing the equivalent hours, minutes, and seconds.
	'''
 
	# Calculating hours from total seconds using floor to avoid floats
	hours = int(seconds // 3600)
	# Calculating seconds remaining from calculated hours
	seconds = int(seconds % 3600)
	# Calculating minutes from remaining seconds using floor to avoid floats
	minutes = int(seconds // 60)
	# Calculating seconds remaining from calculated minutes
	seconds = int(seconds % 60)

    # Return time in hours, minutes,ad seconds as per the required format
	return (f'{hours} h, {minutes} m, {seconds} s')


# 2. Create two functions milesToKm and kmToMiles, each function will take in one
# parameter, distance, of type float. Each function will convert the distance into
# either miles or kilometers based on the function used and return that value.
# (15 points)
# 1 mile = 1.6 kilometers
# 1 kilometer = 0.62 miles


def milesToKm(distanceMiles):
    '''
    Convert a distance in miles to kilometers.

    Parameters:
    distance_miles (float): The distance in miles to be converted.

    Returns:
    float: The equivalent distance in kilometers.
    '''

    # Return distance in KM
    return (round(distanceMiles * 1.6), 1)


def kmToMiles(distanceKM):
    '''
    Convert a distance in kilometers to miles.

    Parameters:
    distance_km (float): The distance in kilometers to be converted.

    Returns:
    float: The equivalent distance in miles.
    '''

    # Return distance in Miles
    return (round(distanceKM * 0.62), 1)


# 3. Create a function called europeUS that takes 2 parameters, sqmToSqft and euroToDollars,
# both of type float. The function must return the coverted values as a tuple: sqft, dollars.
# This will allow us to convert real state listings in Europe, which are in metric, to imperial
# units so we can shop for our next vacation home. (10 points)
# 1 sqm = 10.7639 sqft
# 1 euro = 1.08 dollars

#def function(....):
#	...
#	...
#	return val1, val2
#
#result1, result2 = function(...)

def europeUS(sqmToSqft, euroToDollars):
    '''
    Convert real estate listings from metric units to imperial units.

    Parameters:
    sqmToSqft (float): Conversion factor from square meters to square feet.
    euroToDollars (float): Conversion factor from euros to dollars.

    Returns:
    tuple: A tuple containing the converted values in the order (sqft, dollars).
    '''

    # Convert units from Metric to Imperial
    sqft = (sqmToSqft * 10.7639)
    # Convert units from Euros to USD
    dollars = (euroToDollars * 1.08)

    # Return tuple (Area in SqFt, Cost in USD)
    return (round(sqft, 1), round(dollars, 1))


# 4. Create a function called roadTrip that takes 1 parameter, mpg (miles per gallon), of type float.
# The function should ask for user input on how far they intend to drive on their road trip. Once
# you have the distance, calculate the number of gallons they will need to complete the road trip.
# Use $3.07 as the average cost of a gallon of gas. Return the total cost of gas for the road trip.
# (15 points)

def roadTrip(mpg):
    '''
    Calculate the total cost of gas for a road trip.

    Parameters:
    mpg (float): Miles per gallon (fuel efficiency of the vehicle).

    Returns:
    float: Total cost of gas for the road trip.
    '''

    # Ask the user for the distance of the road trip
    distance = float(input("Enter the distance of your road trip in miles: "))

    # Calculate the number of gallons needed for the road trip
    gallonsNeeded = (distance / mpg)

    # Calculate the total cost of gas based on the average cost per gallon
    gasCost = (gallonsNeeded * 3.07)

    # Return trip's fuel cost
    return (round(gasCost, 1))


# 5. Create a function called insulateHomeCost that takes no parameters and asks the user to input
# the length, width and height of the the basement of their house. Once you have these values,
# calculate the surface area (sq ft) of each side of the basement and use $2.75 as the average cost
# of spray foam insulation per sq ft. Once you have that value multiply. Return the total insulation
# cost. (15 points)

def insulateHomeCost():
    '''
    Calculate the total cost of insulating a home's basement.

    Returns:
    float: Total cost of insulation.
    '''

    # Ask the user for the dimensions of the basement
    length = float(input("Enter the length of the basement (ft): "))
    width = float(input("Enter the width of the basement (ft): "))
    height = float(input("Enter the height of the basement (ft): "))

    # Calculate the surface area of each side of the basement
    areaFloors = (length * width)
    areaWalls = (2 * ((length + width) * height))

    # Calculate the total surface area
    totalArea = (areaFloors + areaWalls)

    # Calculate the total insulation cost based on the average cost per sq-ft
    insulationCost = (totalArea * 2.75)

    # Return the total cost of insulation
    return (round(insulationCost, 1))


# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns
#    the midpoint between that integer and 0.
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of code: midpoint_of_10 = midpoint(10)
# (20 points)

## Import extra_functions.py into this file.
# import extra_functions as ef
## Test the midpoint function from extra_functions.py
# midpoint_of_10 = ef.midpoint(10)
# print(midpoint_of_10)


# 7. Fix the following code (10 points)
def myFunc(height, weight, age):
    '''
    Calculates the Body Mass Index (BMI) based on height, weight, and age.

    Parameters:
    height (float): The height in feet.
    weight (float): The weight in pounds.
    age (int): The age in years.

    Returns:
    tuple: A tuple containing the age (int), the calculated BMI (float), and the classification of the assessment.
    '''

    # Convert height from Feet to Inches
    heightInches = int(height * 12)

    # Calculate BMI using the standard formula
    bmi = (weight / (heightInches ** 2) * 703)

    # Initialize a variable to store BMI classification
    classification = ""

    # Determine BMI classification based on age
    if (bmi < 18.5):
        classification = "Underweight"
    if (bmi >= 18.5 and bmi <= 24.9):
        classification = "Normal"
    if (bmi >= 25 and bmi <= 29.9):
        classification = "Overweight"
    if (bmi >= 30):
        classification = "Obese"

    # Return age, BMI, and classification as a tuple
    return (age, round(bmi, 1), classification)


## Tests:
# print(secondsToHMS(3000))
# print(milesToKm(20))
# print(kmToMiles(15))
# print(europeUS(75, 225))
# print(roadTrip(81))
# print(insulateHomeCost())
# print(myFunc(6.0, 200, 40))