user_word = input("enter a word you want to encrypt:")
alphabet = "abcdefghijklmnopqrstuvwxyz"
from random import choice
import time
x = 0
while x < 12:
    print(choice(alphabet), end="")
    time.sleep(0.7)
    x += 1
decipher_key = input("\n\ntype the decipher key you would like to use:")
decipher_key_check = input("please retype to ensure that you will remember your decipher key:")
if decipher_key == decipher_key_check:
    print("\nyour decipher key is now officially", decipher_key)
    decode_choice = input("\nwould you like to decode your encrypted code, yes or no?:")
    if decode_choice == "yes":
        decode_check = input("what is the decipher key?:")
        if decode_check == decipher_key:
            print("congratulations, the encrpyted code is", user_word)
        else:
            print("you have been locked out of this accound for attempted hack, you will have to try again from the beggining")
    else:
        print("okay, have a good rest of your day.")
else:
    print("sorry you will have to try again from the beggining (it is what it is)")