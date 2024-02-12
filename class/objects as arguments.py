class Car:

    colour = None

class Bike:

    colour = None

def change_colour(car, colour):             #make sure this ISNT inside of the car class

    car.colour = colour                   #the "car" has to be the same as the car in the parameter and the 2nd "colour" has to be the same as the one in the parameter



car_1 = Car()
car_2 = Car()

change_colour(car_1, "red")
change_colour(car_2, "blue")

print(car_1.colour)
print(car_2.colour)

bike = Bike()
change_colour(bike, "black")                    #can even do it with 2 classes that are completely seperate
print(bike.colour)