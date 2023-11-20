## START:


import json



'''
COMP 4401
Homework 8 - Dictionaries & JSON Files

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


# Table with type equivalence between JSON and Python
# Python	            JSON
#--------------------------------
# dict	                object
# list, tuple	        array
# str	                string
# int, long, float	    number
# True	                true
# False	                false
# None	                null

'''
#--------------------------------------------------------------------------#




###----------------------###
###-----Dictionaries-----###
###----------------------###

# 1. Write a function, called listToDict, that takes a list as an argument
# and returns a dictionary containing the keys 1 through n, where n is the
# size of the list, and the values correspond to the values in the list.
# For example, if the list is [2, 6, 6, 1, 7, 9] then the dictionary maps:
# 1 —> 2, 2 —> 6, 3 —>6, 4 —> 1, 5 —> 7 and 6 —> 9.
# In Python this would be: {1:2, 2:6, 3:6, 4:1, 5:7, 6:9}
# (10 points)

def listToDict(inputList) -> dict:
    """
    Convert a list to a dictionary with keys starting at 1 and values corresponding to the list items.

    Parameters:
    inputList (list): The list to convert to a dictionary.

    Returns:
    dict: A dictionary mapping 1 through n to the corresponding elements in the input list.
    """

    # Initialize an empty dictionary
    resultDict = {}
    # Loop through the input list and enumerate it starting from 1, to get index and value
    for index, value in enumerate(inputList, 1):
        # Assign the value to the corresponding key in the resultDict
        resultDict[index] = value

    return resultDict


# 2. Write a function, called newDict, that takes a dictionary as an argument
# and returns a new dictionary with the keys and values inverted (keys become
# values and values become keys).
# What happens if there are duplicate values?
# (10 points)

def newDict(originalDict) -> dict:
    """
    Invert a dictionary by making the keys as values and the values as keys.

    Parameters:
    originalDict (dict): The dictionary to invert.

    Returns:
    dict: A new dictionary with values as keys and keys as values. If there are duplicate
          values in the original dictionary, the resulting dictionary will contain only the
          last original key for each value.
    """

    # Invert the dictionary using a dictionary comprehension
    invertedDict = {value: key for key, value in originalDict.items()}

    return invertedDict


# 3. Write a function, called uniqueElems, that takes a list of values as a
# parameter and determines if all elements are unique (no repeated values).
# Return True if all values are unique, False otherwise. Think of a way to use
# dictionary to perform this task.
# (10 points)

def uniqueElems(valueList) -> bool:
    """
    Check if all elements in the provided list are unique.

    Parameters:
    valueList (list): A list of values to check for uniqueness.

    Returns:
    bool: True if all elements are unique, False otherwise.
    """

    # Use a dictionary to store the occurrence of each element.
    uniqueDict = {}
    # Since dictionary keys are unique, if the size of the dictionary is equal to the size of the list, all elements are unique.
    for value in valueList:
        if value in uniqueDict:
            # If the value is already in the dictionary, not all elements are unique.
            return False
        else:
            # Add the value to the dictionary.
            uniqueDict[value] = True

    # If the loop completes without returning False, all elements are unique.
    return True


# 4. Write a function, called valFrequency, that given a list of values as a
# parameter, counts the frequencies for each value in the list. You can do this
# by returning a dictionary (think about what the key should be and what value
# should be associated with it).
# For example, if the list is [1, 3, 5, 2, 1, 2, 5, 8, 4, 5] then we have:
# 2 x 1's, 1 x 3's, 3 x 5's, 2 x 2's, 1 x 4's, 1 x 8’s
# In Python this would be: {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}
# (10 points)

def valFrequency(valueList) -> dict:
    """
    Count the frequency of each value in the provided list.

    Parameters:
    valueList (list): A list of values for frequency counting.

    Returns:
    dict: A dictionary with values as keys and their frequencies as values.
    """

    frequencyDict = {}
    for value in valueList:
        # The get() method returns 0 when the value is not yet in the dictionary, and increment the count of value in the dictionary.
        frequencyDict[value] = frequencyDict.get(value, 0) + 1

    return frequencyDict


