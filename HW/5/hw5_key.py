'''
COMP 4401
Homework 5 - File Input/Output & Exception Handling

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



In this assignment we will be working with a Kaggle dataset 
(https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)
(https://www.kaggle.com/datasets/mirbektoktogaraev/madrid-real-estate-market). 
This is a real state dataset from the Netherlands and Madrid, Spain. The data 
contains 16 columns with 5555 entries and 58 columns with 21.7k entries respectively.
We will be working with a subset of the data split into multiple files. 

Our objective with this data is to import and analyze this data in order to help a family 
member purchace a home in the Netherlands/Madrid. They will be letting us sleep on their 
couch in exchange for this service. A fair trade.
'''
#--------------------------------------------------------------------------#




# 1. Create a function, called inputData, that takes a file name as an argument. 
# The function must handle an exception if the file is not found (this occurs 
# when the file does not exist, if it was misspelled or it's in a different 
# directory). The function must read in the data from the file and return it
# as a list. 
# (15 points)

def inputData(filename):
    '''Reads in a file (expects a file with one column and 
    rows separated by newline characters) then saves each row as an entry in a list
    Input: file name to read
    Returns: list with each row as a list entry'''
    flag = True
    while flag:
        try:
            with open(filename, 'r') as f:
                data = []
                for line in f.readlines():
                    line = line.replace('\n', '')
                    data.append(line)
            flag = False
        except FileNotFoundError as e:
            print(f'That file does not exist. The stack trace message says: {e}')
            filename = input('Input a new file name to try: ')

    return data

# 2. Create a function, called listOfFloats, that takes a list of values and casts
# each value to a float. The function must be able to handle exceptions dealing with
# missing values and values that cannot be cast to a float, i.e. "fdshjksd". The
# function must return a list of floats. Note: you must create an empty list inside 
# the function, and append the casted values to it, then return it. 
# (15 points)

def listOfFloats(myList: list):
    '''Takes a list of values and casts each value to a float
    Removes rows that cannot be cast to a float or that are missing
    input: a list of values
    Returns: new list of floats
    '''
    newList = []
    for val in myList:
        try:
            val = float(val)
            newList.append(val)
        except ValueError as e:
            print(f'skipping {val} because of {e}')
    return newList


# 3. Create a function, called computeAverage, that takes in a list of floats as an 
# argument. All elements in the list must be floats in order to perform any calculations.
# You cannot use any built-in function to compute the average, instead add up all the
# values and divide by the total number of values you have. Return the average (this
# should be a float). 
# (15 points)

def computeAverage(myList: list):
    '''Computes the average of a list of floats
    Input: list of floats
    Returns: Average value in list, as float'''
    runningSum = 0
    runningCount = 0
    for val in myList:
        runningSum += val
        runningCount += 1
    
    if runningCount == 0:
        return 0
    else:
        return runningSum / runningCount

# 4. Create a function, called filteredData, that takes filename and maxPrice as arguments,
# of types string and float respectively. The function should loop over the list and store the
# results that satisfy the maxprice criteria in a new list (amount is <= maxPrice).
# (use : 
# filteredResults = []
# filteredResults.append(filteredDataPoint) to add the data to the new list). 
# Return the list with the new results. The function must handle the exception of getting an 
# incorrect max value, i.e. "bjfdsk". 
# (15 points)

def filteredData(filename, maxPrice):
    '''Reads in data from a file (located at filename) and saves that data as a list. 
    Then selects only the values from the list which are less than
    or equal to some value (maxPrice).

    Inputs: filename (str) and maxPrice (float)
    Returns: new list of filtered data points (list)

    Raises exception if maxPrice is not a valid number. 
    '''
    if type(maxPrice) == int or type(maxPrice) == float:
        rawData = inputData(filename)
        floatData = listOfFloats(rawData)
        filteredData = []
        for val in floatData:
            if val <= maxPrice:
                filteredData.append(val)
    else:
        raise TypeError('maxPrice must be an integer or a float.')

    return filteredData


