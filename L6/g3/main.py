from functions import one_col, one_col_space, one_row_one_space, one_row_two_spaces, surname, enter_date

day_of_birt = enter_date()


def run_all(a):
    one_row_one_space(*a)
    one_row_two_spaces(*a)
    one_col(*a)
    one_col_space(*a)


one_col(day_of_birt)


run_all(day_of_birt)

s = input("Введіть Ваше прізвище")
v = surname(s)
print("Через змінну", v)
print("Через функцію", surname(s))

print(surname(input("Введіть прізвище")))