# 5. Write a function, called addsToK, that given an integer k and a list of n
# unordered integers A, determines if there is a pair of distinct integers in A
# that add up to k. Returns True if there are, False otherwise.
# For example : given [1, 6, 7, 3, 7, 10, 3] if k=13 then there is a pair of
# integers that add up to 13 : 10 and 3. If k=14 then there isn’t a pair of distinct
# integers that add up to 14 (can’t use 7 twice even if it appears twice in the list)
# (10 points)

def addsToK(k, A) -> bool:
    """
    Determine if there are two distinct integers in the list A that add up to the integer k.

    Parameters:
    k (int): The target sum to find within the list of integers.
    A (list of int): The list of integers to search through.

    Returns:
    bool: True if there is at least one pair of distinct integers that add up to k, False otherwise.
    """

    # Create a set to store the numbers we have seen so far.
    seenNumbers = set()
    for number in A:
        # Calculate the complementary number that would add up to k.
        complement = k - number
        # Check if the complement is in the set.
        if complement in seenNumbers:
            # We have found two numbers that add up to k.
            return True
        # Add the current number to the set of seen numbers.
        seenNumbers.add(number)

    # If we reach here, no pair adds up to k.
    return False



###-------------------###
###-----JSON FIle-----###
###-------------------###

# 6. Write a function, called senatorsInfo, that takes a filename string
# as an argument. It should load the json file and extract the Senator's
# following information:
# First name
# Last name
# State
# Party
# Start date (since when they've been Senators)
# Congress number (which sessions of Congress they were Senators for)
# Contact form
# Phone number
# Twitter handle
# Birthday
# Nickname
# The function should write the senators information to a json file
# called senatorsInfo.json. Use an indent of 2 to make the data more
# readable. The function should also return the data, this should
# be a list of dictionaries.
# Hint: You may want to use the get() method when getting the data
# (20 points)

def senatorsInfo(fileName) -> list:
    """
    Extracts specific information about senators from a JSON file, writes it to 'senatorsInfo.json',
    and returns the data as a list of dictionaries.

    Parameters:
    fileName (str): The name of the JSON file containing senators' data.

    Returns:
    list: A list of dictionaries containing information for each senator.
    """

    # Open and read the data from the given file name
    with open(fileName, 'r') as file:
        data = json.load(file)
    # List to hold all senators' information
    senatorsData = []
    # Iterate through each senator's data in the 'objects' list
    for item in data['objects']:
        # Extract the nested 'person' object
        person = item['person']
        # Extract the nested 'extra' object
        extra = item['extra']
        # Construct the dictionary with the required information
        senatorInfo = {
            'FirstName': person.get('firstname'),
            'LastName': person.get('lastname'),
            'State': item.get('state'),
            'Party': item.get('party'),
            'StartDate': item.get('startdate'),
            'CongressNumber': item.get('congress_numbers'),
            'ContactForm': extra.get('contact_form'),
            'PhoneNumber': item.get('phone'),
            'TwitterHandle': person.get('twitterid'),
            'Birthday': person.get('birthday'),
            'Nickname': person.get('nickname')
        }
        senatorsData.append(senatorInfo)

    # Write the senators' information to 'senatorsInfo.json' with an indent of 2
    with open('senatorsInfo.json', 'w') as outFile:
        json.dump(senatorsData, outFile, indent = 2)

    # Return the list of dictionaries
    return senatorsData


# 7. Write a function, called noContactForm, that takes in a filename string,
# loads the data in from a json file and returns a list containing the first
# and last name of the senators that do
# not have a contact form.
# (15 points)

