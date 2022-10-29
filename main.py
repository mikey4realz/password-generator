#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_new_password = ""
for letter in range(0, nr_letters):
  #random_letter_index = random.randint(0, len(letters) - 1)
  random_letter = random.choice(letters)
  #easy_new_password += letters[random_letter_index]
  easy_new_password += random_letter
for symbol in range(0, nr_symbols):
  #random_symbol_index = random.randint(0, len(symbols) - 1)
  random_symbol = random.choice(symbols)
  #easy_new_password += symbols[random_symbol_index]
  easy_new_password += random_symbol
for number in range(0, nr_numbers):
  #random_number_index = random.randint(0, len(numbers) - 1)
  random_number = random.choice(numbers)
  #easy_new_password += numbers[random_number_index]
  easy_new_password += random_number
  
print(f"Easy level: Your password is {easy_new_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_length = nr_letters + nr_symbols + nr_numbers
hard_new_password = ""
password_characters = []

for i in range(0, nr_letters):
  #random_letter_index = random.randint(0, len(letters) - 1)
  #password_characters.append(letters[random_letter_index])
  password_characters.append(random.choice(letters)) 
  
for j in range(0, nr_symbols):
  #random_symbol_index = random.randint(0, len(symbols) - 1)
  #password_characters.append(symbols[random_symbol_index])
  password_characters.append(random.choice(symbols))
  
for k in range(0, nr_numbers):
  #random_number_index = random.randint(0, len(numbers) - 1)
  #password_characters.append(numbers[random_number_index])
  password_characters.append(random.choice(numbers))
  
for i in range(0, password_length):
  list_length = len(password_characters)
  random_number = random.randint(0,list_length-1)
  hard_new_password += password_characters[random_number]
  password_characters.pop(random_number)

print(f"Hard level: Your password is {hard_new_password}")