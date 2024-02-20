text = "\nthis text has been added onto by a different piece of code!"

with open("test", "a") as file:              #the a means append(add onto)
    file.write(text)