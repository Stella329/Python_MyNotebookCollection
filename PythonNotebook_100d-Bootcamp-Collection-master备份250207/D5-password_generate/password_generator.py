#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#TODO Easy Level - Order not randomnized: e.g. 4 letter, 2 symbol, 2 number = hUys&#25
pw_letter = random.choices(letters, k=nr_letters)
pw_symbols = random.choices(symbols, k=nr_symbols)
pw_numbers = random.choices(numbers, k=nr_numbers)

pw_final = pw_letter+pw_symbols+pw_numbers  #type: list

#TODO Hard Level - Order of characters randomised: e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P --打乱顺序
random.shuffle(pw_final)

#用for_loop将list转化为string: METHOD 1
pw_string = ''
for x in pw_final:
  pw_string += ''+x
print('your password is:')
print (pw_string)

#METHOD 2: 
# password = ""
# for char in password_list:
#   password += char

