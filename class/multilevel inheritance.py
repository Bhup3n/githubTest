#this means that when a derived (child) class inherits another (child) class who inherits and adult class
class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("this dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()