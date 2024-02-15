names = ["Tyler", "Katie", "Ivy", "Noah", "Rachel", "Eva", "Charlie", "Liam", "Mia", "Jack",
         "Bob", "Olivia", "Frank", "Grace", "Alice", "Sam", "Quinn", "David", "Peter", "Henry"]

for i in range(0, len(names)):
    for j in range(0, len(names) - i - 1):
        if names[j] > names[j+1]: #if the name should be swapped
            nameToSwap = names[j+1] #using a temporary variable to store the name that will be swapped
            names[j+1] = names[j]
            names[j] = nameToSwap

print(names) #now unjumbled like lol

variable = False
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
print(num1 + num2)