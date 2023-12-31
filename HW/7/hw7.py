## START:


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





# 2. Create a function, called sortStrings, that takes a list of strings and sorts the list
# based on the length of string from lower to higher. Cannot use built-in sorting functions
# (10 points)





# 3. Write a function, called mixedString, that takes a word string and computes a list of
# all words generated by a single swap of letters in the word.
# For example ‘swap’ should return [‘pwas’, ‘wsap’, ‘sawp’, swpa’] (notice that letters are
# only swapped with their immediate neighbors only, i.e. you don’t have ‘waps’)
# (10 points)





# 4. Write a function, called reversePhrase, that takes a string of words and returns the
# string with the words in reverse order. You cannot use any library methods or functions
# like .split().
# For example if the sentence is: “I love python”, then the function returns: “python love
# I”
# (10 points)








# 5. Write a function, called uniqueLetters, that takes a string as an argument and returns
# a new string with no duplicated letters.
# For example if the word is: “application” then the function returns “aplicton”
# (10 points)





###--------------###
###-----Sets-----###
###--------------###

# 6. Create a function, called setComp, that uses Python set comprehension to generate a
# set of pair tuples consisting of all of the integers between 1 and 10,000 and the square
# of that number but only if the square is divisible by 3 and return that set.
# For example (3, 9) would be in the set since 3^2 is 9 and 9 is divisible by 3.
# You should have 3333 tuples in your set.
# (10 points)




# 7. Write a function, called minMaxSet, that takes a set of numbers and returns the
# minimum and maximum value in the set as a tuple. Cannot use the built-in functions
# min()/max(). Hint: You may want to use math.inf and -math.inf
# (10 points)
import math




# 8. Write a function, uniqueElems, that given a list of values, determines if all elements
# are unique (no repeated values). If elements are unique return True and False otherwise.
# You must use a set to perform this task.
# (10 points)




# 9. Write a function, called distinctElems, that takes two sets, A and B, and returns a new
# frozen set containing elements that are in either A or B but NOT in the intersection of A
# and B.
# (10 points)



# 10. Write a function, called addsToK, that given an integer k and a list of n unordered
# integers A, determines if there is a distinct pair of integers in A that add up to k.
# Return True if a pair of integers add up to k, return False other.
# You must perform this task using sets.
# (10 points)
























