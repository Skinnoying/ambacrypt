# AmbaCrypt

**AmbaCrypt** adalah aplikasi enkripsi dan dekripsi file serta folder menggunakan algoritma **AES** dengan mode **CBC**. Aplikasi ini juga dilengkapi dengan sistem **pembuatan pengguna** dan **login**, yang memungkinkan pengguna untuk mengakses dan melindungi data mereka dengan password yang aman.

## Fitur Utama

1. **Pembuatan Kunci:**
   - Kunci untuk enkripsi dan dekripsi dihasilkan dengan menggunakan password dari pengguna dan **salt** acak, yang diproses menggunakan **PBKDF2** (Password-Based Key Derivation Function 2) dengan algoritma **SHA256**.

2. **Enkripsi dan Dekripsi:**
   - **Enkripsi:** Data (file atau folder) dienkripsi menggunakan algoritma **AES** dalam mode **CBC**, yang menjamin keamanan dengan padding dan penyembunyian data.
   - **Dekripsi:** File yang telah dienkripsi dapat didekripsi kembali menggunakan password yang benar untuk mengembalikan data ke bentuk aslinya.

3. **Sistem Pengguna:**
   - Pengguna dapat membuat akun dan mengakses aplikasi menggunakan **username** dan **password** yang aman, disimpan dalam file JSON.
   - Fungsi login untuk memverifikasi kredensial pengguna.

4. **Pengelolaan File dan Folder:**
   - Pengguna dapat mengenkripsi dan mendekripsi **file** atau **folder**.
   - Folder dan isinya akan diproses secara rekursif, mengenkripsi setiap file dalam folder.

5. **Keamanan:**
   - **Salt** dan **IV (Initialization Vector)** yang digunakan dalam proses enkripsi dihasilkan secara acak untuk meningkatkan keamanan.
   - Proses enkripsi dan dekripsi dilakukan menggunakan **padding PKCS7**, memastikan bahwa data sesuai dengan panjang blok yang diperlukan untuk AES.

6. **Clear Screen:**
   - Layar aplikasi dibersihkan sesuai dengan sistem operasi untuk menjaga antarmuka tetap bersih.

## Alur Kerja

1. Pengguna memulai aplikasi dan memilih untuk login atau membuat akun baru.
2. Setelah login, pengguna memilih untuk mengenkripsi atau mendekripsi file atau folder.
3. Data diproses dengan mengenkripsi atau mendekripsi file berdasarkan password yang diberikan.
4. Hasilnya disimpan kembali ke file yang sama setelah enkripsi/dekripsi selesai.

## Cara Penggunaan

1. Jalankan aplikasi.
2. Pilih opsi untuk login atau membuat akun baru.
3. Setelah berhasil login, pilih opsi untuk mengenkripsi atau mendekripsi file atau folder.
4. Masukkan path file atau folder yang akan diproses.
5. Aplikasi akan mengenkripsi atau mendekripsi file sesuai pilihan Anda.

## Instalasi

1. Clone repositori ini ke komputer Anda.

   ```bash
   git clone https://github.com/Skinnoying/ambacrypt
   cd ambacrypt

2. Install dependensi yang diperlukan menggunakan pip:

   ```bash
   pip install cryptography art

2. Jalankan kode :

   ```bash
   python ambacrypt.py
