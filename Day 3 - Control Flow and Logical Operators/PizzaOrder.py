#Program to calculate the cost of pizza given the following:
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
    print(f"This will cost ${price}")
    exit()
if size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
    print(f"This will cost ${price}")
    exit()
if size == "L":
    price += 25
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
    print(f"This will cost ${price}")
    exit()
else:
    print("Please enter a valid size ")
