from getpass import getpass
from backend.dungeon.ossl import aes_decrypt, aes_encrypt

def encrypt(key, plaintext, ciphertext_file):
    # Encrypt plaintext 
    aes_encrypt(key, plaintext, ciphertext_file)

def decrypt(key, ciphertext_file):
    # To decode ciphertext
    aes_decrypt(key, ciphertext_file)

def kdf(password, salt):
    return password.encode()