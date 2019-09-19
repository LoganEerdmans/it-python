from banner import banner
banner("DEEP THOUGHTS", "Logan Eerdmans")

def main():
    run_event_loop()

def run_event_loop():
    print("What do you want to do with your journal?")

    command = None
    journal_data = []

    while command != "x":
        command = input("[L]ist entries, [A]dd an entry, [E]xit: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() != "E":
            print("Sorry, but that's not a valid input!")

def list_entries(data):
    print("Your journal entries: ")

    entries = reversed(data)

    for num, entry in enumerate(entries):
        print(f"[{num + 1}] {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: ")
    data.append(entry)

main()