import random
import time

bot = random.randrange(0,100)
userGuess = int(input("please enter an number between 0 to 100: "))

while userGuess != bot:
    if userGuess > bot:
        print("Your answer is too high, try again")
        time.sleep(0.5)
        userGuess = int(input("please enter an number between 0 to 100: "))
    elif userGuess < bot:
        print("Your answer is too low, please try again!")
        time.sleep(0.5)
        userGuess = int(input("please enter an number between 0 to 100: "))

else:
    print("Your answer is correct! congrats")


