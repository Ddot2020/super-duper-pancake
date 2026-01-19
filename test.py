user = input("please selection an weapon: (R,P,S) ")

import random
import time

myBot =  ["R", "P", "S"]
bot = random.choice(myBot)


print("Three")
time.sleep(0.5)
print("Two")
time.sleep(0.5)
print("One")
time.sleep(0.5)




if user == "R" and bot == "R":
    print("Draw")
elif user == "P" and bot == "P":
    print("Draw")
elif user == "S" and bot == "S":
    print("Draw")
elif user == "R" and  bot == "S":
    print("User wins")
elif user == "P" and bot == "R":
    print("User Wins")
elif user == "S" and bot == "P":
    print("User Wins")
elif user == "R" and bot == "P":
    print("Bot Wins")
elif user == "P" and bot == "S":
    print("Bot Wins")
elif user == "S" and bot == "R":
    print("Bot Wins")
else:
    print("input invalid, please try again")

print("Bot chooses: ",bot)