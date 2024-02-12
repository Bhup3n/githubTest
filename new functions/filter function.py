#filter() creates a collection of items from an iterable (list, tuple, etc...)
#filter(function, iterable)
#it's kind of like searching for certain criteria withing an iterable

devices = [("ipad", 460.00),
           ("phone", 750.00),
           ("xbox", 350.00),
           ("laptop", 400.00),
           ("alexa", 100.00)]

price = lambda cost: cost[1] <= 400           #if cost[1] is less than or equal to 400

affordable = filter(price, devices)

#if you want to add the results into a list then you would put this in
#affordable = list(filter(price, devices))

for i in affordable:
    print(i)


#break down below

#filter(price, devices)
#the "filter" = the keyword
#the "price" = name of the function
#the "devices" = name of the iterable