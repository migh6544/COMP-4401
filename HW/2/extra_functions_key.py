# extra functions to import

def midpoint(number: int):
    """takes an integer as input and returns the midpoint
    between that integer and zero"""

    # also accepted return number / 2
    return number // 2

if __name__ == '__main__':
    midpoint_of_six = midpoint(6)
    midpoint_of_five = midpoint(5)
    print(midpoint_of_five)
    print(midpoint_of_six)