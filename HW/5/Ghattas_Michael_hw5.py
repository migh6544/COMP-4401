## START:

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

def inputData(fileName):
    """
    Read data from the specified file and return it as a list.

    Parameters:
    - fileName (str): The name (or path) of the file to be read.

    Returns:
    - list: A list of lines from the file.

    Raises:
    - FileNotFoundError: If the file does not exist, was misspelled, or is in a different directory.
    """

    # Initialize an empty list to store the lines from the file
    lines = []

    try:
        # Attempt to open and read the file
        with open(fileName, 'r') as file:
            # Read each line from the file and append it to the list
            for line in file:
                # strip() is used to remove trailing and leading whitespace including newline characters
                lines.append(line.strip())

    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"Error: The file '{fileName}' was not found.")

    return lines


# 2. Create a function, called listOfFloats, that takes a list of values and casts
# each value to a float. The function must be able to handle exceptions dealing with
# missing values and values that cannot be cast to a float, i.e. "fdshjksd". The
# function must return a list of floats. Note: you must create an empty list inside
# the function, and append the casted values to it, then return it.
# (15 points)

def listOfFloats(values):
    """
    Cast each value in the provided list to a float and return a new list of floats.

    Parameters:
    - values (list): A list of values to be cast to floats.

    Returns:
    - list: A list containing the values successfully cast to floats.
            Values that cannot be cast, are missing, or are negative will be ignored.
    """

    # Initialize an empty list to store the casted float values
    floatValues = []

    for value in values:
        # Check if the value is an empty string (missing value)
        if value == "":
            print("Error: Missing value detected and skipped.")
            continue

        try:
            # Attempt to cast the value to a float
            floatValue = float(value)

            # If the value is negative, print a message and continue to the next iteration
            if floatValue < 0:
                print(f"Warning: Negative value '{floatValue}' detected and skipped.")
                continue

            floatValues.append(floatValue)

        except ValueError:
            # Handle exceptions for values that cannot be cast to a float
            print(f"Error: The value '{value}' cannot be cast to a float.")

    return floatValues


# 3. Create a function, called computeAverage, that takes in a list of floats as an
# argument. All elements in the list must be floats in order to perform any calculations.
# You cannot use any built-in function to compute the average, instead add up all the
# values and divide by the total number of values you have. Return the average (this
# should be a float).
# (15 points)

def computeAverage(floatList):
    """
    Compute the average of a list of floats.

    Parameters:
    - floatList (list): A list of float values.

    Returns:
    - float: The average of the values in the list.

    Raises:
    - TypeError: If an element in the list is not a float.
    """

    # Initialize the sum to 0
    totalSum = 0.0

    # For each value in the list
    for value in floatList:
        # Check if the value is a float by comparing its type
        if type(value) != float:
            raise TypeError(f"Error: Expected a float value, but got {type(value)} with value '{value}'")

        # Add the float value to the total sum
        totalSum += value

    # Divide the total sum by the number of values to get the average
    average = (totalSum / len(floatList))

    return average


# 4. Create a function, called filteredData, that takes filename and maxPrice as arguments,
# of types string and float respectively. The function should loop over the list and store the
# results that satisfy the maxprice criteria in a new list (amount is <= maxPrice).
# (use :
# filteredResults = []
# filteredResults.append(filteredDataPoint) to add the data to the new list).
# Return the list with the new results. The function must handle the exception of getting an
# incorrect max value, i.e. "bjfdsk".
# (15 points)

def filteredData(fileName, maxPrice):
    """
    Filter data from a file based on a maximum price criteria.

    Parameters:
    - fileName (str): The name (or path) of the file to be read.
    - maxPrice (float): The maximum price criteria for filtering.

    Returns:
    - list: A list containing the filtered data points based on the maxPrice criteria.

    Raises:
    - FileNotFoundError: If the file does not exist, was misspelled, or is in a different directory.
    - ValueError: If an incorrect maxPrice value is provided.
    """

    # Check if the maxPrice value is a float
    if type(maxPrice) != float:
        raise ValueError(f"Error: Expected a float value for maxPrice, but got {type(maxPrice)} with value '{maxPrice}'")

    # Initialize an empty list to store the lines from the file
    lines = []

    try:
        # Attempt to open and read the file
        with open(fileName, 'r') as file:
            # Read each line from the file and append it to the list
            for line in file:
                # strip() is used to remove trailing and leading whitespace including newline characters
                lines.append(line.strip())

    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"Error: The file '{fileName}' was not found.")
        return lines

    # Initialize an empty list to store the filtered results
    filteredResults = []

    # Loop over the lines to filter based on maxPrice criteria
    for line in lines:
        try:
            # Attempt to cast the data point to float
            dataPoint = float(line)

            # Check if the data point satisfies the maxPrice criteria
            if dataPoint <= maxPrice:
                filteredResults.append(dataPoint)

        except ValueError:
            # Handle exceptions for values that cannot be cast to a float
            print(f"Error: The value '{line}' cannot be cast to a float and was skipped.")

    return filteredResults


# 5. Create a function, called realStateAnalysis, that takes a location, type string. The
# function must ask the user for the file names for buy prices, living space and rent prices
# whilst handling the file not found error (there is a clever to do this).

# The function must ask the user to enter a file name until they entered a valid file name.
# Note: the file names must have the extension .csv to work

# The function must then compute the average buy price, average rent price and average living
# space. Perform checks on your data as the data may not be very clean (you should expect
# missing values and negative values. You must deal with them).

# Write the results in a file called : realStateAnalysis.csv using the following format :
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

