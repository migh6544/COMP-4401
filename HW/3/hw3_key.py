'''
COMP 4401
Homework 3 - Control Flow Statements

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
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''
#--------------------------------------------------------------------------#

# 1. Create a function distanceConversion that takes in two parameters, distance and unit, 
# of types float and string respectively. Based on the unit type, "metric" or "imperial", it 
# will convert distance into miles or kilometers. This is creating a single function from 
# milesToKm and kmToMiles in the last homework. (10 points)

def distanceConversion(distance: float, unit: str):
	"""Takes in 2 arguments, distance (a float) and unit (either 'metric' or 'imperial')
	converts distance to the appropriate opposite type of units then returns that value"""

	if unit == 'metric':
		return distance * 0.62
	elif unit == 'imperial':
		return distance * 1.6


# 2. Create a function called brickPath that takes three parameters: wallLength, smallBricks, and largeBricks.
# You want to make a row of bricks that is wallLength inches long with the given length of the small and large 
# bricks. Return 'Possible' if it is possible to make the goal by choosing from the given bricks. Otherwise 
# return 'Not Possible'. Small bricks are 1 unit long and large bricks are 5 units long.

# For example: 
# If wallLength = 8, smallGBricks = 2, largeGBricks = 3 then it’s not possible because there is no way 
# to get 8 inches using the given bricks. 
# On the other hand, wallLength = 7 with smallBricks = 2 and largeBricks = 3 is possible (1 large and 2 small 
# gives you 7). (15 points)

def brickPath(wallLength: int, smallBricks: int, largeBricks: int):
	"""
	Function hecks if it's possible to build a wall of exactly the specified length with the provided numbers of bricks
	Note: small bricks are 1 unit long and large bricks are 5 units long
	Inputs: wallLength, smallBricks, and largeBricks (all ints)
	Returns: Possible or Not Possible
	"""

	if (wallLength <= smallBricks + 5 * largeBricks) and (wallLength % 5 <= smallBricks):
		return "Possible"
	else:
		return "Not Possible"


# 3. Write a function, called calcSum, that takes 3 integer values as arguments: a, b and c. The function 
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count 
# towards the sum. You cannot use the built-in method sum().
# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. (10 points)

def calcSum(a: int, b: int, c: int):
	"""
	Returns the sum of 3 integers, not counting any duplicates more than once.
	Inputs: a, b, c (all ints)
	Returns: sum of ints (an int), not counting duplicates multiple times
	"""
	if a == b == c:
		return a
	elif a == b:
		return a + c
	elif a == c:
		return a + b
	elif b == c:
		return a + b
	else:
		return a + b + c

# 4. Create a function that takes in 4 parameters, intVal, strVal, floatVal, and floatVal2. Check that each 
# parameter is of the corresponding type, int, string, float and float respectively. If their data type does 
# not match these types, cast them to the right data type. Then return all 4 values as a tuple. (10 points)

def checkTypes(intVal, strVal, floatVal, floatVal2):
	"""checks if 1st input is int, 2nd input is str, 3rd input is float, 4th input is float
	if not, casts them to the right type
	Inputs: 4 values, intVal (must be an int or castable to int), strVal (must be string or castable to string), 
	floatVal, and floatVal2 (both must be floats or castable to floats)
	Returns: all corrected values as a tuple"""

	if type(intVal) != int:
		intVal = int(intVal)
	if type(strVal) != str:
		strVal = str(strVal)
	if type(floatVal) != float:
		floatVal = float(floatVal)
	if type(floatVal2) != float:
		floatVal2 = float(floatVal2)

	return intVal, strVal, floatVal, floatVal2



# 5. Create a function, called change, that takes an input, cash (a float), and determines 
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"

def change(cash: float):
	"""
	Makes change with from a starting cash value using the fewest number of dollar bills and coins possible 
	Input: cash, a float
	Returns: a string describing the change that will be provided
	"""

	current_cash = cash

	bills_100 = int(current_cash // 100)
	current_cash -= bills_100 * 100

	bills_50 = int(current_cash // 50)
	current_cash -= bills_50 * 50

	bills_20 = int(current_cash // 20)
	current_cash -= bills_20 * 20

	bills_10 = int(current_cash // 10)
	current_cash -= bills_10 * 10

	bills_5 = int(current_cash // 5)
	current_cash -= bills_5 * 5

	bills_1 = int(current_cash // 1)
	current_cash -= bills_1 * 1

	coins_25 = int((current_cash * 100) // 25)
	current_cash -= coins_25 * .25

	coins_10 = int((current_cash * 100) // 10)
	current_cash -= coins_10 * .1

	coins_5 = int((current_cash * 100) // 5)
	current_cash -= coins_5 * .05

	coins_1 = int(current_cash * 100)

	result = ''
	if bills_100 == 1:
		result += f'{bills_100} x $100 bill'
	elif bills_100 >= 2:
		result += f', {bills_100} x $100 bills'
	
	if result != '' and bills_50 >= 1:
		result += ', '
	if bills_50 == 1:
		result += f'{bills_50} x $50 bill'
	elif bills_50 >= 2:
		result += f'{bills_50} x $50 bills'
	
	if result != '' and bills_20 >= 1:
		result += ', '
	if bills_20 == 1:
		result += f'{bills_20} x $20 bill'
	elif bills_20 >= 2:
		result += f'{bills_20} x $20 bills'
	
	if result != '' and bills_10 >= 1:
		result += ', '
	if bills_10 == 1:
		result += f'{bills_10} x $10 bill'
	elif bills_10 >= 2:
		result += f'{bills_10} x $10 bills'
	
	if result != '' and bills_5 >= 1:
		result += ', '
	if bills_5 == 1:
		result += f'{bills_5} x $5 bill'
	elif bills_5 >= 2:
		result += f'{bills_5} x $5 bills'

	if result != '' and bills_1 >= 1:
		result += ', '
	if bills_1 == 1:
		result += f'{bills_1} x $1 bill'
	elif bills_1 >= 2:
		result += f'{bills_1} x $1 bills'
	
	if result != '' and coins_25 >= 1:
		result += ', '
	if coins_25 == 1:
		result += f'{coins_25} quarter'
	elif coins_25 >= 2:
		result += f'{coins_25} quarters'
	
	if result != '' and coins_10 >= 1:
		result += ', '
	if coins_10 == 1:
		result += f'{coins_10} dime'
	elif coins_10 >= 2:
		result += f'{coins_10} dimes'

	if result != '' and coins_5 >= 1:
		result += ', '
	if coins_5 == 1:
		result += f'{coins_5} nickel'
	elif coins_5 >= 2:
		result += f'{coins_5} nickels'

	if result != '' and coins_1 >= 1:
		result += ', '
	if coins_1 == 1:
		result += f'{coins_1} penny'
	elif coins_1 >= 2:
		result += f'{coins_1} pennies'
	
	return result

# 6. Create a function, called bottlesOfBeer, that accurately prints the “99 bottles of beer on the wall” song: 
# http://www.99-bottles-of-beer.net/lyrics.html
# Your program should account for changes in plural vs. singular nouns and should count down from 99 to 0. 
# (10 points)

def bottlesOfBeer():
	"""Prints 99 bottles of beer on the wall song. No inputs and nothing returned."""
	for bottle_num in range(99, 0):
		if bottle_num > 2:
			print(f'{bottle_num} bottles of beer on the wall, {bottle_num} bottles of beer.')
			print(f'Take one down and pass it around, {bottle_num - 1} bottles of beer on the wall.')
			print('')
		elif bottle_num == 2:
			print(f'{bottle_num} bottles of beer on the wall, {bottle_num} bottles of beer.')
			print(f'Take one down and pass it around, {bottle_num - 1} bottle of beer on the wall.')
			print('')
		elif bottle_num == 1:
			print(f'{bottle_num} bottle of beer on the wall, {bottle_num} bottle of beer.')
			print(f'Take one down and pass it around, no more bottles of beer on the wall.')
			print('')
			print('No more bottles of beer on the wall, no more bottles of beer.')
			print('Go to the store and buy some more, 99 bottles of beer on the wall.')


# 7. Check age and height (15 points)

def checkAgeHeight(age, height_inches):
	"""
	Inputs: age in years (an int or float), height in inches (an int or float)
	Checks if someone is old enough and tall enough to get on a ride and prints a message 
	about the results
	returns: None
	"""
	if age > 12:
		print("You're old enough to get on the ride.")
		if height_inches > 54:
			print("You can get on the ride. Enjoy!")
		else:
			print("You're a bit too short, sorry.")
	else:
		print("Too young.")


# 8. Debug the following code (15 points):

def changeNumber(myNum, myType):
	'''
	This function will change a number from int to float or float to int
	
	inputs:
	myNum (a value already an int or float): input number
	myType (a data type, int or float): the data type we want to get back
	
	returns myNum but with correct type
	'''
		
	if myType == int:
		myNum = int(myNum)
	elif myType == float:
		myNum = float(myNum)
	
	return myNum













