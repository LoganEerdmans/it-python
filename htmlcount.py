import os
from banner import banner

banner("HTML Tag Counter", "Logan Eerdmans")

print("Welcome to the HTML Tag Counter!")

again = "Y"

def load(filename):
    data = []
    if os.path.exists(filename):
        with open(filename) as f:
            for line in f.readlines():
                data.append(line)
    return data

def taggrab(line):
    count = 0
    tagcheck = "<"
    for char in line:
        if char == tagcheck:
            count += 1
    return count

def taggrab2(line):
    count = 0
    tagcheck_previous = None
    for x in line:
        if x == "/" and tagcheck_previous == "<":
            count -= 1
        tagcheck_previous = x
    return count

while again.capitalize() == "Y":
    filename = input("Please enter the name of an HTML file: ")
    data = load(filename)

    tagcount = 0
    for line in data:
        tagcount += taggrab(line)
        tagcount += taggrab2(line)

    print(f"The file {filename} contains {tagcount} tags.\n")

    again = input("Would you like to count another HTML file (Y/N)? ")

print("Thank you for using the HTML Tag Counter. Goodbye!")