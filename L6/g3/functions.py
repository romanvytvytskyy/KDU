def enter_date():
    day = input("Enter day of birth")
    month = input("Enter month of birth")
    year = input("Enter year of birth")
    return day, month, year


def one_row_one_space(day, month, year):
    print(f"{day} {month} {year}")


def one_row_two_spaces(day, month, year):
    print(f"day:{day}  month:{month}  year:{year}")


def one_col(a, b, c):
    print(f"{a}\n{b}\n{c}")


def one_col_space(a, b, c):
    print(f"{a}\n\n{b}\n\n{c}")


def surname(surname):
    surname = f"Ви ввели прізвище {surname}"
    return surname
