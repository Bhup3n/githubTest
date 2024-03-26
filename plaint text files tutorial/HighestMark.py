#this program reads the names and marks from a text file and prints the name and mark of the student with the highest mark (EXCLUDING MULTIPLE HIGH MARK HOLDERS)

import csv #a csv file is a file that has rows and collumns seperated by commas

currentHighestMark = 0
currentHighestMarkHolder = ""

with open("marks.txt", "r") as file: #read from the file
    csvReader = csv.reader(file) #use the csv file reader to make our life easier
    for row in csvReader: #iterating through each row
        currentMark = row[1] #the current mark equals the row's mark we are in
        if int(currentMark) > int(currentHighestMark): #if our current mark is higher than the highest mark we have had so far
            currentHighestMark = currentMark #then our current mark is our new current highest mark
            currentHighestMarkHolder = row[0] #the holder of that mark is also assigne
    print(currentHighestMarkHolder, currentHighestMark) #print out the holder and the mark they got