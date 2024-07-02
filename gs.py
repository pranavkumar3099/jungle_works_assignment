def guess():
    print("Welcome to Guess Game!")
    print("Think of a number between 1 and 400.")
    input("Press Enter when ready...")

    l = 1
    h = 400
    t = 0

    while l <= h:
        g = (l + h) // 2
        t += 1

        print(f"My guess: {g}.")
        f = input("Is it high (H), low (L), or correct (C)? ").strip().upper()

        if f == "C":
            print(f"I got it! Your number is {g}. It took me {t} tries.")
            return
        elif f == "H":
            h = g - 1
        elif f == "L":
            l = g + 1
        else:
            print("Invalid input. Please enter H, L, or C.")

    print("I couldn't guess your number. Maybe a mistake?")