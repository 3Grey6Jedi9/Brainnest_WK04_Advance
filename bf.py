from app import Caesar_Cipher
import string
import itertools


with open('secret_word.txt') as f:
    secret_word = f.read()

with open('key') as f:
    secret_key = int(f.read())



class Brute_Force:


    british_alphabet = list(string.ascii_uppercase)
    special_characters = [' ', ',', '.', '+', '*', '-', '_', '@', '#', '%', '&', '$', '?']
    for s in special_characters:
        british_alphabet.append(s)

    def __init__(self): # I define the constructor (unnecessary in this case) in case I want to add something
        pass

    def generate_combinations(self, my_list, n):
        for i in range(1, n + 1):
            for combo in itertools.product(my_list, repeat=i):
                yield ''.join(combo)


    def attack(self):
        combinations = self.generate_combinations(Caesar_Cipher.british_alphabet, len(Caesar_Cipher.british_alphabet))
        guess = ''
        for i in combinations:
            print(i)
            if i == secret_word.upper():
                guess += i
                break

        key = ''

        for j in range(1, 76):
            if j == secret_key:
                key = j
                break

        print(f'''the encrypted password is:  {guess} and the key used is {key}, so using the encryptor
we can guess the password''')

        encryptor = Caesar_Cipher(key)

        print(f'The password is {encryptor.dencrypt(guess)}')




if __name__ == '__main__':
    hack_password = Brute_Force()
    hack_password.attack()























