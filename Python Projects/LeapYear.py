#program to determine if given year is a leap year or not
def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        leap = True
    else:
        leap = False
    if year % 100 == 0:
        leap = False
    else:
        leap = True
    if leap % 400 == 0:
        leap = True
    else:
        leap = False
    return (print(f"Leap year is {leap}"))


year = int(input("What year would you like to give? "))
is_leap_year(year)
