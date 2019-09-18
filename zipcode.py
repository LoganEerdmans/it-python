from banner import banner

banner("Zip Code Sorter", "Logan Eerdmans")

print("Welcome to the Newaygo County zip code sorter.")

ask = "Y"

while ask.capitalize() == "Y":

    zcode = int(input("Please enter a zip code: "))

    if zcode == 49309:
        area = "Bitley"
    elif zcode == 49312:
        area = "Brohman"
    elif zcode == 49337:
        area = "Croton"
    elif zcode == 49412 or zcode == 49413:
        area = "Fremont"
    elif zcode == 49327:
        area = "Grant"
    elif zcode == 49337:
        area = "Newaygo"
    elif zcode == 49349:
        area = "White Cloud"
    else:
        area = "None"
        print(f"The zip code {zcode} is not in Newaygo County.")

    if area is "None":
        print()
    else:
        print(f"The zip code {zcode} is for {area}.")

    ask = input("Would you like to enter another zip code (Y/N)? ")

print("\nThank you for using the Newaygo County Zip Code Sorter. Goodbye!")