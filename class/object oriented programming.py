# to create a class, we write class
# we usually use capital letters after class
class Car:

    def __init__(self, make, model, year, colour):                     #__init__ means initialise and it constructs(makes) objects for us
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):                            #self refers to the object using this method
        print("this", self.model, "is driving")         #this self is replacing car and anything can be substituted with it

    def stop(self):
        print("this", self.model, "is stopped")

car1 = Car("chevrolet", "corvette", 2021, "blue")          #the x = y, the y has to be the same as the name of the class
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.colour)
car1.drive()
car1.stop()

print("\n")

car2 = Car("ford", "focus", 2022, "red")
print(car2.make)
print(car2.model)
print(car2.year)
print(car2.colour)
car2.drive()
car2.stop()