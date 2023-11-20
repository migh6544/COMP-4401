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
	"""takes a number of seconds as input and returns a string that list the
	number of hours, minutes, and seconds this converts to"""

	hours = seconds // 3600
	minutes = (seconds % 3600) // 60
	remaining_seconds = (seconds % 3600) % 60

	return str(hours) + 'h, ' + str(minutes) + ' m, ' + str(remaining_seconds) + ' s'

# 2. Create two functions milesToKm and kmToMiles, each function will take in one 
# parameter, distance, of type float. Each function will convert the distance into 
# either miles or kilometers based on the function used and return that value. 
# (15 points)
# 1 mile = 1.6 kilometers
# 1 kilometer = 0.62 miles

def milesToKm(distance: float):
	"""takes distance parameter, a float, in miles as input and
	returns distance in kilometers as a float"""

	return distance * 1.6

def kmToMiles(distance: float):
	"""takes distance parameter, a float, in kilometers as input
	and returns distance in miles as a float"""

	return distance * 0.62

# optional code to test our functions
if __name__ == '__main__':
	dist_in_miles = kmToMiles(10)
	print(dist_in_miles)


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


def europeUS(sqmToSqft: float, euroToDollars: float):
	"""takes 2 float parameters, representing square meters of a real estate listing and its price in euros
	converts these numbers into square feet and dollars
	returns a tuple with square feet and dollars"""

	sqft = sqmToSqft * 10.7639
	dollars = euroToDollars * 1.08
	return sqft, dollars

# 4. Create a function called roadTrip that takes 1 parameter, mpg (miles per gallon), of type float. 
# The function should ask for user input on how far they intend to drive on their road trip. Once 
# you have the distance, calculate the number of gallons they will need to complete the road trip. 
# Use $3.07 as the average cost of a gallon of gas. Return the total cost of gas for the road trip. 
# (15 points)

def roadTrip(mpg: float):
	"""prompts for user input on how far the user intends to drive on their road trip
	using that distance, the function calculates number of gallons needed
	and returns the total cost of gas for the road trip as a float"""

	distance = float(input('How long do you plan to drive on your roadtrip: '))
	cost = (distance / mpg) * 3.07
	return cost

# 5. Create a function called insulateHomeCost that takes no parameters and asks the user to input 
# the length, width and height of the the basement of their house. Once you have these values,
# calculate the surface area (sq ft) of each side of the basement and use $2.75 as the average cost 
# of spray foam insulation per sq ft. Once you have that value multiply. Return the total insulation 
# cost. (15 points)

def insulateHomeCost():
	"""no input needed, function asks for user input on the length, width, and height of the basement
	of their house then returns the total cost to insulate all the walls, using $2.75 as cost per sqft"""

	length = float(input('What is the length of your basement?: '))
	width = float(input('What is the width of your basement?: '))
	height = float(input('What is the height of your basement?: '))

	long_sides = length * height * 2
	wide_sides = width * height * 2
	total_surface_area = long_sides + wide_sides
	
	return total_surface_area * 2.75
	

# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns 
#    the midpoint between that integer and 0.
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of code: midpoint_of_10 = midpoint(10)
# (20 points)

# import midpoint function from extra_functions_key
from extra_functions_key import midpoint

# invoke midpoint function
midpoint_of_10 = midpoint(10)

# 7. Fix the following code (10 points)

def myFunc(height, weight, age):
	"""
	This function performs some mathematical operations on heigh, weight, and age.
	
	inputs are:
	height in feet (a float)
	weight in lbs (a float)
	age in years (an int)
	
	function returns three float values:
	height times age
	height in inches
	weight divided by height squared times 703
	
	"""
	
	temp = height * age
	temp2 = height * 12
	temp3 = weight / height**2 * 703
	
	return temp, temp2, temp3
	
	
	
	


