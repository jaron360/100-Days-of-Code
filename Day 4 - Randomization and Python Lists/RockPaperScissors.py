import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(rock, paper, scissors)
print("Welcome to rock, paper, scissors!")

user_input = input("Would you like to go Rock, Paper, or Scissors? ")
computer_list = ["rock", "paper", "scissors"]
computer_answer = random.choice(computer_list)

def rock():
    if user_input == "rock" and computer_answer == "paper":
        print(f"Computer chose {computer_answer}")
        print("You Lose!")
        exit()
    elif user_input == "rock" and computer_answer == "scissors":
        print(f"Computer chose {computer_answer}")
        print("You Win!")
        exit()
    elif user_input == "rock" and computer_answer == "rock":
        print(f"Computer chose {computer_answer}")
        print("Tie Game!")
        exit()
    else:
        print("Something went wrong")

def paper():
    if user_input == "paper" and computer_answer == "paper":
        print(f"Computer chose {computer_answer}")
        print("Tie Game!")
        exit()
    elif user_input == "paper" and computer_answer == "scissors":
        print(f"Computer chose {computer_answer}")
        print("You Lose!")
        exit()
    elif user_input == "paper" and computer_answer == "rock":
        print(f"Computer chose {computer_answer}")
        print("You Win!")
        exit()
    else:
        print("Something went wrong")

def scissors():
    if user_input == "scissors" and computer_answer == "paper":
        print(f"Computer chose {computer_answer}")
        print("You Win!")
        exit()
    elif user_input == "scissors" and computer_answer == "scissors":
        print(f"Computer chose {computer_answer}")
        print("Tie Game!")
        exit()
    elif user_input == "scissors" and computer_answer == "rock":
        print(f"Computer chose {computer_answer}")
        print("You Lose!")
        exit()
    else:
        print("Something went wrong")


if user_input == "rock":
    rock()
elif user_input == "paper":
    paper()
else:
    scissors()
