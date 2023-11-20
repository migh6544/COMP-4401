'''
COMP 4401
Homework 4 - Classes & Unit Tests

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


Homework 4 Instructions:
Every class, method and function must have proper DocString documentation of the
following form :

def someFunction(arg1, arg2):
    """
    Function DocString. Indent the DocString.
    One or two lines explaining what the function does

    Args:
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the function ?
    """
    #your code here


class SomeClassIMadeUp:
    """
    Class DocString. Indent the DocString
    One or two lines explaining what the class does

    Attributes:
    ----------------------------------------
        attr1 (type): what is this attribute
        attr2 (type): what is this attribute

    Method:
    ----------------------------------------
        method1: what does this method do
        method2: what does this method do
    """

def method_inside_class(arg1, arg2):
    """
    Method DocString. Indent the DocString
    One or two lines explaining what the method does

    Args: (don't include 'self' in the arguments)
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the method ?
    """


'''
#--------------------------------------------------------------------------#


#####################################
# Answers to all problems are together at the bottom
#####################################


# 1. Complete the following class, called Car.
# The class must have the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -num_doors (this includes the hatch/tail gate) (int)
# -engine_type (gas, diesel, electric) (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)


# 2. Complete the following methods :
# changeColor: this method should take in a color as an argument (str)
# and change the color attribute of the Car instance

# carInfo: this method should take no arguments and return a string
# with the basic car info in the format : "Make - Model - Color"


# 3. Complete the following method :
# betterGasMileage: this method should take two instances of the Car
# class and return the car info, using the carInfo method, of the car
# instance that gets the better gas mileage.


# 4. Create the following class attribute and class method :
# create a class attribute, called num_cars, which increases every time
# a new Car instance is created.


# 5. Make a parent class for Car, called Vehicle, which will
# contain an __init__ method for the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)
#
# Don't forget to change the Car class __init__ method to make use of the Vehicle class.

######### Problems 1-4

# Car standalone class 
class Car():
    """
    Class stores information on different types of cars

    Class attribute: num_cars, which keeps track of the total number of cars
    being initialized as variables

    Object ttributes:
    ----------------------------------------
        color (str): description of car color
        year (int): year the car was made
        make (str): manufacturer of the car
        model (str): model of car
        num_doors (int): number of doors on the car, including hatch
        engine_type (str): gas, disel, or electric
        top_speed (float): highest speed the car can go in miles/hour
        mpg (float): average miles per gallon the car gets

    Object Methods:
    ----------------------------------------
        changeColor: changes the color attribute of the car
        carInfo: returns a string in the format "Make - Model - Color"
        betterGasMileage: compares 2 cars and returns info on the car with better gas mileage

    """
    num_cars = 0

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        initializes a Car object with attributes:
        color, year, make, model, num_doors, engine_type, top_speed, mpg
        also increments num_cars class attribute by 1
        """
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg

        Car.num_cars += 1

    def changeColor(self, new_color):
        """takes new_color argument and updates object color attribute"""
        self.color = new_color

    def charInfo(self):
        """takes no additional arguments besides object itself
        and returns a string in the format 'Make - Model - Color'"""
        return self.make + ' - ' + self.model + ' - ' + self.color
    
    def betterGasMileage(self, other):
        """takes another car as argument
        checks with one has better gas mileage
        calls the carInfo method to return a string representing
        the car with better gas mileage"""
        if self.mpg >= other.mpg:
            return self.charInfo()
        else:
            return other.charInfo()


######### Problem 5

# Vehicle parent class
class Vehicle():
    """
    Class stores information on different types of vehicles (e.g. cars)

    Object ttributes:
    ----------------------------------------
        color (str): description of car color
        year (int): year the car was made
        make (str): manufacturer of the car
        model (str): model of car
        top_speed (float): highest speed the car can go in miles/hour
        mpg (float): average miles per gallon the car gets
    """

    def __init__(self, color, year, make, model, top_speed, mpg):
        """initializes a vehicle object"""
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.mpg = mpg

# Car subclass
class Car(Vehicle):
    """
    Class stores information on different types of cars

    Class attribute: num_cars, which keeps track of the total number of cars
    being initialized as variables

    Object ttributes:
    ----------------------------------------
        color (str): description of car color
        year (int): year the car was made
        make (str): manufacturer of the car
        model (str): model of car
        num_doors (int): number of doors on the car, including hatch
        engine_type (str): gas, disel, or electric
        top_speed (float): highest speed the car can go in miles/hour
        mpg (float): average miles per gallon the car gets

    Object Methods:
    ----------------------------------------
        changeColor: changes the color attribute of the car
        carInfo: returns a string in the format "Make - Model - Color"
        betterGasMileage: compares 2 cars and returns info on the car with better gas mileage

    """
    num_cars = 0

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        initializes a Car object with attributes:
        color, year, make, model, num_doors, engine_type, top_speed, mpg
        """
        super().__init__(color, year, make, model, top_speed, mpg)
        self.num_doors = num_doors
        self.engine_type = engine_type
        
        Car.num_cars += 1

    def changeColor(self, new_color):
        """takes new_color argument and updates object color attribute"""
        self.color = new_color

    def charInfo(self):
        """takes no additional arguments besides object itself
        and returns a string in the format 'Make - Model - Color'"""
        return self.make + ' - ' + self.model + ' - ' + self.color
    
    def betterGasMileage(self, other):
        """takes another car as argument
        checks with one has better gas mileage
        calls the carInfo method to return a string representing
        the car with better gas mileage"""
        if self.mpg >= other.mpg:
            return self.charInfo()
        else:
            return other.charInfo()




























