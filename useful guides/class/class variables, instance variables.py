class Car:

    wheels = 4     #class variable            this is delcared inside the class but outside the constructor (__init__)

    def __init__(self, make, model, year, colour):                     #__init__ means initialise and it constructs(makes) objects for us,
        self.make = make       #instance variable
        self.model = model     #instance variable
        self.year = year       #instance variable            this means that each object can have their own unique values
        self.colour = colour   #instance variable

car1 = Car("chevrolet", "corvette", 2021, "blue")
car2 = Car("ford", "focus", 2022, "red")

car1.wheels = 2

print(car1.wheels)
print(car2.wheels)

#to change a class variable, we would do   Car.wheels = x