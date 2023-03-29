#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string

def substitution_cipher(plaintext, key, mode):
    # valid key
    if set(key) != set(string.ascii_lowercase):
        raise ValueError("Key must contain all letters of the alphabet.")

    # Create the substitution alphabet
    alphabet = string.ascii_lowercase
    sub_alphabet = str.maketrans(alphabet, key)

    # Encrypt or decrypt the plaintext
    if mode == "encrypt":
        ciphertext = plaintext.lower().translate(sub_alphabet)
        return ciphertext
    elif mode == "decrypt":
        plaintext = plaintext.lower().translate(str.maketrans(key, alphabet))
        return plaintext
    else:
        raise ValueError("Mode must be either 'encrypt' or 'decrypt'.")


# Example usage
plaintext = input('PlainText: ')
key = input('The key: ')
ciphertext = substitution_cipher(plaintext, key, "encrypt")
print("Ciphertext:", ciphertext)
decrypted_plaintext = substitution_cipher(ciphertext, key, "decrypt")
print("Decrypted plaintext:", decrypted_plaintext)

