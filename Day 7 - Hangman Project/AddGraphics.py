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

stages_wrong = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

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

    #Code for determining if user input is correct or not
    if guess in chosen_word:
        print("Right!")
    else:
        print("Wrong!")
        stages_wrong -= 1
        print(stages[stages_wrong])

    placeholder_func()
    print(''.join(display))

    if stages_wrong == 0:
        print("Game Over, You Lose!")
        exit()

print("You Win!!")
