# zip(iterables) = combine elements from 2 or more iterables

usernames = ["psp", "bahd", "halo"]          #ist of usernames
passwords = ("123", "fge", "fdsa*?")         #list of passwords
login = ["1/1/2022", "1/2/2022", "1/3/2022"]    #ist of dates

users = zip(usernames, passwords, login)      #this combines all of them so for example, it puts psp, 123 and 1/1/2022 together

#for i in users:
 #   print(i)                         you could print it out llike this, but if you want it seperated, then do this:

for x, y, z in users:
    print(x, ":", y, ":", z)