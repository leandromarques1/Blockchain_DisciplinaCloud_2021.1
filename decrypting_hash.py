from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

msg = "Welcome to channel".encode()
f_obj = Fernet(key)
encrypted_msg  =f_obj.encrypt(msg)
print(encrypted_msg)
decrypted_msg = f_obj.decrypt(encrypted_msg)
print(decrypted_msg)
