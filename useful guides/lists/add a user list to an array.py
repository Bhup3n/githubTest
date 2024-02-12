array_cars = [ ["Ford", "B-Max", "Red", "BD43XPU"],
               ["Volkswagen", "Golf", "Blue", "RX82YHT"],
               ["Nissan", "Primera", "White", "NS95HDS"] ]
num_cars = 1
num_info = 4
user_car = []
for i in range(num_cars):
    user_car.append([None] * num_info)
    for cars in range(num_cars):
        for info in range(num_info):
            print("enter the car information for your car in the info", info + 1, "collumn:")
            user_car[cars][info] = input()
array_cars = array_cars + user_car
for x in array_cars:
    print("")
    for y in x:
        print(y, end="\t")