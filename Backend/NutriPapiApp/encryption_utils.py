from cryptography.fernet import Fernet
from NutriPapi.settings import ENCRYPTION_KEY

# Encryption function
def encrypt_data(data):
    cipher_suite = Fernet(ENCRYPTION_KEY)
    return cipher_suite.encrypt(data.encode())

# Decryption function
def decrypt_data(encrypted_data):
    cipher_suite = Fernet(ENCRYPTION_KEY)
    return cipher_suite.decrypt(encrypted_data).decode()