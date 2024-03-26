import csv
import pandas as pd

fileName = "C:\Bhupen\Pycharm\pythonProject\projectContentsGithub\CatsAndDogs"

def addAnimal():
    name = input("\nenter the animal's name: ")
    species = input("enter the animal's species: ")
    dob = input("enter the animal's date of birth: ")
    owner = input("enter the animal's owner name: ")
    with open(fileName, "a") as f:
        f.write(f"\n{name},{species},{dob},{owner}")

def searchForAnimal():
    animal = input("\nEnter the name of the animal you would like to find: ")
    found = False
    with open(fileName, "r") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            if row[0] == animal:
                found = True
                print(f"Name = {row[0]}\nSpecies = {row[1]}\nDate of Birth = {row[2]}\nOwner = {row[3]}")
                break
        if not found:
            print("The animal could not be found")

def removeAnimal():
    animal = input("\nEnter the name of the animal you want to remove: ")
    rowToRemove = pd.read_csv(fileName, index_col="Name")
    rowToRemove = rowToRemove.drop(animal)
    rowToRemove.to_csv(fileName, index=True)



satisfied = False

while not satisfied:
    choice = input("\nWelcome to Cats & Dogs Veterinary Surgery. Would you like to:\na)Add a new animal\nb)search for an animal\nc)remove an animal\nd)Exit program\nenter choice here: ").lower()
    if choice == "a":
        addAnimal()
    elif choice == "b":
        searchForAnimal()
    elif choice == "c":
        removeAnimal()
    elif choice == "d":
        print("\nThank you for using this service.")
        satisfied = True
    else:
        print("\nYou did not enter a valid choice")