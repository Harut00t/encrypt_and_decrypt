import random
import string

#The variable containing different keys, numbers, brackets, etc.
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#Encryption
plain_text = input("Please enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")

#Decryption
cipher_text = input("Please enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"decrypted message : {plain_text}")
print(f"original message : {cipher_text}")
