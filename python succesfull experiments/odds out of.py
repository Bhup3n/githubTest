import random
import time
print("welcome to the random game, in this you will input a random number between 0 and 5 everytime you are asked to do so")
time.sleep(3)
print("a computer will also guess a number between 0 and 5 and if the numbers guessed match, you have lives and you lose one of them")
time.sleep(3)
print("if the number dont match, your score goes up by 1")
time.sleep(2)
print("the goal is to try and get a high score, once you lose all your lives, its game over")
time.sleep(3)
difficulty = input("do you want to play, easy (3 lives), normal (2 lives) or hard (1 life):")

score = 0
if difficulty == "easy":
    lives = 3
    print("you have 3 lives")
elif difficulty == "normal":
    lives = 2
    print("you have 2 lives")
else:
    lives = 1
    print("you have 1 life")

while lives == 3:
    user_num = int(input("\nenter a number between 0 and 5:"))
    num = random.randint(0, 5)
    if user_num == num:
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("you lost a life, 2 lives remaining")
        lives = 2
        num = random.randint(0, 5)
    elif user_num < 0 or user_num > 5:
        print("bro just enter a number between 0 and 5")
    else:
        score += 1
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("your score is now", score, ", well done")
        num = random.randint(0, 5)

while lives == 2:
    user_num = int(input("\nenter a number between 0 and 5:"))
    num = random.randint(0, 5)
    if user_num == num:
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("\nthats 1 life gone, 1 life remaining, hang in there")
        lives = 1
        num = random.randint(0, 5)
    elif user_num < 0 or user_num > 5:
        print("bro just enter a number between 0 and 5")
    else:
        score += 1
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("your score is now", score, ", well done")
        num = random.randint(0, 5)

while lives == 1:
    user_num = int(input("\nenter a number between 0 and 5:"))
    num = random.randint(0, 5)
    if user_num == num:
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("\nlives remaining = 0, game over, score =",score)
        lives = 0
        num = random.randint(0, 5)
    elif user_num < 0 or user_num > 5:
        print("bro just enter a number between 0 and 5")
    else:
        score += 1
        print("\nyour number was", user_num, "and the computer's number was", end=" ")
        time.sleep(1.2)
        print(num)
        print("your score is now", score, ", well done.")
        num = random.randint(0, 5)


#can use functions to shorten this, in the process of doing testing and will figure out a solution and replace this code with the code
#that works with the functions to make this alot shorter