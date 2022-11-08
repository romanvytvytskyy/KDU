a = int(input("Ennter number"))
operator = input("Enter operation(+, -, *, /)")
b = int(input("Ennter number"))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Ділити на 0 не можна")
else:
    print("Unknown operator")
