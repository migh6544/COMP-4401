# Declaring global variable to store user input
GLOBAL_INPUT = input()

# extra_functions.py
def midpoint(integer):
    '''
    Calculate the midpoint between the given integer and 0.

    Parameters:
    integer (int): The integer for which the midpoint is calculated.

    Returns:
    float: The calculated midpoint.
    '''

    # Return midpoint value
    return float(integer / 2)


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


# This function is the program 'conductor'. It calls other functions.
def main(integerInput):
    '''
    This function serves as the entry point of the program when the script is executed directly.

    Parameters:
    integer_input (int): An integer value used as input for testing the midpoint function.

    Returns:
    float: The calculated midpoint.
    '''

    # Call the midpoint() function to calculate result
    return midpoint(integerInput)

# Entry point of the program
if __name__ == '__main__':
    # Call the midpoint function based on input value received
    result = midpoint(10)
    # Print the result
    print(f"Midpoint of {GLOBAL_INPUT} and 0 is: {result}")