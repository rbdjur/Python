def ask():
    while True:
        try:
            rec_input = int(input("Please enter a number:"))
            print("You entered", rec_input)
        except:
            print("That is not a number. Please enter a number")
            continue
        else:
            print("The square of the number is", rec_input **2)
            break
        finally:
            print("All done")

ask()