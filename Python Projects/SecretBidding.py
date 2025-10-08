logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the secret auction program! ")

end_of_bid = False
bids = {}
bids_evaluation = []

while not end_of_bid:
    #Add each name/bid into the dictionary
    name = input("What is your name? ")
    bid = int(input(f"How much would you like to bid?\n$"))
    go_again = input("Would you like to add another bid? Type 'yes' or 'no'")
    bids[name] = bid
    print(bids)

    #repeat the program if user wants to go again
    if go_again == "yes".lower():
        #repeat the escape sequence 20 times, to clear the screen
        for i in range(20):
            print(chr(27) + "[2J")
        continue
    #Print the key and value pair for the highest bidder
    elif go_again == "no".lower():
        max_key = max(bids, key=bids.get)
        print(f"Winner is {max_key} with bid of ${bids[max_key]}")
    else:
        print("Invalid choice")