def euroToDollar(euroValue):
    """
    Convert a value from euros to dollars.

    Parameters:
    - euroValue (float): The value in euros.

    Returns:
    - float: The value converted to dollars.
    """
    conversionRate = 1.18
    return (euroValue * conversionRate)


def sqmtToSqft(sqmtValue):
    """
    Convert a value from square meters to square feet.

    Parameters:
    - sqmtValue (float): The value in square meters.

    Returns:
    - float: The value converted to square feet.
    """
    conversionFactor = 10.764
    return (sqmtValue * conversionFactor)


def realStateAnalysis():
    """
    Collects data files for both Madrid and Netherlands, processes the real estate data, and writes the results 
    to 'realStateAnalysis.csv'. If the output file already exists, it is overwritten with new data.
    """

    # Inner function to collect data files for a specific location
    def collectData(location):
        """
        Prompt user to provide data files for the given location.

        Parameters:
        - location (str): The name of the location (Madrid or Netherlands).

        Returns:
        - dict: A dictionary containing filenames for buy prices, living space, and rent prices.
        """
        dataFiles = {}  # Dictionary to store the filenames

        # Collect buy prices filename
        while True:
            try:
                buyPricesFileName = input(f"Enter the filename for buy prices in {location}: ")
                if buyPricesFileName[-4:] != '.csv':
                    raise ValueError("Filename must have a .csv extension")
                dataFiles['buyPrices'] = buyPricesFileName
                break
            except FileNotFoundError:
                print("File not found. Please try again.")

        # Collect living space filename
        while True:
            try:
                livingSpaceFileName = input(f"Enter the filename for living space in {location}: ")
                if livingSpaceFileName[-4:] != '.csv':
                    raise ValueError("Filename must have a .csv extension")
                dataFiles['livingSpace'] = livingSpaceFileName
                break
            except FileNotFoundError:
                print("File not found. Please try again.")

        # Collect rent prices filename
        while True:
            try:
                rentPricesFileName = input(f"Enter the filename for rent prices in {location}: ")
                if rentPricesFileName[-4:] != '.csv':
                    raise ValueError("Filename must have a .csv extension")
                dataFiles['rentPrices'] = rentPricesFileName
                break
            except FileNotFoundError:
                print("File not found. Please try again.")

        return dataFiles

    # Collecting data files for both locations
    firstLocation = input("Please enter the first location (Madrid or Netherlands): ")
    firstDataFiles = collectData(firstLocation)

    secondLocation = "Netherlands" if firstLocation == "Madrid" else "Madrid"
    secondDataFiles = collectData(secondLocation)

    # Function to process the data and write results to the CSV file
    def processAndWrite(location, dataFiles):
        """
        Process the provided data files and write the analysis results to 'realStateAnalysis.csv'.

        Parameters:
        - location (str): The name of the location (Madrid or Netherlands).
        - dataFiles (dict): A dictionary containing filenames for buy prices, living space, and rent prices.
        """

        # Read the data from the files
        buyPrices = inputData(dataFiles['buyPrices'])
        livingSpace = inputData(dataFiles['livingSpace'])
        rentPrices = inputData(dataFiles['rentPrices'])

        # Calculate the averages and convert the values
        avgBuyPrice = euroToDollar(computeAverage(listOfFloats(buyPrices)))
        avgRentPrice = euroToDollar(computeAverage(listOfFloats(rentPrices)))
        avgLivingSpace = sqmtToSqft(computeAverage(listOfFloats(livingSpace)))

        # Append the results to the output file
        with open('realStateAnalysis.csv', 'a') as file:
            file.write(f"{location}, {avgBuyPrice}, {avgRentPrice}, {avgLivingSpace}\n")
        print(f"Analysis for {location} has been saved to 'realStateAnalysis.csv'.")

    # To ensure the file is overwritten if it exists, open it in write mode and close it immediately
    # This action effectively clears the file
    with open('realStateAnalysis.csv', 'w') as file:
        pass

    # Process the collected data and write results for both locations
    processAndWrite(firstLocation, firstDataFiles)
    processAndWrite(secondLocation, secondDataFiles)


def main():
    # Test the inputData function
    print("Testing inputData function...")
    # Assume sampleData.csv has some sample lines to test
    print(inputData("sampleData.csv"))
    print()

    # Test the listOfFloats function
    print("Testing listOfFloats function...")
    # Expect [1.23, 4.56, 7.89]
    print(listOfFloats(["1.23", "4.56", "abc", "", "7.89"]))
    print()

    # Test the computeAverage function
    print("Testing computeAverage function...")
    print(computeAverage([1.0, 2.0, 3.0, 4.0]))  # Expect 2.5
    try:
        print(computeAverage([1.0, 2.0, "3.0", 4.0]))
    except TypeError as e:
        print(f"Caught expected error: {e}")
    print()

    # Test the filteredData function
    print("Testing filteredData function...")
    # Assume samplePrices.csv has some sample prices and expect those <= 100.0
    print(filteredData("samplePrices.csv", 100.0))
    print()

    # Test euroToDollar function (Not in previous script, so I'll add it here for consistency)
    print("Testing euroToDollar function...")
    print(euroToDollar(100))  # Expect 118.0 based on 1.18 conversion rate
    print()

    # Test sqmtToSqft function
    print("Testing sqmtToSqft function...")
    print(sqmtToSqft(100))  # Expect 1076.4 based on 10.764 conversion factor
    print()


if __name__ == "__main__":
    realStateAnalysis()
    main()

## END.