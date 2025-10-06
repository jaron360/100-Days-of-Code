import random
from wsgiref.validate import check_status

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

for i in chosen_word:
    print("_", end='')
print()

guess = input(f"Guess a letter: \n").lower()
display = ''

#Creating placeholder function, for printing the placeholder _____ for each letter
def placeholder_func():
    result = []
    placeholder = 0
    for i in chosen_word:
        placeholder += 1
        if i == guess:
            result.append(guess)
        else:
            result.append("_")
    return ''.join(result)

#Code for determining if user input is correct or not
if guess in chosen_word:
    print("Right!")
else:
    print("Wrong!")


variable = placeholder_func()
print(variable)
