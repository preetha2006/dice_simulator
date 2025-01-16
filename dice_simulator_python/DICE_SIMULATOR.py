#dice simulator
import random

print("----------------------DICE-ROLL---------------------")

a = 'r'

# while loop for rolling the dice
while a == 'r':

    r = random.randint(1, 6)

    if r == 1:
        print("|      |")
        print("|   0  |")
        print("|      |")
    elif r == 2:
        print("|0     |")
        print("|      |")
        print("|     0|")
    elif r == 3:
        print("|0     |")
        print("|   0  |")
        print("|     0|")
    elif r == 4:
        print("|0    0|")
        print("|      |")
        print("|0    0|")
    elif r == 5:
        print("|0    0|")
        print("|   0  |")
        print("|0    0|")
    elif r == 6:
        print("|0    0|")
        print("|0    0|")
        print("|0    0|")

    # identify whether user wants to play again or exit
    a = input("Enter 'r' to roll the dice and 'n' to stop: ")
    print("\n")
    
print("----------------THANK YOU FOR PLAYING----------------")
