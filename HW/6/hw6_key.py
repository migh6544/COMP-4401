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

def importData(filename: str):
  """
  reads in a file name (handling the case where the file is not found) and saves data to list
  with each entry in list representing one row of the data
  input: filename (str) where data is located
  returns: list containing data
  """
  flag = True
    
  while flag:
    if filename == '':
      return []
    else:
      try:
        with open(filename, 'r') as f:
          data = f.readlines()
        flag = False
      except FileNotFoundError as e:
        print(f'Invalid file name. The stack trace message reads: {e}')
        filename = input('Re-enter the filename: ')

  return data

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

def castData(inputList: list):
  """
  converts price column to float, lot size to float, living space to float, build year to int
  input: inputList, a list of strings with the expected format of 4 columns, 
        price, lot size, living space, and build year, separated by commas
  returns: outputList, a list of lists with columns split on commas, each entry with the corrected data types
  """
  outputList = []

  for row in inputList:
    price, lotSize, livingSpace, buildYear = row.strip('\n').split(',')

    try:
      price = float(price) # price
    except:
      price = ''

    try:
      lotSize = float(lotSize) # lot size
    except:
      lotSize = ''

    try:
      livingSpace = float(livingSpace) # living space
    except:
      livingSpace = ''
    
    try:
      buildYear = int(buildYear) # build year
    except:
      buildYear = ''

    # append all rows with at least one column of valid data to output list
    if price == lotSize == livingSpace == buildYear == '':
      pass
    else:
      outputList.append([price, lotSize, livingSpace, buildYear]) 

    # also valid option to remove rows with any missing data, which would look like:
    # if price != '' or lotSize = '' or livingSpace = '' or buildYear = '':
    #  pass
    # else:
    #  outputList.append([price, lotSize, livingSpace, buildYear]) 

  return outputList


# 3. Create a function, called averageValues, that takes in a list. The list contains the price,
# lot size, living space and build year. The function must deal with missing values, keeping 
# track of the number of data points collected for each field (required for computing the average),
# and realistic data points for the year built column.
# The function should return a tuple containing the average home price, lot size, living space, 
# and build year for all homes. Your output should be :
# (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767)
# (15 points)

def averageValues(inputList: list):
  """
  input: list of lists, where each sublist contains price, lot size, living space, and build year
  returns: tuple containing average home price, lot size, living space, and build year
  """
  priceSum = 0
  priceCount = 0
  lotSizeSum = 0
  lotSizeCount = 0
  livingSpaceSum = 0
  livingSpaceCount = 0
  buildYearSum = 0
  buildYearCount = 0

  for price, lotSize, livingSpace, buildYear in inputList:
    if type(price) == float:
      priceSum += price
      priceCount += 1
    if type(lotSize) == float:
      lotSizeSum += lotSize
      lotSizeCount += 1
    if type(livingSpace) == float:
      livingSpaceSum += livingSpace
      livingSpaceCount += 1
    if type(buildYear) == int and buildYear <= 2023:
      buildYearSum += buildYear
      buildYearCount += 1
  
  priceAvg = priceSum / priceCount if priceCount > 0 else 0
  lotSizeAvg = lotSizeSum / lotSizeCount if lotSizeCount > 0 else 0
  livingSpaceAvg = livingSpaceSum / livingSpaceCount if livingSpaceCount > 0 else 0
  buildYearAvg = buildYearSum / buildYearCount if buildYearCount > 0 else 0

  return (priceAvg, lotSizeAvg, livingSpaceAvg, buildYearAvg)



# 4. Create a function called filterByValues that takes in a list containing real estate 
# information, a minimum price and maximum price, these must be of type list, float and float 
# respectively. The function should return the average home price, lot size, living space, and 
# build year of all homes that fit between the minimum and maximum home values given. 
# Result should be returned as a tuple in the order price, lot size, living space, and build year.

# When function called with minPrice = 100000 and maxPrice = 400000, output should be:
# (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) 
# (15 points)

