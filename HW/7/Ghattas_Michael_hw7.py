## START:


import math



'''
COMP 4401
Homework 7 - Strings & Sets

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

###-----------------###
###-----Strings-----###
###-----------------###

# All functions must be able to handle edge cases like an empty string or list and
# strings and lists with a single character.


# 1. Write a function, called checkPalindrome, that takes a string as an argument and
# determines if the string is a palindrome. The function should return True if it is
# a palindrome, False otherwise.
# A palindrome is a string that is the same forward and backward like: level or noon.
# Make sure your function works on the string "rats live on no evil star"
# (10 points)

def checkPalindrome(s: str) -> bool:
    """
    Determines if the input string is a palindrome.

    Parameters:
    - s (str): The input string to check.

    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    """

    # Remove all spaces from the string to handle multi-word palindromes
    s = s.replace(" ", "")

    # Compare the string with its reverse
    return (s == s[::-1])


# 2. Create a function, called sortStrings, that takes a list of strings and sorts the list
# based on the length of string from lower to higher. Cannot use built-in sorting functions
# (10 points)

def sortStrings(lst: list) -> list:
    """
    Sorts a list of strings based on string length from shortest to longest.

    Parameters:
    - lst (list): The list of strings to sort.

    Returns:
    - list: The sorted list of strings.
    """

    # Initialize an empty list for the sorted strings
    sortedList = []

    # While there are strings left in the original list
    while lst:
        # Find the shortest string
        shortest = min(lst, key = len)

        # Add the shortest string to the sorted list
        sortedList.append(shortest)

        # Remove the shortest string from the original list
        lst.remove(shortest)

    return sortedList


# 3. Write a function, called mixedString, that takes a word string and computes a list of
# all words generated by a single swap of letters in the word.
# For example ‘swap’ should return [‘pwas’, ‘wsap’, ‘sawp’, swpa’] (notice that letters are
# only swapped with their immediate neighbors only, i.e. you don’t have ‘waps’)
# (10 points)

def mixedString(word: str) -> list:
    """
    Computes a list of all words generated by a single swap of letters in the word.

    Parameters:
    - word (str): The word to be processed.

    Returns:
    - list: A list containing words generated by swapping adjacent letters.
    """

    # If the word has 1 or 0 characters, return the word itself as no swaps can be made
    if len(word) <= 1:
        return [word]

    # Initialize an empty list to store the results
    result = []

    # Swap the first and last characters and add to the result
    result.append(word[-1] + word[1:-1] + word[0])

    # Convert the word to a list for easy character swapping
    wordList = list(word)

    # Loop through each character in the word
    for i in range(len(word) - 1):
        # Swap adjacent characters
        wordList[i], wordList[i + 1] = wordList[i + 1], wordList[i]

        # Convert the list back to a string and append to the result list
        result.append(''.join(wordList))

        # Swap the characters back to their original position for the next iteration
        wordList[i], wordList[i + 1] = wordList[i + 1], wordList[i]

    return result


# 4. Write a function, called reversePhrase, that takes a string of words and returns the
# string with the words in reverse order. You cannot use any library methods or functions
# like .split().
# For example if the sentence is: “I love python”, then the function returns: “python love
# I”
# (10 points)

def reversePhrase(phrase: str) -> str:
    """
    Reverses the order of words in the input phrase.

    Parameters:
    - phrase (str): The input phrase to reverse.

    Returns:
    - str: The phrase with the words in reverse order.
    """

    # Initialize an empty list to store words
    words = []
    # Initialize an empty string to temporarily store a word
    word = ""

    # Loop through each character in the phrase
    for char in phrase:
        # If the character is not a space, add it to the temporary word
        if char != ' ':
            word += char
        # If the character is a space or it's the end of the string, append the word to the words list and reset word
        else:
            words.append(word)
            word = ""
    # Append the last word (if it exists)
    if word:
        words.append(word)

    # Reverse the list of words and join them with spaces to get the reversed phrase
    reversedPhrase = ' '.join(words[::-1])

    return reversedPhrase


# 5. Write a function, called uniqueLetters, that takes a string as an argument and returns
# a new string with no duplicated letters.
# For example if the word is: “application” then the function returns “aplicton”
# (10 points)

def uniqueLetters(word: str) -> str:
    """
    Returns a new string with no duplicated letters from the input word.

    Parameters:
    - word (str): The input word to process.

    Returns:
    - str: The word without duplicated letters.
    """

    # Initialize an empty string to store the result
    uniqueWord = ""
    # Initialize an empty set to keep track of seen characters
    seenChars = set()

    # Loop through each character in the word
    for char in word:
        # If the character hasn't been seen before, add it to the result and the seen set
        if char not in seenChars:
            uniqueWord += char
            seenChars.add(char)

    return uniqueWord



###--------------###
###-----Sets-----###
###--------------###

# 6. Create a function, called setComp, that uses Python set comprehension to generate a
# set of pair tuples consisting of all of the integers between 1 and 10,000 and the square
# of that number but only if the square is divisible by 3 and return that set.
# For example (3, 9) would be in the set since 3^2 is 9 and 9 is divisible by 3.
# You should have 3333 tuples in your set.
# (10 points)

def setComp() -> set:
    """
    Generates a set of pair tuples consisting of all integers between 1 and 10,000
    and the square of that number, but only if the square is divisible by 3.

    Returns:
    - set: The set of tuples.
    """

    # Use set comprehension to generate the required set
    resultSet = {(i, i ** 2) for i in range(1, 10001) if (i ** 2) % 3 == 0}

    return resultSet


# 7. Write a function, called minMaxSet, that takes a set of numbers and returns the
# minimum and maximum value in the set as a tuple. Cannot use the built-in functions
# min()/max(). Hint: You may want to use math.inf and -math.inf
# (10 points)

def minMaxSet(numbers: set) -> tuple:
    """
    Returns the minimum and maximum value in the set of numbers.

    Parameters:
    - numbers (set): The set of numbers.

    Returns:
    - tuple: A tuple with the minimum and maximum value.
    """

    # Initialize the minimum value to positive infinity and the maximum value to negative infinity
    minVal = math.inf
    maxVal = -math.inf

    # Loop through each number in the set
    for num in numbers:
        # If the current number is less than the current minimum, update the minimum
        if num < minVal:
            minVal = num
        # If the current number is greater than the current maximum, update the maximum
        if num > maxVal:
            maxVal = num

    return (minVal, maxVal)


# 8. Write a function, uniqueElems, that given a list of values, determines if all elements
# are unique (no repeated values). If elements are unique return True and False otherwise.
# You must use a set to perform this task.
# (10 points)

def uniqueElems(values: list) -> bool:
    """
    Determines if all elements in the list are unique.

    Parameters:
    - values (list): The list of values.

    Returns:
    - bool: True if all elements are unique, False otherwise.
    """

    # Convert the list to a set
    uniqueSet = set(values)

    # If the length of the set is equal to the length of the list, then all elements are unique
    return len(uniqueSet) == len(values)


# 9. Write a function, called distinctElems, that takes two sets, A and B, and returns a new
# frozen set containing elements that are in either A or B but NOT in the intersection of A
# and B.
# (10 points)

def distinctElems(A: set, B: set) -> frozenset:
    """
    Returns a frozen set containing elements that are in either set A or set B but
    not in the intersection of A and B.

    Parameters:
    - A (set): The first set of values.
    - B (set): The second set of values.

    Returns:
    - frozenset: A frozen set containing the distinct elements.
    """

    return frozenset(A ^ B)


# 10. Write a function, called addsToK, that given an integer k and a list of n unordered
# integers A, determines if there is a distinct pair of integers in A that add up to k.
# Return True if a pair of integers add up to k, return False other.
# You must perform this task using sets.
# (10 points)

def addsToK(k: int, A: list) -> bool:
    """
    Determines if there is a distinct pair of integers in the list A that add up to k.

    Parameters:
    - k (int): The target sum.
    - A (list): The list of unordered integers.

    Returns:
    - bool: True if a distinct pair of integers add up to k, False otherwise.
    """

    # Initialize an empty set to keep track of numbers seen so far
    seen = set()

    # Loop through each number in the list A
    for num in A:
        # Calculate the difference between k and the current number
        diff = (k - num)
        # If the difference is in the set seen, we found a pair that adds up to k
        if diff in seen:
            return True
        # Otherwise, add the current number to the set seen
        seen.add(num)

    # If we have gone through the entire list without finding a pair, return False
    return False



def main():
    """
    Main function to test all the provided functions.
    """

    # Test the checkPalindrome function
    print("Testing checkPalindrome...")
    print(checkPalindrome("rats live on no evil star")) # Should return True
    print(checkPalindrome("hello")) # Should return False

    # Test the sortStrings function
    print("\nTesting sortStrings...")   # Should return ['a', 'kiwi', 'apple', 'banana']
    print(sortStrings(["apple", "banana", "kiwi", "a"]))

    # Test the mixedString function
    print("\nTesting mixedString...")   # Should return ['pwas', 'wsap', 'sawp', 'swpa']
    print(mixedString("swap"))

    # Test the reversePhrase function
    print("\nTesting reversePhrase...") # Should return "python love I"
    print(reversePhrase("I love python"))

    # Test the uniqueLetters function
    print("\nTesting uniqueLetters...") # Should return "aplicton"
    print(uniqueLetters("application"))

    # Test the setComp function
    print("\nTesting setComp...")
    result = setComp()
    print(len(result))  # Should return 3333
    print((3, 9) in result) # Should return True

    # Test the minMaxSet function
    print("\nTesting minMaxSet...") # Should return (1, 9)
    print(minMaxSet({1, 3, 5, 7, 9}))

    # Test the uniqueElems function
    print("\nTesting uniqueElems...")
    print(uniqueElems([1, 2, 3, 4, 5])) # Should return True
    print(uniqueElems([1, 2, 3, 4, 5, 5]))  # Should return False

    # Test the distinctElems function
    print("\nTesting distinctElems...") # Should return frozenset({1, 2, 5, 6})
    print(distinctElems({1, 2, 3, 4}, {3, 4, 5, 6}))

    # Test the addsToK function
    print("\nTesting addsToK...")
    print(addsToK(8, [1, 2, 3, 4, 5]))  # Should return True
    print(addsToK(10, [1, 2, 3, 4, 5])) # Should return False



if __name__ == "__main__":
    main()


## END.