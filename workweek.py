day = input("Enter day : ")

match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("End of work week")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Midweek day")
