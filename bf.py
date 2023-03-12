from app import Caesar_Cipher
import string
import itertools

british_alphabet = list(string.ascii_uppercase)
special_characters = [' ', ',', '.', '+', '*', '-', '_', '@', '#', '%', '&', '$', '?']
for s in special_characters:
    british_alphabet.append(s)

#print(british_alphabet)

with open('secret_word.txt') as f:
    secret_word = f.read()

with open('key') as f:
    secret_key = int(f.read())

def generate_combinations(my_list, n):
    for i in range(1, n+1):
        for combo in itertools.product(my_list, repeat=i):
            yield ''.join(combo)

combinations = generate_combinations(british_alphabet, 39)

guess = ''


for i in combinations:
    print(i)
    if i == secret_word.upper():
        guess += i
        break



key = ''

for j in range(1,76):
    if j == secret_key:
        key = j
        break

print(f'''the encrypted password is:  {guess} and the key used is {key}, so using the encryptor
 we can guess the password''')

encryptor = Caesar_Cipher(key)

print(f'The password is {encryptor.dencrypt(guess)}')