def noContactForm(fileName) -> list:
    """
    Loads data from a .json file and returns a list of names of senators without a contact form.

    Parameters:
    fileName (str): The name of the JSON file to read from.

    Returns:
    list: A list containing the first and last names of senators without a contact form.
    """

    # Load the data from the JSON file
    with open(fileName, 'r') as file:
        data = json.load(file)
    # Initialize an empty list to hold the names of senators without a contact form
    senatorsNoContact = []
    # Iterate through each senator's data in the 'objects' list
    for item in data['objects']:
        extra = item.get('extra', {})
        # Check if the 'contact_form' key is missing, has a falsy value, or an empty string
        if not extra.get('contact_form'):
            person = item.get('person', {})
            # Extract the first and last name and append to the list
            fullName = person.get('firstname', '') + " " + person.get('lastname', '')
            # .strip() to remove potential leading/trailing spaces
            senatorsNoContact.append(fullName.strip())

    return senatorsNoContact


# 8. Write a function, called congressSessionMembers, that takes a congress session
# sessionNumber (int) and a filename (str). It should load the data created in question 6
# and search for all the senators that were part of that particular session of congress.
# The function should write the resulting senators to a file called
# congressSession{sessionNumber}.json and returns a list of every senator that was
# part of the Senate for the given sessionNumber. It should return an empty
# list if none of the senators were members for that congress.
# (Congress session 1 should have nobody in it (except maybe Chuck Grassley
# and Mitch McConnell)).
# The numbers of senators for each Congress session available.
# sessionNumber 116 = 33
# sessionNumber 117 = 64
# sessionNumber 118 = 100
# sessionNumber 119 = 66
# sessionNumber 120 = 34
# all other session numbers should be empty
# (15 points)

def congressSessionMembers(sessionNumber, fileName) -> list:
    """
    Searches for all senators that were part of a specific session of Congress, writes the result to a file,
    and returns a list of those senators.

    Parameters:
    sessionNumber (int): The number of the Congress session to search for.
    fileName (str): The name of the JSON file containing senators' data.

    Returns:
    list: A list of dictionaries, each representing a senator part of the given Congress session.
    """

    # Load the data from the JSON file created by senatorsInfo
    with open(fileName, 'r') as file:
        senatorsData = json.load(file)
    # List to hold all senators part of the specified Congress session
    sessionSenators = []
    # Iterate through each senator's data and check their Congress numbers
    for senator in senatorsData:
        if sessionNumber in senator['CongressNumber']:
            sessionSenators.append(senator)
    # Write the session senators to a file
    sessionFileName = (f'congressSession{sessionNumber}.json')
    with open(sessionFileName, 'w') as outFile:
        json.dump(sessionSenators, outFile, indent = 2)

    return sessionSenators



def main():
    # Test the list_to_dict function
    testList = [2, 6, 6, 1, 7, 9]
    listDict = listToDict(testList)
    print("listToDict result:", listDict)

    # Test the newDict function
    testDict = {1: 'a', 2: 'b', 3: 'c'}
    invertedDict = newDict(testDict)
    print("newDict result:", invertedDict)

    # Test the uniqueElems function
    testListUnique = [1, 2, 3, 4, 5]
    isUnique = uniqueElems(testListUnique)
    print("uniqueElems result:", isUnique)

    # Test the valFrequency function
    testListFreq = [1, 3, 5, 2, 1, 2, 5, 8, 4, 5]
    frequencyResult = valFrequency(testListFreq)
    print("valFrequency result:", frequencyResult)

    # Test the addsToK function
    testListAdds = [1, 6, 7, 3, 7, 10, 3]
    kValue = 13
    addsResult = addsToK(kValue, testListAdds)
    print(f"addsToK result for k={kValue}:", addsResult)

    # Test the senatorsInfo function
    senatorsInfoResult = senatorsInfo('senators.json')
    print("senatorsInfo result:", json.dumps(senatorsInfoResult, indent=2))

    # Test the noContactForm function
    noContactFormResult = noContactForm('senators.json')
    print("noContactForm result:", noContactFormResult)

    # Test the congressSessionMembers function for session 116 as an example
    sessionNumber = 116
    congressMembersResult = congressSessionMembers(sessionNumber, 'senatorsInfo.json')
    print(f"congressSessionMembers result for session {sessionNumber}:", congressMembersResult)



# Run the main function
if __name__ == "__main__":
    main()


## END.