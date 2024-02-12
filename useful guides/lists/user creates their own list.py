num_student = int(input("how many students will you input:"))  #the student number is how many rows there will be
num_test = int(input("how many tests are there:"))  #the test number is how many collumns there will be
marks = [] #create empty array of marks
for i in range(num_student):
    marks.append([None]*num_test) #create array for each student
for student in range(num_student):
    for test in range(num_test):
        print("Enter mark for student", student, "test", test)
        marks[student][test] = input()

#this whole code allows the user to create an array/list of the marks students got in each test they did
#and if you want to print out the final result, you can use the code below

for x in marks:
    print("")
    for y in x:
        print(y, end="\t")