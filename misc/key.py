from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
from utils.encryption import encrypt_data, decrypt_data, encryption_key
load_dotenv()

some_key = "12999dbgsd"
encrypted_key = encrypt_data(some_key)
decrypted_key = decrypt_data(encrypted_key)
# # key = os.getenv("ENCRYPTION_KEY")
# encryption_key = Fernet.generate_key()
# with open('key.key', 'wb') as key_file:
#     key_file.write(encryption_key)


print(decrypted_key)
# print(encryption_key)