# 5. Create a function, called realEstateAnalysis, that takes a location, type string. The 
# function must ask the user for the file names for buy prices, living space and rent prices 
# whilst handling the file not found error (there is a clever to do this). 

# The function must ask the user to enter a file name until they entered a valid file name.
# Note: the file names must have the extension .csv to work

# The function must then compute the average buy price, average rent price and average living 
# space. Perform checks on your data as the data may not be very clean (you should expect 
# missing values and negative values. You must deal with them).

# Write the results in a file called : realEstateAnalysis.csv using the following format :
# Location, Avg_buy_price, Avg_rent_price, Avg_sqft

# Note 1: the living space is in square meters, rent and buy prices are in euros, so create
# a second file, helper_functions.py and use our previously defined function to convert sqmt 
# to sqft and euros to dollars (you may need to modify the function to make it work).
# Note 2: You must also use whichever functions created in this homework to accomplish this task.
# Note 3: You will need to call the function twice, once for the data for Madrid and another for
# the Netherlands
# The output for the function should look like this :
# Madrid, 578091.9661429492, 1434.4682101167316, 883.9385353229587
# Netherlands, 602963.3547672321, 3014.7843377841937, 1576.2050598919893
# (40 points)

import HW5_helper_functions as hf

def realEstateAnalysis(location: str):
    '''Based on user input to specify file names, reads in 3 files containing data on:
    - buy prices (in Euros), 
    - living space (in sq meters)
    - rent prices (in Euros)
    Calculates the averages for each file, dropping missing and invalid data.
    Converts those values to dollars and sq feet.
    to a file realEstateAnalysis.csv, writes data in the following format:
    location, avg buy price, avg rent price, avg living space

    Input: location name (as a string)
    Returns: None (since function just writes data to file)
    '''

    # read in buy prices and return the data as a list
    buyPricesFile = input('Enter a file name that contains the buy prices data: ')
    buyPricesData = inputData(buyPricesFile)

    # read in rent prices and return the data as a list
    rentPricesFile = input('Enter a file name that contains the rent prices data: ')
    rentPricesData = inputData(rentPricesFile)

    # read in living space and return the data as a list
    livingSpaceFile = input('Enter a file name that contains the living space data: ')
    livingSpaceData = inputData(livingSpaceFile)

    # convert all data lists to floats
    buyPricesData = listOfFloats(buyPricesData)
    rentPricesData = listOfFloats(rentPricesData)
    livingSpaceData = listOfFloats(livingSpaceData)

    # drop negative numbers from data lists (data errors)
    positiveBuyPrices = []
    for entry in buyPricesData:
        if entry > 0:
            positiveBuyPrices.append(entry)
    positiveRentPrices = []
    for entry in rentPricesData:
        if entry > 0:
            positiveRentPrices.append(entry)
    positiveLivingSpaces = []
    for entry in livingSpaceData:
        if entry > 0:
            positiveLivingSpaces.append(entry)

    # calculate averages
    avgBuyPrice = computeAverage(positiveBuyPrices)
    avgRentPrice = computeAverage(positiveRentPrices)
    avgLivingSpace = computeAverage(positiveLivingSpaces)

    # convert average buy and rent prices from euros to dollars
    avgBuyPrice = hf.eurosToDollars(avgBuyPrice)
    avgRentPrice = hf.eurosToDollars(avgRentPrice)

    # convert average living space from sq meters to sq feet
    avgLivingSpace = hf.sqmToSqft(avgLivingSpace)

    # create a string with results
    results = str(location) + ',' + str(avgBuyPrice) + ',' + str(avgRentPrice) + ',' + str(avgLivingSpace)

    # write results to csv file
    with open('realEstateAnalysis.csv', 'w') as f:
        f.write(results)

 


















