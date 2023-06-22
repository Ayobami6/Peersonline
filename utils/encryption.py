from cryptography.fernet import Fernet


with open('key.key', 'rb') as key_file:
    encryption_key = key_file.read()


def encrypt_data(data):
    f = Fernet(encryption_key)
    encrypt_data = f.encrypt(data.encode()).decode()
    return encrypt_data


def decrypt_data(encrypted_data):
    f = Fernet(encryption_key)
    decrypted_data = f.decrypt(encrypted_data.encode()).decode()
    return decrypted_data
