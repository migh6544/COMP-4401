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


# 2. Create a function called brickPath that takes three parameters: wallLength, smallBricks, and largeBricks.
# You want to make a row of bricks that is wallLength inches long with the given length of the small and large 
# bricks. Return 'Possible' if it is possible to make the goal by choosing from the given bricks. Otherwise 
# return 'Not Possible'. Small bricks are 1 unit long and large bricks are 5 units long.

# For example: 
# If wallLength = 8, smallGBricks = 2, largeGBricks = 3 then it’s not possible because there is no way 
# to get 8 inches using the given bricks. 
# On the other hand, wallLength = 7 with smallBricks = 2 and largeBricks = 3 is possible (1 large and 2 small 
# gives you 7). (15 points)


# 3. Write a function, called calcSum, that takes 3 integer values as arguments: a, b and c. The function 
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count 
# towards the sum. You cannot use the built-in method sum().
# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. (10 points)


# 4. Create a function that takes in 4 parameters, intVal, strVal, floatVal, and floatVal2. Check that each 
# parameter is of the corresponding type, int, string, float and float respectively. If their data type does 
# not match these types, cast them to the right data type. Then return all 4 values as a tuple. (10 points)


# 5. Create a function, called change, that takes an input, cash (a float), and determines 
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"


# 6. Create a function, called bottlesOfBeer, that accurately prints the “99 bottles of beer on the wall” song: 
# http://www.99-bottles-of-beer.net/lyrics.html
# Your program should account for changes in plural vs. singular nouns and should count down from 99 to 0. 
# (10 points)


# 7. Check age and height (15 points)

def checkAgeHeight():
	if age (greater than) 12
		print You're old enough to get on the ride")
		if height > 54
			print You can get on the ride. Enjoy")
		else
			print(You're a bit too short, sorry
	else
		print(Too young


# 8. Debug the following code (15 points):
def change Number
	'''
	This function will change a number from int to float or float to int
	
	myNum (int/float): input number
	myType (int/float): the type we want to get back
	
	return
		myNum but with correct type
		
	if myType = int()
		myNum <= float(myNum)
	else
		myNum != int(myNum)
	
	return













