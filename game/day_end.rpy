label day_end:
    "Welcome to where things will go for after day 1"
    "So, what'll it be?"
    menu:
        "Next day":
            "Time to start day 2"
            $ day_no += 1
            jump door
        "Quit":
            "Welp"

    