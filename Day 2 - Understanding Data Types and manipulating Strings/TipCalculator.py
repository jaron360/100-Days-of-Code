#Tip calculator project
print("Welcome to the tip calculator.")

#variables
total_bill = float(input("What was the total bill? "))
tip = int(input("How much would you like to tip? 10, 12, or 15? "))
split = int(input("How many people will split the bill? "))
bill_with_tip = tip / 100 * total_bill + total_bill

final_bill = round(bill_with_tip / split, 2)

#Final output
print(f"each person should pay: ${final_bill}")
