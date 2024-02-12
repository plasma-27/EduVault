from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import mysql.connector

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # AES encryption
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CTR(), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    return encrypted_data

def store_in_mysql(encrypted_data):
    connection = mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    cursor = connection.cursor()

    # Assuming you have a table with a column named 'encrypted_data' of type BLOB
    insert_query = "INSERT INTO encrypted_files (encrypted_data) VALUES (%s)"
    cursor.execute(insert_query, (encrypted_data,))
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    file_path = 'your_file_path'
    key = b'your_AES_key'  # 16, 24, or 32 bytes
    encrypted_data = encrypt_file(file_path, key)
    store_in_mysql(encrypted_data)
