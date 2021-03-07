#WAP to find division of two numbwers
try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number"))
    z=x/y
    print("The Result: ",z)
except ValueError:
    print("Enter Numbers Only")
except ZeroDivisionError:
    print("A number divided by zero is zero")
finally:
    print("This is finally block")