#super function can be used to shorten repeated lines in different functions
class Rectangle:
    def __init__(self, length, width):
        self.length = length                        #this shortens these 2 lines from each code, but this can be used for much larger stuff
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)             #this calls the function from the parent class Rectangle and we have to set paramaters

    def area(self):
        return self.length * self.width           #calculates area

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)            #this calls the function from the parent class Rectangle and we have to set paramaters
        self.height = height                 #we keep this line because the cube has a height but the square doesnt

    def volume(self):
        return self.length * self.height * self.width          #calculates volume

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())