### START:

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


def distanceConversion(distance: float, unit: str) -> float:
    """
    Convert the provided distance based on the specified unit type.

    Parameters:
    - distance (float): The distance value to be converted.
    - unit (str): The unit type of the provided distance. Can be either "metric" (for kilometers) or "imperial" (for miles).

    Returns:
    - float: The converted distance value. If the unit is "metric", the return value is in miles. If the unit is "imperial", the return value is in kilometers.
    """

    if unit == "metric":
        # Convert kilometers to miles
        return (distance * 0.62)
    elif unit == "imperial":
        # Convert miles to kilometers
        return (distance * 1.6)
    else:
        return None


# 2. Create a function called brickPath that takes three parameters: wallLength, smallBricks, and largeBricks.
# You want to make a row of bricks that is wallLength inches long with the given length of the small and large
# bricks. Return 'Possible' if it is possible to make the goal by choosing from the given bricks. Otherwise
# return 'Not Possible'. Small bricks are 1 unit long and large bricks are 5 units long.

# For example:
# If wallLength = 8, smallGBricks = 2, largeGBricks = 3 then it’s not possible because there is no way
# to get 8 inches using the given bricks.
# On the other hand, wallLength = 7 with smallBricks = 2 and largeBricks = 3 is possible (1 large and 2 small
# gives you 7). (15 points)

