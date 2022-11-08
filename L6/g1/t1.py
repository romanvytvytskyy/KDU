def enter_date():
    day = input("Enter day")
    month = input("Enter month")
    year = input("Enter year")
    return day, month, year


def one_row_one_space(d, m, y):
    print("Run one_row_one_space")
    print(f"{d} {m} {y}")


def one_row_two_spaces(d, m, y):
    print("Run one_row_two_spaces")
    print(f"{d}  {m}  {y}")


def one_col(a, b, c):
    print("Run one_col")
    print(f"{a}\n{b}\n{c}")


def one_col_space(a, b, c):
    print("Run one_col_space")
    print(f"{a}\n\n{b}\n\n{c}")


def surname(surname):
    print(f"Ви ввели прізвище {surname}")
