import string
import random
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','*','(',')']
print("WELCOME TO RANDOM PASSWORD GENERATOR")

no_letters = int(input("How many letters would you like in your password: "))
no_numbers = int(input("How many digits would you like in your password: "))
no_symbols = int(input("How many symbols would you like in your password: "))

password_list = []
for _ in range(no_letters):
    password_list.append(random.choice(alphabets))
for _ in range(no_numbers):
    password_list.append(random.choice(numbers))
for _ in range(no_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print("Suggested Password is:",''.join(password_list))
