#this means that you have a class inside of another class but the child class can use the adult class stuff

class Animal:

    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("this rabbit is running")

class Fish(Animal):

    def swim(self):
        print("this fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("this hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

print("\n")

rabbit.run()
fish.swim()
hawk.fly()