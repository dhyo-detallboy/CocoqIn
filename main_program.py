# APLIKASI COCOQIN
# BY ALIF DIO AF'ALLY
# main_program.py

import golongan_darah  # Mengimpor modul fungsi golongan darah

def main():
    opsi = "ya"

    while opsi.lower() == 'ya':
        # Tampilan awal program
        print("+-------------------------------------------------------------------------+")
        print("Selamat Datang di CocoqIn! :D ")
        print("+-------------------------------------------------------------------------+")
        print("Petunjuk Pengisian :")
        print("* Gunakan huruf kecil (o, a, b, ab)")
        print("+-------------------------------------------------------------------------+")

        # Input golongan darah penerima dan pendonor
        penerima = input("Golongan darah penerima : ").lower()
        pendonor = input("Golongan darah pendonor : ").lower()

        print("+-------------------------------------------------------------------------+")
        print("Hasil Pemeriksaan Kecocokan :")

        # Memanggil fungsi sesuai golongan darah penerima
        if penerima == 'o':
            golongan_darah.golongan_darah_O(penerima, pendonor)
        elif penerima == 'a':
            golongan_darah.golongan_darah_A(penerima, pendonor)
        elif penerima == 'b':
            golongan_darah.golongan_darah_B(penerima, pendonor)
        elif penerima == 'ab':
            golongan_darah.golongan_darah_AB(penerima, pendonor)
        else:
            print(f"Golongan darah penerima {penerima} tidak valid")

        print("+-------------------------------------------------------------------------+\n")
        opsi = input("Ingin melakukan pemeriksaan kembali? (ya/tidak): ").lower()

    print("Terima kasih sudah menggunakan aplikasi ini!")

# Memastikan main() dijalankan jika file ini dieksekusi secara langsung
if __name__ == "__main__":
    main()
