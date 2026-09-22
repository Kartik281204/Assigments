import random
import string
chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
# print(f"{chars}")
# print(f"{keys}")

# Decryption
plain_text = input("Enter whatever your message : ")
cipher_text = ""
for letters in plain_text:
    index = chars.index(letters)
    cipher_text += keys[index]
print(f"Your plain text was {plain_text}")
print(f"Your encrypted text is {cipher_text}")
# Decryption
cipher_text = input("Enter the message you want to decrypt : ")
plain_text = ""
for letters in cipher_text:
    index = keys.index(letters)
    plain_text += chars[index]
print(f"Your encrypted text is {cipher_text}")
print(f"Your plain text was {plain_text}")
