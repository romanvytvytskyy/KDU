from functions import (one_col, one_row_one_space,
                       one_col_space, one_row_two_spaces,
                       surname, enter_date)

#day_of_birth = enter_date()


def run_all(a):
    one_row_one_space(*a)
    one_row_two_spaces(*a)
    one_col(*a)
    one_col_space(*a)


# run_all(day_of_birth)

s = input("Введіть ваше прізвище")
v = surname(s)
print("збережено у змінну", v)
print("Викликано функцією", surname(s))
