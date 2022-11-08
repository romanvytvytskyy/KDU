num = int(input("Enter your number"))

match num:
    case 1:  # if num == 1:
        print("Your number 1")
    case 2:  # elif num == 2:
        print("Your number 2")
    case 3:  # ...
        print("Your number 3")
    case 4:
        print("Your number 4")
    case 5:
        print("Your number 5")
    case _:  # else:
        print("Your number undefined")


color = input("Enter color").lower()
match color:
    case "bright":
        print("Theme is bright")
    case "dark":
        print("Theme is dark")
    case _:
        print("Theme is contrast")
