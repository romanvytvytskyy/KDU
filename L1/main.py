students = list()  # !empty
students = []  # !empty
students1 = ["Potter", "Whisely", "Gringer"]
# ?               0           1           2
# print(students)
print(students1)
students1.append("Malkoi")
print(students1)
print(students1[2:])
print(students1[:2])
#students1[:] = []
# print(students1)
#del students1[2]

user = {}
user = dict()
user = {
    "id": 123,
    "name": "Garry",
    "surname": "Potter",
    "age": 13,
    "address": 'Platporm 9 3/4'
}
print(user)
print(user["name"])
user["address"] = 'Backer srt., 5'
print(user)
user["phone"] = "+3801112345678"
print(user)
user["friends"] = students1[1:]
print(user)
del user["friends"]
print(user)
print(f'''Welcome to FB \n 
      Name: {user['name']}\n 
      Surname: {user["surname"]}
      Age: {user["age"]}
      Phone: {user["phone"]}
          ''')
