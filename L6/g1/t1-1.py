from t1 import enter_date, one_col, one_col_space, one_row_one_space, one_row_two_spaces
import t1

a = (enter_date())
print(a)
one_row_one_space(*a)
one_row_two_spaces(*a)
one_col(*a)
one_col_space(*a)


def print_all():
    print("Run all")
    one_col(*enter_date())
    one_row_one_space(*enter_date())


print_all()
