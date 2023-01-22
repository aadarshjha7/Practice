import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the Password Generator!")
nr_letters = int(input("Total letters?\n"))
nr_symbols = int(input("Total symbols?\n"))
nr_numbers = int(input("Total numbers?\n"))

password = ""
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password = password + random_letter
# print(password)

for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password = password + random_symbol
# print(password)

for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password = password + random_number
# print(password)

password = list(password)
random.shuffle(password)
# print(password)
password = "".join(password)
print(password)
