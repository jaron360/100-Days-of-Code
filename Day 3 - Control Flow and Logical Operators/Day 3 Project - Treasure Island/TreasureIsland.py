print('''

                    ____...------------...____
              '_.-"` /o/__ ____ __ __  __ \o\_`"-._'
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__    '-.\'uuu'/.-'   __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to treasure island!")
print("Your mission is to find the treasure")

left_or_right = input("Would you like to go left or right? ")

if left_or_right == "left":
    print("You're on the right track.")
    swim_or_wait = input("There is a river in the way - Would you like to swim or wait? ")
    if swim_or_wait == "wait":
        print("Good choice, a school of vicious trout just passed through. ")
        which_door = input("Now you have approached a building with a red, blue, and yellow door. Which door will you choose? ")
        if which_door == "red":
            print("You have died from a fire blast. Game Over")
            exit()
        elif which_door == "blue":
            print("You have been eaten by beasts. Game Over")
            exit()
        elif which_door == "yellow":
            print("You Win!")
            exit()
        else:
            print("Game Over")
            exit()
    else:
        print("Game Over!")
else:
    print("Wrong choice. Game Over")
