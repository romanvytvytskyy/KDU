user = dict()
user = {}
user = {
    "id": 123,
    "name": "Garry",
    "surname": "Potter",
    "age": 13,
    "address": "Hoghwards"
}
print(user)
print(user.keys())
print(user.values())
print(user.items())
user["age"] = 14
print(user)
user["phone"] = "+380991234567"
print(user)
del user["address"]
print(user)
friends = ["Germiona", "Ron", "Hadrid"]
user["friends"] = friends
print(user)


users = {
    "user1": {"id": "1", "name": "Germiona",
              "surname": "Gringer"
              },
    "user2": {"id": "2", "name": "Ron",
              "surname": "Whisely"
              }
}
print(users["user2"]["surname"])
