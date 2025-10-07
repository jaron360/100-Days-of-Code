#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
#1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
#2. Then check for the number of times the letters in the word LOVE occurs.   
#3. Then combine these numbers to make a 2 digit number and print it out.  

#Example Input 
#calculate_love_score("Kanye West", "Kim Kardashian")
#Example Output
#42

name1 = input("What is the first name? ")
name2 = input("What is the second name? ")

def calculate_love_score(a, b):
    combined_names = (a + b)
    combined_names_lower = combined_names.lower()
    name1_list = 0
    if "t" in combined_names_lower:
        name1_list += 1
    if "r" in combined_names_lower:
        name1_list += 1
    if "u" in combined_names_lower:
        name1_list += 1
    if "e" in combined_names_lower:
        name1_list += 1

    name2_list = 0
    if "l" in combined_names_lower:
        name2_list += 1
    if "o" in combined_names_lower:
        name2_list += 1
    if "v" in combined_names_lower:
        name2_list += 1
    if "e" in combined_names_lower:
        name2_list += 1
    total = int(str(name1_list)) + int(str(name2_list))
    print(name1_list, end='')
    print(name2_list)

calculate_love_score(name1, name2)
