#this program reads the names and marks from a text file and prints the name and mark of the student with the highest mark (INCLUDING MULTIPLE STUDENTS WITH HIGHEST MARK)

import csv #a csv file is a file that has rows and collumns seperated by commas

def endOfFile(file):
    currentPos = file.tell() #get the current position of the file
    file.seek(0, 2) #moves to the end of the file
    endPos = file.tell() #now know the end of the file
    file.seek(currentPos) #move position of the file back to its old position
    return currentPos == endPos #give us a boolean value on whether we have reached the end of the file or not

highestMarkHolders = []
highestMark = 0
currentHighestMarkHolder = ""

with open("marks (Including multiple highest marks).txt", "r") as file: #read from the file
    while not endOfFile(file): #while we havent reached the end of the file
        csvReader = csv.reader(file) #use the csv file reader to make our life easier
        for row in csvReader: #iterating through each row
            currentMark = row[1] #the current mark equals the row's mark we are in
            if int(currentMark) > int(highestMark): #if our current mark is higher than the highest mark we have had so far
                highestMark = currentMark #then our current mark is our new current highest mark
                currentHighestMarkHolder = row[0] #the holder of that mark is also assigned
        file.seek(0) #move the file pointer back to the beginiing
        for row in csvReader: #iterate through the file again to find all of the highest mark holders
            currentMark = row[1] #the current mark equls the row's mark we are in
            if int(currentMark) == int(highestMark): #if our current mark is equal to the highest mark
                highestMarkHolders.append(row[0]) #add the holder of that mark into the list
        print(f"{highestMarkHolders} all have marks of {highestMark}") #print out the highest mark and mark holders


file.close() #closes the file after we are finished with it