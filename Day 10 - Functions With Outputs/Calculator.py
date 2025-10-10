logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print("Welcome to the calculator program.")

#Take the numbers which user would like to calculate and store the values as number_1 and number_2
first_calculation = True
result = []
user_not_done = True
number_1 = 0

while user_not_done:
    if first_calculation == True:
        number_1 = float(input("What is the first number you would like to calculate? "))
        calculation = input("Which operation would you like to perform? +, -, *, / ")
        number_2 = float(input("What is the second number you would like to calculate? "))
        if calculation in operations:
            result = operations[calculation](number_1, number_2)
            print(f"{number_1} {calculation} {number_2} = {result}")
        else:
            print("invalid calculation option")
            exit()
    if first_calculation == False:
        calculation = input("Which operation would you like to perform? +, -, *, / ")
        number_2 = float(input("What is the second number you would like to calculate? "))
        if calculation in operations:
            result = operations[calculation](number_1, number_2)
            print(f"{number_1} {calculation} {number_2} = {result}")
        else:
            print("invalid calculation option")
            exit()

    go_again = input("Would you like to calculate using the previous result? yes or no: ")
    if go_again == "no":
        if input("Another calculation? yes or no: ") == "no":
            user_not_done = False
            print(f"\nThank you, bye!")
            exit()
        else:
            continue
    if go_again == "yes":
        number_1 = result
        first_calculation = False
        continue
