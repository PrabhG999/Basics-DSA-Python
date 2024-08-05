import sys

number = input("Enter a number: ")

if float(number) <= 100.00:

    if 100 >= float(number) >= 90:
        Grade = "A+"
        print(f"Your Grade is {Grade}  for these Marks {number}")
    elif 90 >= float(number) >= 80:
        Grade = "A"
        print(f"Your Grade is {Grade} for these Marks {number}")
    elif 80 >= float(number) >= 70:
        Grade = "B+"
        print(f"Your Grade is {Grade} for these Marks {number}")
    elif 70 >= float(number) >= 60:
        Grade = "B"
        print(f"Your Grade is {Grade} for these Marks {number}")
    elif 60 >= float(number) >= 50:
        Grade = "C+"
        print(f"Your Grade is {Grade} for these Marks {number}")
    elif 50 >= float(number) >= 40:
        Grade = "D+"
        print(f"Your Grade is {Grade} for these Marks {number}")
    elif 40 >= float(number) >= 30:
        Grade = "E+"
        print(f"Your Grade is {Grade} for these Marks {number}")
    else:
        if float(number) >= 0:
            Grade = "F"
            print(f"Your Grade is {Grade} for these Marks {number}")
        elif float(number) < 0:
            sys.exit("Your Grade is out of range")
if float(number) >= 100:
    sys.exit("Your Marks should be less than or equal to 100")

