from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from art import text2art
import os
import getpass
import json

# Fungsi untuk menghasilkan kunci dari password
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Fungsi untuk mengenkripsi data
def encrypt_file(password, file_path):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        return
    except PermissionError:
        print(f"Tidak memiliki izin untuk membaca file {file_path}!")
        return

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    try:
        with open(file_path, 'wb') as f:
            f.write(salt + iv + encrypted_data)
    except PermissionError:
        print(f"Tidak memiliki izin untuk menulis ke file {file_path}!")
        return

    print(f"File {file_path} telah dienkripsi.")

# Fungsi untuk mendekripsi data
def decrypt_file(password, file_path):
    try:
        with open(file_path, 'rb') as f:
            salt = f.read(16)
            iv = f.read(16)
            encrypted_data = f.read()
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        return
    except PermissionError:
        print(f"Tidak memiliki izin untuk membaca file {file_path}!")
        return

    key = generate_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    try:
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)
    except PermissionError:
        print(f"Tidak memiliki izin untuk menulis ke file {file_path}!")
        return

    print(f"File {file_path} telah didekripsi.")

# Fungsi untuk mengenkripsi folder
def encrypt_folder(password, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(password, file_path)

# Fungsi untuk mendekripsi folder
def decrypt_folder(password, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(password, file_path)

# Fungsi untuk membuat pengguna baru
def create_user():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    user_data = {"username": username, "password": password}
    
    with open("users.json", "a") as f:
        json.dump(user_data, f)
        f.write("\n")
    print("Pengguna berhasil dibuat.")

# Fungsi untuk memverifikasi pengguna dan sesi
def verify_user():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    
    with open("users.json", "r") as f:
        for line in f:
            user_data = json.loads(line.strip())
            if user_data["username"] == username and user_data["password"] == password:
                return username, password
    print("Username atau password salah!")
    return None, None

# Fungsi untuk login pengguna atau buat akun jika belum ada
def login_or_register():
    print("Selamat datang di AmbaCrypt!")
    print("1. Login")
    print("2. Register")
    choice = input("Pilih opsi (1/2): ")

    if choice == '1':
        username, password = verify_user()
        if username is not None:
            return username, password
        else:
            return login_or_register()
    elif choice == '2':
        create_user()
        return login_or_register()
    else:
        print("Pilihan tidak valid!")
        return login_or_register()

#Fungsi untuk Clear Screen
def clear_screen():
    # Menghapus layar berdasarkan sistem operasi
    if os.name == 'nt':  # Untuk Windows
        os.system('cls')
    else:  # Untuk Linux/macOS
        os.system('clear')
    
# Fungsi utama untuk interaksi pengguna
def main():
    ascii_art = text2art("AmbaCrypt")
    print(ascii_art)

    username, password = login_or_register()
    clear_screen()
    
    ascii_art = text2art("AmbaCrypt")
    print(ascii_art)

    print("Pilih opsi:")
    print("1. Enkripsi file")
    print("2. Dekripsi file")
    print("3. Enkripsi folder")
    print("4. Dekripsi folder")
    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid!")
        return

    path = input("Masukkan path dari file atau folder: ")

    if not os.path.exists(path):
        print("Path tidak ditemukan!")
        return

    if choice == '1':
        if os.path.isfile(path):
            encrypt_file(password, path)
        else:
            print("Path yang dimasukkan bukan file!")
    elif choice == '2':
        if os.path.isfile(path):
            decrypt_file(password, path)
        else:
            print("Path yang dimasukkan bukan file!")
    elif choice == '3':
        if os.path.isdir(path):
            encrypt_folder(password, path)
        else:
            print("Path yang dimasukkan bukan folder!")
    elif choice == '4':
        if os.path.isdir(path):
            decrypt_folder(password, path)
        else:
            print("Path yang dimasukkan bukan folder!")

if __name__ == "__main__":
    main()
