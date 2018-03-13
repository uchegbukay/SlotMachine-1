print("Welcome to the Slot Machine Travel Guide!")
numberOfTimes = input('How many times do you want to play?')
slotsPossible = ["Africa","Europe","Asia","Africa","Asia"]
from random import *
def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    win = ""
    if (slot1==slot2==slot3=="Africa"):
        win = "Congrats! Youre headed to Africa"
    if (slot1==slot2==slot3=="Asia"):
        win = "Congrats! Youre headed to Asia"
    if (slot1==slot2==slot3=="Europe"):
        win = "Congrats! Youre headed to Europe"
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(numberOfTimes)):
    print(play())
