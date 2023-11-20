# Start:


import unittest
from car import Car  # Import the Car class from the file where it's defined



###------------------------###
###------ Unit Tests ------###
###------------------------###

# In a separate file, called test_classes.py, complete the class for the
# unit tests. Import your Car class from homework 4.

# 1. Create the following instances for your unit tests :
# car1 = Car("yellow", 2010, "Ferrari", "LaFerrari", 3, "gas", 245, 6)
# car2 = Car("red", 2010, "Lambourghini", "Aventador", 3, "gas", 252, 6.2)

def setUp(self):
        # Create instances of Car for use in tests
        self.car1 = Car("yellow", 2010, "Ferrari", "LaFerrari", 3, "gas", 245, 6)
        self.car2 = Car("red", 2010, "Lamborghini", "Aventador", 3, "gas", 252, 6.2)


# 2. Write an unit test, called test_betterGasMileage, that checks that the
# betterGasMileage for car1 and car2 is working properly (keep in mind that
# you're using float values for mpg, so use the appropriate test).

def test_betterGasMileage(self):
        # Test that the betterGasMileage method
        self.assertEqual(self.car1.betterGasMileage(self.car2), self.car2.charInfo(), "Car with better MPG should be car2")


# 3. Write an unit test, called test_changeColor, that checks that the attribute
# color of car1 above corresponds to the correct color value, then change the
# car's color to blue using the changeColor method, and check that the car's
# color is now blue.

def test_changeColor(self):
        # Test that color changes correctly
        self.assertEqual(self.car1.color, "yellow", "Initial color should be yellow")
        self.car1.changeColor("blue")
        self.assertEqual(self.car1.color, "blue", "Color after change should be blue")


# 4. Write an unit test, called test_numCars, that checks that the class variable
# num_cars is equal to 2 after having created the car1 and car2 variables.

def test_numCars(self):
        # Test that the class variable num_cars works correctly
        self.assertEqual(Car.num_cars, 2, "There should be 2 cars")



# class TestClasses(unittest.TestCase):
class TestClasses(unittest.TestCase):

    def setUp(self):
        """
        Create instances of Car for use in all test methods.
        """

        # Reset the counter before each test suite run
        Car.num_cars = 0
        self.car1 = Car("yellow", 2010, "Ferrari", "LaFerrari", 3, "gas", 245, 6)
        self.car2 = Car("red", 2010, "Lamborghini", "Aventador", 3, "gas", 252, 6.2)


    def test_betterGasMileage(self):
        """
        Test that the betterGasMileage method returns the car with better mpg.
        """

        self.assertEqual(self.car2.carInfo(), self.car1.betterGasMileage(self.car2), "Car with better MPG should be car2")


    def test_changeColor(self):
        """
        Test that the car's color changes properly using the changeColor method.
        """

        self.assertEqual(self.car1.color, "yellow", "Initial color should be yellow")
        self.car1.changeColor("blue")
        self.assertEqual(self.car1.color, "blue", "Color after change should be blue")


    def test_numCars(self):
        """
        Test that the class variable num_cars is incremented properly.
        """

        self.assertEqual(Car.num_cars, 2, "There should be 2 cars after the setUp method")



if __name__ == '__main__':
    unittest.main()


# END.