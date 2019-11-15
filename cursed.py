from banner import banner

banner("OH GOD OH HELP", "Logan Eerdmans")

number = 0
phrase = ""

while number != 20000:
    print(f"{phrase}")
    number += 1

    if number > 19000:
        phrase = "OH GOD OH HELP"
    elif number > 18500:
        phrase = "OH GOD OH HEL"
    elif number > 18000:
        phrase = "OH GOD OH HE"
    elif number > 17000:
        phrase = "OH GOD OH H"
    elif number > 16000:
        phrase = "OH GOD OH"
    elif number > 15000:
        phrase = "OH GOD O"
    elif number > 14000:
        phrase = "OH GOD"
    elif number > 13000:
        phrase = "OH GO"
    elif number > 12000:
        phrase = "OH G"
    elif number > 11000:
        phrase = "OH"
    elif number > 10000:
        phrase = "O"
    else:
        phrase = ""