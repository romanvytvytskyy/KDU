from random import randint
'''
name = input("Enter youir name")
num = int(input("How mach?"))

while num > 0:
    print("Hello, "+name+"!")
    num -= 1


marks = [5, 4, 3, 3, 2, 5, 5, 4, 4, 5, 2, 3, 5, 4]
i = 0
summ = 0
while i < len(marks):
    summ += marks[i]
    i += 1
average = summ/len(marks)
print(average)
'''
i = 1
while i < 9:
    print("*"*i)
    i += 1

i = 1
j = 9
while j > 0:
    print(" "*(j-1), "*"*i)
    i += 1
    j -= 1

i = 1
j = 9
while j > 0:
    if i % 2 != 0:
        print(" "*(j//2), "*"*i)
    i += 1
    j -= 1

mas = []
i = 0
while i < 15:
    mas.append(randint(100, 500))
    i += 1
print(mas)
