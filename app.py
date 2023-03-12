import string
import datetime
import sys

class Caesar_Cipher():

    british_alphabet = list(string.ascii_uppercase)
    special_characters = [' ', ',', '.', '+', '*', '-', '_', '@', '#', '%', '&', '$', '?']
    for s in special_characters:
        british_alphabet.append(s)
    british_alphabet = british_alphabet*2

    def __init__(self, key):
        self.key = key

    def host(self):
        current_time = datetime.datetime.now()
        moment = ''
        if  6 <= current_time.hour and current_time.hour < 12:
            moment = 'morning'
        elif 12 <= current_time.hour and current_time.hour < 18:
            moment = 'afternoon'
        elif 18 <= current_time.hour and current_time.hour < 22:
            moment = 'evening'
        elif  22 <= current_time.hour and current_time.hour < 6:
            moment = 'night'
        return f'''\nGood {moment}, I will help you encrypting or decrypting the message you desire'''


    def encrypt(self, word):
        ciphertext = []
        ciphertext_string = ''
        for w in word.upper():
            for l in Caesar_Cipher.british_alphabet:
                if w == l:
                    initial_index = Caesar_Cipher.british_alphabet.index(l)
                    final_index = initial_index + self.key
                    ciphertext.append(Caesar_Cipher.british_alphabet[final_index])
                    break
                else:
                    continue
        for w in ciphertext:
            ciphertext_string += w
        with open ('secret_word.txt','w') as f:
            f.write(ciphertext_string)
        return ciphertext_string.capitalize()

    def dencrypt(self, ciphertext):
        original_word = []
        original_word_str = ''
        for w in ciphertext.upper():
            for l in Caesar_Cipher.british_alphabet:
                if w == l:
                    initial_index = Caesar_Cipher.british_alphabet.index(l)
                    final_index = initial_index - self.key
                    original_word.append(Caesar_Cipher.british_alphabet[final_index])
                    break
                else:
                    continue
        for w in original_word:
            original_word_str += w
        return original_word_str.capitalize()

    def proceed(self):
        connected = True
        while connected or ValueError:
            print(self.host())
            try:
                choice = input('\nWhat would you like to do [enter "e" for encryption or "d" for decryption]? ').lower()
                if choice not in ['e','d']:
                    raise ValueError('Please you must enter "e" or "d"')
            except ValueError as err:
                print(f'{err}')
            else:
                if choice == 'e':
                    try:
                        secret_word = input('Would you be so kind to entering the secret word please: ')
                        for w in secret_word:
                            if w.upper() not in Caesar_Cipher.british_alphabet:
                                raise ValueError(f'Your password must be composed by letters from the British Alphabet and you can add these special characters {Caesar_Cipher.special_characters} ')
                            else:
                                continue
                    except ValueError as err:
                        print(f'{err}')
                    else:
                        ciphertext = self.encrypt(secret_word)
                        print(f'''Your secret word is now encrypted and I also created a backup in case you forget the ciphertext,
which is {ciphertext}''')
                elif choice == 'd':
                    try:
                        ciphert = input('''I will need you to enter the ciphertext so I can decrypt it.
Or if you just press enter I will use the ciphertext store in the backup if there is any. ''')
                        for w in ciphert:
                            if w.upper() not in Caesar_Cipher.british_alphabet and w != '':
                                raise ValueError(f'Your password must be composed by letters from the British Alphabet and you can add these special characters {Caesar_Cipher.special_characters}')
                            else:
                                continue
                    except ValueError as err:
                        print(f'{err}')
                    else:
                        if ciphert == '':
                            with open('secret_word.txt', 'r') as f:
                                ciphert = f.read()
                            original_w = self.dencrypt(ciphert)
                            print(f'Very well here is the secret word {original_w}')
                        else:
                            original_word = self.dencrypt(ciphert)
                            print(f'Very well here is the secret word {original_word}')
                do_now = input('''What would you like to do now? If you wish to restart the app press "n" and if you wish to exit the program
press any other key: ''')
                if do_now == 'n':
                    connected = True
                else:
                    sys.exit()













if __name__ == '__main__':

    while ValueError:
        try:
            key = int(input('Enter the key so I can configurate the encryptor (Enter 0 if you want to use the key stored): '))
            if key == 0:
                with open('key') as f:
                    key = int(f.read())
            if key not in range(1,76):
                raise ValueError
        except ValueError:
            print('You must enter an integer lower than 76')
            pass
        else:
            with open('key', 'w') as f:
                f.write(str(key))
            encryptor = Caesar_Cipher(key)
            encryptor.proceed()



# Do not set a password with more than 5 characters for processing time reasons



