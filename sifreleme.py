from cryptography.fernet import Fernet

def generate_key():
    """
    Rastgele bir anahtar oluşturur.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Mesajı şifreler.
    """
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Şifreli mesajı çözer.
    """
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Anahtar oluştur
key = generate_key()

# Şifrelenecek mesaj
message_to_encrypt = "Merhaba, bu mesaj şifrelenecek!"

# Mesajı şifrele
encrypted_message = encrypt_message(message_to_encrypt, key)
print(f"Şifrelenmiş Mesaj: {encrypted_message}")

# Şifreli mesajı çöz
decrypted_message = decrypt_message(encrypted_message, key)
print(f"Çözülmüş Mesaj: {decrypted_message}")
