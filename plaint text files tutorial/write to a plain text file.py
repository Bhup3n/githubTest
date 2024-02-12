text = "this is pretty neat\nwe can also read this file and write to it"

with open("test", "w") as file:         #the w means write
    file.write(text)


file.close()