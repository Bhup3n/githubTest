names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tyler"]

middleIndex = len(names) // 2
testingVariable = False

valueWanted = input(f"Welcome to the value chooser!\nselect a value you want from the following list:\n{names}\nenter here:")

for i in range(2, len(names) + 1):
    if names[middleIndex] < valueWanted:
        middleIndex += len(names) // (2 * i)
    if names[middleIndex] > valueWanted:
        middleIndex -= len(names) // (2 * i)
    if names[middleIndex] == valueWanted:
        print(f"{valueWanted} is found at index {middleIndex}")
        break
if names[middleIndex] != valueWanted:
    print(f"{valueWanted} is not in the list")
