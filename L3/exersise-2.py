from itertools import count
from operator import le
from random import randint

# ---------------
i = int(input("HOw much"))
word = input("Enter your name")
while i > 0:
    print("Hello, " + word)
    i -= 1

# -----------------
marks = [5, 5, 4, 4, 3, 5, 3, 5, 4, 2, 5]
i = 0
summa = 0
while i < len(marks):
    summa += marks[i]
    i += 1
avarage = summa/len(marks)
print(avarage)

# ------------------
i = 0
j = 15
while i < j:
    if i % 2 != 0:
        print(" "*(j-1), "*"*i)
    i += 1
    j -= 1

# -------------------
mass = []
i = 0
while i < 15:
    mass.append(randint(100, 500))
    i += 1
print(mass)
