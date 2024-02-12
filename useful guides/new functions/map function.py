#map() applies a function to each item in an iterable (list, tuple, etc..)
#map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),                         #a store in dollars
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)          #converting shop prices to euros

store_euros = map(to_euros, store)

#if you want to add the results into a list then you would put this in
#store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)


#break down below

#map(to_euros, store)
#the "map" = keyword
#the "to_euros" = the function name
#the "store" = the name of the iterable, (in this it was a list)