import time
products = [ ["Milk", 1],
             ["Bread", 0.55],
             ["Pringles", 1.25],
             ["Chicken", 3.65],
             ["Doritos", 1.99] ]

print("these are the products currently in stock:")
time.sleep(1)
f = "{:<10} {:>18}"
print(f.format("Product", "Price(£)"))
for product in products:
    print(f.format(product[0], product[1]))

def products_prices():
    bill = 0
    x = False
    while x == False:
        user_choice = input("do you want to buy any products, yes or no?:")
        if user_choice == "yes":
            user_product = input("what product are you looking for?:")
            user_row = int(input("enter the row it is on:"))
            bill += products[user_row - 1][1]
        else:
            x = True
    print("your total bill is", bill)
products_prices()