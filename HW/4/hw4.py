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


###---------------------###
###------ Classes ------###
###---------------------###

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

class Car:
    """
    Class DocString. Indent the DocString.
    Represents a car with various attributes related to its specifications.

    Attributes:
    ----------------------------------------
    color (str): The color of the car.
    year (int): The year the car was manufactured.
    make (str): The manufacturer of the car.
    model (str): The specific model of the car.
    num_doors (int): The total number of doors including the hatch/tail gate.
    engine_type (str): The type of engine (gas, diesel, electric).
    top_speed (float): The top speed of the car in miles/hour.
    mpg (float): Miles per gallon the car achieves.
    """

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        Method DocString. Indent the DocString.
        Initializes the Car object with the provided attributes.

        Args:
            color (str): The color of the car.
            year (int): The year the car was manufactured.
            make (str): The manufacturer of the car.
            model (str): The specific model of the car.
            num_doors (int): The total number of doors including the hatch/tail gate.
            engine_type (str): The type of engine (gas, diesel, electric).
            top_speed (float): The top speed of the car in miles/hour.
            mpg (float): Miles per gallon the car achieves.
        """
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg


# 2. Complete the following methods :
# changeColor: this method should take in a color as an argument (str)
# and change the color attribute of the Car instance

# carInfo: this method should take no arguments and return a string
# with the basic car info in the format : "Make - Model - Color"

class Car:
    """
    Class DocString. Indent the DocString.
    Represents a car with various attributes related to its specifications.

    Attributes:
    ----------------------------------------
    color (str): The color of the car.
    year (int): The year the car was manufactured.
    make (str): The manufacturer of the car.
    model (str): The specific model of the car.
    num_doors (int): The total number of doors including the hatch/tail gate.
    engine_type (str): The type of engine (gas, diesel, electric).
    top_speed (float): The top speed of the car in miles/hour.
    mpg (float): Miles per gallon the car achieves.

    Methods:
    ----------------------------------------
    changeColor: Changes the color of the car.
    carInfo: Provides basic information about the car in "Make - Model - Color" format.
    """

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        Method DocString. Indent the DocString.
        Initializes the Car object with the provided attributes.

        Args:
            color (str): The color of the car.
            year (int): The year the car was manufactured.
            make (str): The manufacturer of the car.
            model (str): The specific model of the car.
            num_doors (int): The total number of doors including the hatch/tail gate.
            engine_type (str): The type of engine (gas, diesel, electric).
            top_speed (float): The top speed of the car in miles/hour.
            mpg (float): Miles per gallon the car achieves.
        """
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg

    def changeColor(self, new_color):
        """
        Method DocString. Indent the DocString.
        Changes the color of the car to the provided new color.

        Args:
            new_color (str): The new color to be set for the car.

        Return:
            None
        """
        self.color = new_color

    def carInfo(self):
        """
        Method DocString. Indent the DocString.
        Provides a string with basic car information in the format "Make - Model - Color".

        Return:
            str: The basic car information.
        """
        return (f"{self.make} - {self.model} - {self.color}")


# 3. Complete the following method :
# betterGasMileage: this method should take two instances of the Car
# class and return the car info, using the carInfo method, of the car
# instance that gets the better gas mileage.

class Car:
    """
    Class DocString. Indent the DocString.
    Represents a car with various attributes related to its specifications.

    Attributes:
    ----------------------------------------
    color (str): The color of the car.
    year (int): The year the car was manufactured.
    make (str): The manufacturer of the car.
    model (str): The specific model of the car.
    num_doors (int): The total number of doors including the hatch/tail gate.
    engine_type (str): The type of engine (gas, diesel, electric).
    top_speed (float): The top speed of the car in miles/hour.
    mpg (float): Miles per gallon the car achieves.

    Methods:
    ----------------------------------------
    changeColor: Changes the color of the car.
    carInfo: Provides basic information about the car in "Make - Model - Color" format.
    betterGasMileage: Compares the mpg of two cars and returns the car info of the one with better mileage.
    """

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg

    def changeColor(self, new_color):
        """
        Changes the color of the car to the provided new color.

        Args:
            new_color (str): The new color to be set for the car.

        Return:
            None
        """
        self.color = new_color

    def carInfo(self):
        """
        Provides a string with basic car information in the format "Make - Model - Color".

        Return:
            str: The basic car information.
        """
        return (f"{self.make} - {self.model} - {self.color}")

    def betterGasMileage(self, car1, car2):
        """
        Method DocString. Indent the DocString.
        Compares the mpg of two Car instances and returns the car info of the one with better mileage.

        Args:
            car1 (Car): The first Car instance.
            car2 (Car): The second Car instance.

        Return:
            str: The car info of the Car instance with better mileage.
        """
        if car1.mpg > car2.mpg:
            return car1.carInfo()
        else:
            return car2.carInfo()


