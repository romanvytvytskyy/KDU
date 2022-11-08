user = {
    "id": 123,
    "name": "Garry",
    "surname": "Potter",
    "age": 13,
    "addres": "Hoghwards",
}
print(user)
user["phone"] = "+380991234567"
print(user)
print(user.keys())
print(user.values())
print(user.items())
user["age"] = 14
print(user)
friends = ["Gringer", "Whisely", "Gagrid"]
user["friends"] = friends
print(user)
del user["addres"]
print(user)
