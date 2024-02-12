text = "this is the new file we wrote"

with open("test writing", "w") as file:         #the w means write
    file.write(text)


file.close()