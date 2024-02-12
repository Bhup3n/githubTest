from tkinter import *

#radio button = similiar to check box but you cget multiple choice but can only select one from the group

food = ["pizza", "burger", "hotdog"]

def order():
    if(x.get()==0):                        #if the value of x = pizza
        print("you got pizza")
    elif(x.get()==1):                     #if value of x = the index of burger
        print("you got burger")
    else:                                 #if none of those 2, then this
        print("you got hotdog")

window = Tk()

pizza = PhotoImage(file="photos/pizza.png")
burger = PhotoImage(file="photos/burger.png")
hotdog = PhotoImage(file="photos/hotdog.png")

food_image = [pizza, burger, hotdog]     #puts all pictures in a list

x = IntVar()

for i in range(len(food)):         #this figures out the length of the food list which is 3 and creates 3 radio buttons
    radiobutton = Radiobutton(window,
                              text=food[i],              #text = the items in the food list, it first prints out pizza, then burger then hotdog
                              variable=x,                #groups radiobuttons together if they share the same variable
                              value=i,                #assings each radio button a different value, so pizza = 0, burger = 1, hotdog = 2
                              padx=20,
                              font=("Comic Sans", 30),
                              image=food_image[i],      #adds images from food image to the radial buttons
                              compound="right",
                              command=order)
    #                         indicatoron=0          this eliminates the circle indicators and turns the images and text into push buttons

    radiobutton.pack(anchor="w")   #have to put this inside of the for loop so it displays all the information and not just the 1st item in the list
                         #the anchor = "w" displays everything to the west side

window.mainloop()