def brickPath(wallLength: int, smallBricks: int, largeBricks: int) -> str:
    """
    Determines if it's possible to create a wall of the specified length using the given number of small and large bricks.

    Parameters:
    - wallLength (int): The total length of the wall you want to build.
    - smallBricks (int): The number of small bricks available (1 unit each).
    - largeBricks (int): The number of large bricks available (5 units each).

    Returns:
    - str: 'Possible' if the wall can be built with the given bricks, 'Not Possible' otherwise.
    """

    # Using as many large bricks as we can without exceeding wallLength
    maxLargeBricksNeeded = (wallLength // 5)
    largeBricksUsed = min(largeBricks, maxLargeBricksNeeded)
    # Calculating the remaining length after using the large bricks
    remainingLength = (wallLength - largeBricksUsed * 5)

    # Check if we have enough small bricks to cover the remaining length
    if remainingLength <= smallBricks:
        return ('Possible')
    return ('Not Possible')


# 3. Write a function, called calcSum, that takes 3 integer values as arguments: a, b and c. The function
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count
# towards the sum. You cannot use the built-in method sum().
# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. (10 points)

def calcSum(a: int, b: int, c: int) -> int:
    """
    Calculates the sum of three integers. If one of the integers is a duplicate, it doesn't count towards the sum.

    Parameters:
    - a (int): First integer value.
    - b (int): Second integer value.
    - c (int): Third integer value.

    Returns:
    - int: The sum of the three integers, excluding duplicates.
    """

    # If all three numbers are the same, return any one of them.
    if a == b == c:
        return a

    # If two numbers are the same, return the sum of the third number and one of the duplicates.
    if a == b:
        return (a + c)
    if a == c:
        return (a + b)
    if b == c:
        return (b + a)

    # If all numbers are unique, return their total sum.
    return (a + b + c)


# 4. Create a function that takes in 4 parameters, intVal, strVal, floatVal, and floatVal2. Check that each
# parameter is of the corresponding type, int, string, float and float respectively. If their data type does
# not match these types, cast them to the right data type. Then return all 4 values as a tuple. (10 points)

def ensureTypes(intVal, strVal, floatVal, floatVal2):
    """
    Checks the type of each parameter and casts them to the required type if necessary.

    Parameters:
    - intVal: Value expected to be of type int.
    - strVal: Value expected to be of type string.
    - floatVal: Value expected to be of type float.
    - floatVal2: Value expected to be of type float.

    Returns:
    - tuple: A tuple containing the four values, possibly casted to the correct type.
    """

    # Ensure intVal is of type int, else cast it
    if type(intVal) != int:
        intVal = int(intVal)

    # Ensure strVal is of type string, else cast it
    if type(strVal) != str:
        strVal = str(strVal)

    # Ensure floatVal is of type float, else cast it
    if type(floatVal) != float:
        floatVal = float(floatVal)

    # Ensure floatVal2 is of type float, else cast it
    if type(floatVal2) != float:
        floatVal2 = float(floatVal2)

    return (intVal, strVal, floatVal, floatVal2)


# 5. Create a function, called change, that takes an input, cash (a float), and determines
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"

def change(cash: float) -> str:
    """
    Determines the least number of dollar bills and coins needed for the given cash amount.

    Parameters:
    - cash (float): The amount of cash for which to provide change.

    Returns:
    - str: A string describing the number of each bill and coin needed.
    """

    # Define available bills and their respective names
    bills = [100, 50, 20, 10, 5, 1]
    billNames = ["$100 bill", "$50 bill",
                 "$20 bill", "$10 bill", "$5 bill", "$1 bill"]

    # Define available coins and their respective names
    coins = [0.25, 0.10, 0.05, 0.01]
    coinNames = ["quarter", "dime", "nickel", "penny"]

    # Initialize an empty string to store the result
    resultStr = ""

    # Loop over each bill type to determine how many of each are needed
    for i in range(len(bills)):
        bill = bills[i]
        # Determine how many of the current bill are needed
        count = int(cash // bill)
        # If the current bill is needed, append its count to the result string
        if count:
            # If result string is not empty, append a comma for formatting
            if resultStr:
                resultStr += (", ")
            # Determine if plural is needed
            plural = ("s") if (count > 1) else ("")
            # Add the bill count and type to the result string
            resultStr += (f"{count} x {billNames[i]}{plural}")
        # Subtract the value of the bills used from the total
        cash -= (count * bill)

    # Convert the remaining cash to cents for calculation ease
    cash = round(cash * 100)

    # Loop over each coin type to determine how many of each are needed
    for i in range(len(coins)):
        coin = coins[i]
        # Determine how many of the current coin are needed
        count = int(cash // (coin * 100))
        # If the current coin is needed, append its count to the result string
        if count:
            # If result string is not empty, append a comma for formatting
            if resultStr:
                resultStr += (", ")

            # Determine if "penny" should be plural
            if (coinNames[i] == "penny"):
                plural = ("ies") if (count > 1) else ("y")
            else:
                plural = ("s") if (count > 1) else ("")
            # Add the coin count and type to the result string without using rstrip
            coinName = coinNames[i] if coinNames[i] != ("penny") else ("penn")
            resultStr += (f"{count} {coinName}{plural}")

        # Subtract the value of the coins used from the total
        cash -= (count * (coin * 100))

    # Return the result string
    return (resultStr + ".")


# 6. Create a function, called bottlesOfBeer, that accurately prints the “99 bottles of beer on the wall” song:
# http://www.99-bottles-of-beer.net/lyrics.html
# Your program should account for changes in plural vs. singular nouns and should count down from 99 to 0.
# (10 points)

def bottlesOfBeer():
    """
    Prints the lyrics of the "99 bottles of beer on the wall" song.

    The song accounts for changes in plural vs. singular nouns and counts down from 99 to no bottles.

    Parameters:
    - None

    Returns:
    - None
    """

    # Begin the loop to iterate from 99 bottles down to 0
    for i in range(99, -1, -1):

        # For counts of bottles greater than 1
        if i > 1:
            # Print the current number of bottles on the wall and taken down
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            # Print the action of taking one down and the remaining number of bottles
            print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")

        # For the count of a single bottle
        elif i == 1:
            # Print that there's only one bottle left on the wall
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            # Print the action of taking the last bottle down
            print(f"Take one down, pass it around, no more bottles of beer on the wall.\n")

        # For when there are no more bottles left
        else:
            # Print that there are no more bottles on the wall
            print("No more bottles of beer on the wall, no more bottles of beer.")
            # Print the suggestion to buy some more bottles
            print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")


# 7. Check age and height (15 points)

def checkAgeHeight(age: int, height: int):
    """
    Checks if a person is old enough and tall enough to get on a ride.

    Parameters:
    - age (int): Age of the person.
    - height (int): Height of the person in inches.

    Returns:
    - None
    """

    # Check if age is greater than 12
    if age > 12:
        print("You're old enough to get on the ride.")

        # Nested check for height
        if height > 54:
            print("You can get on the ride. Enjoy!")
        else:
            print("You're a bit too short, sorry.")
    else:
        print("Too young.")


# 8. Debug the following code (15 points):
def changeNumber(myNum, myType):
    """
    Changes a number from int to float or float to int.

    Parameters:
    - myNum: The input number. Can be of type int or float.
    - myType: The type we want to get back. Can be int or float.

    Returns:
    - myNum but with the correct type.
    """

    # Check if the desired type is int
    if myType == int:
        return int(myNum)
    else:
        return float(myNum)


def main():
    """
    The main function serves to test all the previously defined functions in the script.
    The functions being tested include:

    - distanceConversion: Converts distances between kilometers and miles.
    - brickPath: Determines the feasibility of constructing a wall with given bricks.
    - calcSum: Computes the sum of three integers, excluding any duplicates.
    - ensure_types: Ensures and casts the data types of four parameters to their expected types.
    - change: Determines the least number of dollar bills and coins needed for a given cash amount.
    - bottlesOfBeer: Prints the lyrics of the "99 bottles of beer on the wall" song.
    - checkAgeHeight: Checks if a person meets age and height criteria for a ride.
    - changeNumber: Converts an input number from its current type (int or float) to the desired type (int or float).
    
    Parameters:
    - None

    Returns:
    - None

    Outputs:
    - Prints the results of each test, which includes computed values and strings based on input scenarios.
    """

    # Test distanceConversion function
    # Expected output: 62.0
    print(distanceConversion(100, "metric"))
    # Expected output: 160.0
    print(distanceConversion(100, "imperial"))

    # Test brickPath function
    # Expected output: 'Possible'
    print(brickPath(23, 3, 4))
    # Expected output: 'Not Possible'
    print(brickPath(8, 2, 3))

    # Test calcSum function
    # Expected output: 7
    print(calcSum(2, 2, 5))

    # Test ensure_types function
    # Expected output: (1, '1', 3.5, 4.2)
    print(ensureTypes('1', 1.0, '3.5', '4.2'))

    # Test change function
    # Expected output: "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies."
    print(change(35.63))

    # Test bottlesOfBeer function
    bottlesOfBeer()

    # Test checkAgeHeight function
    # Expected output: "You're old enough to get on the ride.", "You can get on the ride. Enjoy!"
    checkAgeHeight(13, 55)
    # Expected output: "Too young."
    checkAgeHeight(11, 55)

    # Test changeNumber function
    # Expected output: 5.0
    print(changeNumber(5, float))
    # Expected output: 5
    print(changeNumber(5.5, int))


if __name__ == "__main__":
    main()
### END.