# 4. Create the following class attribute and class method :
# create a class attribute, called num_cars, which increases every time
# a new Car instance is created.

class Car:
    """
    Class DocString. Indent the DocString.
    Represents a car with various attributes related to its specifications.

    Attributes:
    ----------------------------------------
    color (str): The color of the car.
    year (int): The year the car was manufactured.
    make (str): The manufacturer of the car.
    model (str): The specific model of the car.
    num_doors (int): The total number of doors including the hatch/tail gate.
    engine_type (str): The type of engine (gas, diesel, electric).
    top_speed (float): The top speed of the car in miles/hour.
    mpg (float): Miles per gallon the car achieves.
    num_cars (int): The total number of Car instances created.

    Methods:
    ----------------------------------------
    changeColor: Changes the color of the car.
    carInfo: Provides basic information about the car in "Make - Model - Color" format.
    betterGasMileage: Compares the mpg of two cars and returns the car info of the one with better mileage.
    getNumCars: Returns the total number of Car instances created.
    """

    # Class attribute to keep track of the number of Car instances created
    num_cars = 0

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg

        # Increment the class attribute num_cars each time a new instance is created
        Car.num_cars += 1

    def changeColor(self, new_color):
        """
        Changes the color of the car to the provided new color.

        Args:
            new_color (str): The new color to be set for the car.

        Return:
            None
        """
        self.color = new_color

    def carInfo(self):
        """
        Provides a string with basic car information in the format "Make - Model - Color".

        Return:
            str: The basic car information.
        """
        return (f"{self.make} - {self.model} - {self.color}")

    def betterGasMileage(self, car1, car2):
        """
        Compares the mpg of two Car instances and returns the car info of the one with better mileage.

        Args:
            car1 (Car): The first Car instance.
            car2 (Car): The second Car instance.

        Return:
            str: The car info of the Car instance with better mileage.
        """
        if car1.mpg > car2.mpg:
            return car1.carInfo()
        else:
            return car2.carInfo()

    def getNumCars(self):
        """
        Returns the total number of Car instances created.

        Return:
            int: The total number of Car instances.
        """
        return Car.num_cars


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

class Vehicle:
    """
    Class DocString. Indent the DocString.
    Represents a generic vehicle with basic attributes related to its specifications.

    Attributes:
    ----------------------------------------
    color (str): The color of the vehicle.
    year (int): The year the vehicle was manufactured.
    make (str): The manufacturer of the vehicle.
    model (str): The specific model of the vehicle.
    top_speed (float): The top speed of the vehicle in miles/hour.
    mpg (float): Miles per gallon the vehicle achieves.
    """

    def __init__(self, color, year, make, model, top_speed, mpg):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.mpg = mpg


class Car(Vehicle):
    """
    Class DocString. Indent the DocString.
    Represents a car, inheriting attributes and behaviors from the Vehicle class and adding car-specific details.

    Attributes:
    ----------------------------------------
    num_doors (int): The total number of doors including the hatch/tail gate.
    engine_type (str): The type of engine (gas, diesel, electric).
    num_cars (int): The total number of Car instances created.

    Methods:
    ----------------------------------------
    changeColor: Changes the color of the car.
    carInfo: Provides basic information about the car in "Make - Model - Color" format.
    betterGasMileage: Compares the mpg of two cars and returns the car info of the one with better mileage.
    getNumCars: Returns the total number of Car instances created.
    """

    num_cars = 0

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        # Initialize attributes from the parent class
        super().__init__(color, year, make, model, top_speed, mpg)

        # Attributes specific to the Car class
        self.num_doors = num_doors
        self.engine_type = engine_type
        Car.num_cars += 1

    def changeColor(self, new_color):
        """
        Changes the color of the car to the provided new color.

        Args:
            new_color (str): The new color to be set for the car.

        Return:
            None
        """
        self.color = new_color

    def carInfo(self):
        """
        Provides a string with basic car information in the format "Make - Model - Color".

        Return:
            str: The basic car information.
        """
        return f"{self.make} - {self.model} - {self.color}"

    def betterGasMileage(self, car1, car2):
        """
        Compares the mpg of two Car instances and returns the car info of the one with better mileage.

        Args:
            car1 (Car): The first Car instance.
            car2 (Car): The second Car instance.

        Return:
            str: The car info of the Car instance with better mileage.
        """
        if car1.mpg > car2.mpg:
            return car1.carInfo()
        else:
            return car2.carInfo()

    def getNumCars(self):
        """
        Returns the total number of Car instances created.

        Return:
            int: The total number of Car instances.
        """
        return Car.num_cars