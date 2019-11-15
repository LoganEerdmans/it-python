import math
from banner import banner

def calculation(a, b, c):
    # If there's more than one value set to "0", it will print out a proper error message
    # saying that it's impossible to calculate the triangle. Otherwise, if only one value
    # is set to "0", then the calculations will begin.
    if ((a == 0) and (b == 0)) or ((a == 0) and (c == 0)) or ((b == 0) and (c == 0)):
        print("\nThere is too many unknown values to calculate a side of the triangle!")
    elif a == 0:
        x = b * b
        y = c * c
        z = y - x
        a = math.sqrt(z)
        print(f"Your missing side is a and its length is {a}.")
    elif b == 0:
        x = a * a
        y = c * c
        z = y - x
        b = math.sqrt(z)
        print(f"Your missing side is b and its length is {b}.")
    elif c == 0:
        x = a * a
        y = b * b
        z = x + y
        c = math.sqrt(z)
        print(f"Your missing side is c and its length is {c}.")
    else:
        print("\nUh, it looks like you already have all the sides of the triangle!")

if __name__ == "__main__":
    banner("PYTHAGOREAN CALCULATOR", "Logan Eerdmans")

    print("We will help you find the missing side of a right triangle. The lengths of the two\nlegs are 'a' and 'b', and the length of the hypotenuse is 'c'.")

    again = "Y"

    while again.capitalize() == "Y":

        print("\nPlease enter the length of each side, or leave it blank if you don't know")

        # This will grab each side of the right triangle, and if a side is left blank,
        # then it will not output a value error and will instead set the value to "0".
        try:
            a = float(input("a = "))
        except ValueError:
            a = 0
        try:
            b = float(input("b = "))
        except ValueError:
            b = 0
        try:
            c = float(input("c = "))
        except ValueError:
            c = 0

        # If you do "from pythag import calculation" in a different program, you can
        # actually put in numbers for a, b and c and get an answer there! Amazing!
        calculation(a, b, c)

        again = input("\nWould you like to calculate another triangle (Y/N)? ")

    print("\nThank you for using the Pythagorean Calculator.")