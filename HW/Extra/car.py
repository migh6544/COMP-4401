# Start:


# Vehicle parent class
class Vehicle():
    """
    Class stores information on different types of vehicles (e.g. cars)

    Object attributes:
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

    Object attributes:
    ----------------------------------------
        color (str): description of car color
        year (int): year the car was made
        make (str): manufacturer of the car
        model (str): model of car
        num_doors (int): number of doors on the car, including hatch
        engine_type (str): gas, diesel, or electric
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

    def carInfo(self):
        """takes no additional arguments besides object itself
        and returns a string in the format 'Make - Model - Color'"""
        return self.make + ' - ' + self.model + ' - ' + self.color

    def betterGasMileage(self, other):
        """takes another car as argument
        checks with one has better gas mileage
        calls the carInfo method to return a string representing
        the car with better gas mileage"""
        if self.mpg >= other.mpg:
            return self.carInfo()
        else:
            return other.carInfo()


## END.