#this is when a child class comes from more than one parent class, this means that the child class has access to both parents
class Prey:
    def flee(self):
        print("this animal flees")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()