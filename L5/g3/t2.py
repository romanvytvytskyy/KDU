# Напишіть програму, яка виводить назви
# введених чисел. Користувач вводить
# ціле число. Якщо це число або 1 або
# 2 або 3, то виводиться повідомлення
# - назва числа, відповідно, One, Two,
# Three. В усіх інших випадках
# виводиться слово Unknown.
#   20  -   Unknown
#   1   -   One
#   2   -   Two
#   3   -   Three
number = int(input("Enter number"))
if number == 1:
    print("One")
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
else:
    print("Unknown")
