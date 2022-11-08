# Напишіть програму, в якій користувач вводить
# значення температури, і, якщо це значення менше
# або дорівнює 0 градусів Цельсія, необхідно
# вивести повідомлення A cold, isn’t it?. Якщо ж
# температура становить більше 0 і менше 10
# градусів Цельсія повідомлення буде Cool., у
# інших випадках Nice weather we’re having..
# TODO  | 12.5   -   Nice weather we're having.
# TODO  | -5     -   A cold, isn't it?
# TODO  | 9      -   Cool.
temp = float(input("Enter temperature"))
if temp > 10:
    print("Nice weather we're having.")
elif 0 < temp < 10:
    print("Cool")
else:
    print("A cold, isn't it?")
