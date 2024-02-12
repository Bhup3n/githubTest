array_tens = [ [1,   2,  3,  4,  5,  6],
               [11, 12, 13, 14, 15, 16],
               [21, 22, 23, 24, 25, 26],
               [31, 32, 33, 34, 35, 36] ]
user_row = int(input("what row do you want to enter the new number:"))
user_collumn = int(input("what collumn do you want to enter the new number:"))
array_tens[user_row - 1][user_collumn - 1] = int(input("what is the new number:"))
for x in array_tens:
    print("")
    for y in x:
        print(y, end="\t")   #without the for loops, it would print the list in one row
print("\nyour change was in row", user_row, "and collumn", user_collumn)