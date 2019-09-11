def banner(subject, banner):
    subject_length = len(subject)
    by_line = f"By (author)"
    by_line_length = len(by_line)
    banner_length = max(subject_length, by_line_length) + 4

    print(f"{'=' * banner_length}")
    print(f"{subject:^{banner_length}}")
    print(f"{by_line:^{banner_length}}")
    print(f"{'=' * banner_length}")
    print("")

banner("BANNER", "Logan Eerdmans")
subject = input("What's the subject? ")
author = input("Who's the author? ")
banner(subject, author)
