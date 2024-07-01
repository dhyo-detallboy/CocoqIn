# APLIKASI COCOQIN
## BY ALIF DIO AF'ALLY

### Deskripsi Proyek
CocoqIn adalah aplikasi sederhana untuk memeriksa kecocokan golongan darah antara penerima dan pendonor. Proyek ini terdiri dari dua file utama:
- `main_program.py`: Program utama yang mengelola interaksi dengan pengguna dan pemanggilan fungsi golongan darah.
- `golongan_darah.py`: Modul yang berisi definisi fungsi untuk memeriksa kecocokan golongan darah.

### Fungsi Utama
- **golongan_darah_O**: Memeriksa kecocokan golongan darah jika penerima memiliki golongan darah O.
- **golongan_darah_A**: Memeriksa kecocokan golongan darah jika penerima memiliki golongan darah A.
- **golongan_darah_B**: Memeriksa kecocokan golongan darah jika penerima memiliki golongan darah B.
- **golongan_darah_AB**: Memeriksa kecocokan golongan darah jika penerima memiliki golongan darah AB.

### Cara Penggunaan
1. Program akan menyapa pengguna dengan pesan selamat datang dan petunjuk pengisian.
2. Pengguna diminta untuk memasukkan golongan darah penerima dan pendonor dalam format huruf kecil (o, a, b, ab).
3. Hasil pemeriksaan kecocokan golongan darah akan ditampilkan.
4. Pengguna dapat memilih untuk melakukan pemeriksaan kembali atau mengakhiri aplikasi.

### Contoh Penggunaan
Misalnya, untuk memeriksa kecocokan golongan darah antara penerima O dan pendonor A:
```plaintext
+-------------------------------------------------------------------------+
Selamat Datang di CocoqIn! :D 
+-------------------------------------------------------------------------+
Petunjuk Pengisian :
* Gunakan huruf kecil (o, a, b, ab)
+-------------------------------------------------------------------------+
Golongan darah penerima : o
Golongan darah pendonor : a
+-------------------------------------------------------------------------+
Hasil Pemeriksaan Kecocokan :
Golongan darah a cocok untuk transfusi ke golongan darah o
+-------------------------------------------------------------------------+

Ingin melakukan pemeriksaan kembali? (ya/tidak): tidak
Terima kasih sudah menggunakan aplikasi ini!
