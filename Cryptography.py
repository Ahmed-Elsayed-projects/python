import cryptography.fernet
import time

def generate_key():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    return key


def encrypting(file_path, key_string):
    with open(file_path, 'rb') as original_file:
        original = original_file.read()

    f = cryptography.fernet.Fernet(key_string)
    encrypted = f.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypting(file_path, key_string):
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    f = cryptography.fernet.Fernet(key_string)
    decrypted = f.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


#enc_or_dec = input("Encrypting or Decrypting:\t")
#file_name = input("Enter the name of the file:\t")

"""if enc_or_dec.lower() == 'encrypting':
    want_key = input('Do you want to generate a key? Y/N\t')
    if want_key.lower() == 'y':
        with open('key.txt', 'wb') as file:
            key = generate_key()
            file.write(key)
    elif want_key.lower() == 'n':
        key = input("Enter your key:\t")
    else:
        print('Something went wrong!')
        time.sleep(8)
        exit()
    encrypting(file_name, key)

elif enc_or_dec.lower() == 'decrypting':
    key = input("Enter your key:\t")
    try:
        decrypting(file_name, key)
    except:
        print('Something went wrong!')
        time.sleep(8)
        exit()
"""

encrypting(r'project\file.py', b'3gZ2d7Hz2cJXxOTJEsekj1dAB2l9Y8zGmVQp1cne_d8=')