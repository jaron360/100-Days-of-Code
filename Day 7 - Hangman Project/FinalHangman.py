import random
from wsgiref.validate import check_status


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


logo = """
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """

print(logo)
stages_wrong = 6

guess_list = []
word_list = [
    "aardvark", "baboon", "camel",
    "dolphin", "elephant", "flamingo",
    "giraffe", "hedgehog", "iguana",
    "jaguar", "kangaroo", "leopard",
    "mongoose", "narwhal", "octopus",
    "penguin", "quokka", "rhinoceros",
    "sloth", "toucan", "umbrella bird",
    "vulture", "walrus", "xenops",
    "yak", "zebra"
]

chosen_word = random.choice(word_list)
#print(chosen_word)

display = ["_" for _ in chosen_word]

for i in chosen_word:
    print("_", end='')
print()

while "_" in display:
    guess = input(f"Guess a letter: \n").lower()

    #Function for adding the correct guess in the display
    def placeholder_func():
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

    #Code for determining if user input is correct or not, or if the guess has already been made
    if guess in guess_list:
        print("You already guessed this letter.")
        continue
    if guess in chosen_word:
        print("Right!")
    else:
        print("Wrong! The Letter you guessed is not in the word.")
        stages_wrong -= 1
        print(stages[stages_wrong])

    #Add each guess to a list, so it can be checked against
    guess_list.append(guess)

    placeholder_func()
    print(''.join(display))

    #Return message when game has been lost
    if stages_wrong == 0:
        print("***********************YOU LOSE**********************")
        exit()


print("***********************YOU WIN**********************")


