import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_letters = []
selected_symbols = []
selected_numbers = []
for i in range(0, nr_letters):
    selected_letters.append(letters[random.randint(0, len(letters)-1)])
for i in range(0, nr_symbols):
    selected_symbols.append(symbols[random.randint(0, len(symbols)-1)])
for i in range(0, nr_numbers):
    selected_numbers.append(numbers[random.randint(0, len(numbers)-1)])
total_password = selected_letters + selected_symbols + selected_numbers
random_list = random.sample(total_password, len(total_password))
string_password = ""
for i in random_list:
    string_password += i
print(string_password)