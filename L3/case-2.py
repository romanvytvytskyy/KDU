import math


number = int(input("Enter number: "))

match number:
    case 1:  # ? if number == 1:
        print("You choise 1")
    case 2:  # ? elifnumber == 2:
        print("You choise 2")
    case 3:  # ...
        print("You choise 3")
    case 4:
        print("You choise 4")
    case 5:
        print("You choise 5")
    case _:  # ? else:
        print("You choise nothing")


color = input("Enter you favorit color ").lower()

match color:
    case "red":
        print("My too")
    case "blue":
        print("oh good")
    case _:
        print("Uknown color")
