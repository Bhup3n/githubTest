marks = [ [16, 30, 14, 28, 23, 4],
          [30, 29, 30, 28, 27, 28],
          [9, 12, 8, 11, 15, 7],
          [22, 24, 19, 21, 18, 25] ]
for student in marks:
    print("") #needed to create a new line after each set of the list
    for test in student:
        print(test, end="\t") #the \t is to end each number with a whitespace/tab