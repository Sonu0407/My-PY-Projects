import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*','(', ')', '-', '_', '=', '+', '{', '}','[', ']', '|', '\\', ':', ';', '"', "'",'<', '>', ',', '.', '?', '/', '`', '~']

print("Welcome to the PyPassword Generator")
en_letters = int(input("How many letters would you like in your password?\n"))
en_symbols = int(input("How many symbols would you like?\n"))
en_numbers = int(input("How many numbers would you like?\n"))

# hard level
password = ""

for char in range(1, en_letters + 1):
    password += random.choice(letters)

for symbol in range(1, en_symbols + 1):
    password += random.choice(symbols)

for number in range(1, en_numbers + 1):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
print("Your Password is " + final_password)








