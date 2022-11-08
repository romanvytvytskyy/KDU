# Напишіть програму, в якій користувач
# вводить пароль і якщо він співпадає
# із наперед визначеним паролем для
# цього користувача, то виводиться
# повідомлення Password accepted..
# У іншому випадку повідомлення буде
# Sorry, that is the wrong password
# ? starlink
#! 12345
password = input("Enter password")
true_password = "starlink"
if password == true_password:
    print("Password accepted..")
else:
    print("Sorry, that is the wrong password")
