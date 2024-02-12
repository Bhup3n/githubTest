#lamda functions are functions written in one lines
#they are used for short periods of time and for short functions
#lambda parameters:expression

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(2, 3))
print(add(3, 4, 5))
print(full_name("jeff", "bezos"))
print(age_check(13))


#break down below

#double = lambda x: x * 2

#the "double" = function name
#the "lambda" = the keyword
#the "x" = the parameter
#everything after the colon is what the code is inside of the function