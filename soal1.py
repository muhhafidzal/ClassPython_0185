#Create a class with a rectangle that has both length and width properties!
#Make the constructor!
#Create a function to calculate its circumference!
#Create a function to calculate the area!
#Create the __str__ function so that it can display the string object! Examples: rectangle, 3 cm long, and 2 cm wide
#Call all function from Class Rectangle to run the program

#Rectangle program
class Rectangle:
    pass

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width cannot be 0")
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"