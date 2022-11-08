for i in range(1, 50, 5):
    print(i)

words = ["cat", "lion", "elephant"]
for word in words:
    print(word, len(word))


numbers = [1, 2, 6, 4, 8, 5, 4, 8, 5, 4, 8, 6, 2, 48]
for number in numbers:
    if number % 2 == 0:
        print(number)