def filterByValues(inputList: list, minPrice: float, maxPrice: float):
  """
  input: 
   - inputList: real estate data as a a list of lists, with sublist including price, lot size, living space, and build year
   - min price (float)
   - max price (float)
  filters data to only rows where the price is between max and min, then averages each column
  returns: tuple with avg price, lot size, living space, build year
  """

  inputList = castData(inputList)
  filteredList = []

  for entry in inputList:
    if entry[0] >= minPrice and entry[0] <= maxPrice:
      filteredList.append(entry)
  
  return averageValues(filteredList)


###----------------###
###-----Tuples-----###
###----------------###


# 5. Write a function, called minMaxTuple, that takes a list of numbers and returns 
# the smallest element and the largest element as a tuple (smallest, largest). Cannot 
# use the built-in functions min()/max().
# For example : lst = [6, 3, 8, 23, -4, 35] should return (-4, 35) 
# (10 points)

def minMaxTuple(numList: list):
  """
  input: list of numbers
  finds smallest and largest elements in list
  returns: tuple with (smallest, largest)
  """

  if len(numList) == 0:
    return (None, None)
  
  # needed in case list only contains 1 number, in which case max and min is the same
  min = numList[0]
  max = numList[0]

  for num in numList:
    if num < min:
      min = num
    elif num > max:
      max = num
  
  return (min, max)


# 6. Write a function, called allPairs, that takes two lists as paramters, x and y, 
# and returns a new list containing all possible pairs consisting of one element from 
# x and one element from y as long as they are not the same. Cannot use built-in 
# functions or sets.
# For example: If the list x = [1, 4, 6, 8] and y = [5, 2, 6] then the result is the list 
# [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)]. 
# Note that (6, 6) doesn't appear because they are the same element. 
# (15 points)

def allPairs(x: list, y: list):
  """
  input: two lists, x and y
  calculates all possible pairs consisting of one element from x and one element from y,
  as long as the two elements are not the same
  returns: list of tuples consisting of pairs of elements
  """
  resultList = []

  for element in x:
    for element2 in y:
      if element != element2:
        resultList.append((element, element2))

# 7. Write a function, called removeDups, that takes a list of tuples and removes any 
# duplicate tuples and returns the modified list. Cannot use built-in functions nor 
# sets.
# For example if the list contains [(1, 2), (1, 4, 5), (1, 2), (3, 5)] then the list 
# will become [(1, 2), (1, 4, 5), (3, 5)]. 
# (10 points)

def removeDups(listOfTuples: list):
  """
  input: list of tuples
  removes any duplicate tuples from original lsit
  returns: list of tuples with duplicates removed
  """
  newList = []
  for entry in listOfTuples:
    if entry not in newList:
      newList.append(entry)

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
import HW6_extra_functions as ef

def resultTuples(location: str):
  """
  input: location, a string
  creates named tuples called realEstate with fields Location, CheapestBuyPrice, AvgBuyPrice, MostExpBuy
  imports data from a file (file path must be specified by user as input) in order to calculate those values
  converts units from euors to dollars
  returns: named tuple
  """

  # import and clean data
  filename = input('Enter a filename where your real estate data is stored: ')
  data = importData(filename)
  data = castData(data)

  # get average buy price
  avgPrice = averageValues(data)[0]

  # create list of only prices
  prices = []
  for price, _, _, _ in data:
    prices.append(price)
  minPrice, maxPrice = minMaxTuple(prices)

  # create named tuple
  realEstate = namedtuple('realEstate', ['Location', 'CheapestBuyPrice', 'AvgBuyPrice', 'MostExpBuy'])

  # convert units
  minPrice = ef.eurosToDollars(minPrice)
  avgPrice = ef.eurosToDollars(avgPrice)
  maxPrice = ef.eurosToDollars(maxPrice)

  # return named tuple with real estate info
  return realEstate(location, minPrice, avgPrice, maxPrice)








