'''
COMP 4401
Homework 6 - Lists & Tuples

General Homework Guidelines:
- Do not use built-in functions
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

# In this assignment we will be working with a Kaggle dataset
# (https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset). This is a real estate
# dataset from the Netherlands. The data contains 16 columns and 5555 entries.

# Our objective with this data is to import and analyze this data in order to help a family
# member purchace a home in the Netherlands. They will be letting us sleep on their couch in
# exchange for this service.



###---------------###
###-----Lists-----###
###---------------###


# 1. Create a function, called importData, that takes the file name as an argument. The function
# must handle an exception when the file is not found (this occurs when the file does not exist,
# if it was misspelled or it's in a different directory). If the exception is raised, the function
# must ask the user to re-enter the file name and check again.
# Repeat this as many times as needed until the data is read in. If the user enters nothing, the
# function should terminate. The function should return the data that was read in, it should be of
# type list, or return an empty list if the user terminated the function.
# The output list should have length 5556
# (10 points)





# 2. Create a function, called castData, that takes in the data read in by the previous function,
# this should be a list of strings. The function should perform the following casts :
# Price --> float
# Lot size (m2) --> float
# Living space size (m2) --> float
# Build year --> int
# The function should return the data after fixing the data types, this should be of type list.
# Be mindful of errors in the data, you will need to handle exceptions !
# Output list should have length 5438.
# (10 points)




# 3. Create a function, called averageValues, that takes in a list. The list contains the price,
# lot size, living space and build year. The function must deal with missing values, keeping
# track of the number of data points collected for each field (required for computing the average),
# and realistic data points for the year built column.
# The function should return a tuple containing the average home price, lot size, living space,
# and build year for all homes. Your output should be :
# (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767)
# (15 points)





# 4. Create a function called filterByValues that takes in a list containing real estate
# information, a minimum price and maximum price, these must be of type list, float and float
# respectively. The function should return the average home price, lot size, living space, and
# build year of all homes that fit between the minimum and maximum home values given.
# Result should be returned as a tuple in the order price, lot size, living space, and build year.

# When function called with minPrice = 100000 and maxPrice = 400000, output should be:
# (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298)
# (15 points)





###----------------###
###-----Tuples-----###
###----------------###


# 5. Write a function, called minMaxTuple, that takes a list of numbers and returns
# the smallest element and the largest element as a tuple (smallest, largest). Cannot
# use the built-in functions min()/max().
# For example : lst = [6, 3, 8, 23, -4, 35] should return (-4, 35)
# (10 points)
import math



# 6. Write a function, called allPairs, that takes two lists as paramters, x and y,
# and returns a new list containing all possible pairs consisting of one element from
# x and one element from y as long as they are not the same. Cannot use built-in
# functions or sets.
# For example: If the list x = [1, 4, 6, 8] and y = [5, 2, 6] then the result is the list
# [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)].
# Note that (6, 6) doesn't appear because they are the same element.
# (15 points)





# 7. Write a function, called removeDups, that takes a list of tuples and removes any
# duplicate tuples and returns the modified list. Cannot use built-in functions nor
# sets.
# For example if the list contains [(1, 2), (1, 4, 5), (1, 2), (3, 5)] then the list
# will become [(1, 2), (1, 4, 5), (3, 5)].
# (10 points)




# 8. Create a function, called resultTuples, which takes a location as an argument, this
# should be of type str. The function will create namedtuples named realEstate. Each
# namedtuple should have the fields :
# Location, CheapestBuyPrice, AvgBuyPrice and MostExpBuy.
# To create each tuple you will need to make function calls to our previously defined
# functions in this homework. Also keep in mind that  The function must return the namedtuple created.

# Note1: You will also need to convert the units from sqmt to sqft and euros to
# dollars using the functions from previous homeworks.
# Note2: You will need to place those functions in the extra_functions.py file and
# import them to use them as we've done in the past.
# Note3: You may need to modify our previously used functions so they work with our
# data.

# Output should look like this :
# (the location can change, I used Madrid as an example, numerical values are correct) :
# realEstate(Location='Madrid', CheapestPrice=149000.0, AvgPrice=557707.7581831556, MostExp=4700000.0)
# (15 points)

from collections import namedtuple








