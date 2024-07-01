# APLIKASI COCOQIN
# BY ALIF DIO AF'ALLY
# golongan_darah.py

# Fungsi Golongan Darah O
def golongan_darah_O(penerima, pendonor):
    # Definisi golongan darah yang dapat didonasikan oleh golongan darah O
    darah_support_O = ['o', 'a', 'b', 'ab']
    
    # Pengecekan kecocokan golongan darah
    if pendonor in darah_support_O:
        print(f"Golongan darah {pendonor} cocok untuk transfusi ke golongan darah {penerima}")
    else:
        print(f"Golongan darah {pendonor} tidak cocok untuk transfusi ke golongan darah {penerima}")

# Fungsi Golongan Darah A
def golongan_darah_A(penerima, pendonor):
    # Definisi golongan darah yang dapat didonasikan oleh golongan darah A
    darah_support_A = ['o', 'a']
    
    # Pengecekan kecocokan golongan darah
    if pendonor in darah_support_A:
        print(f"Golongan darah {pendonor} cocok untuk transfusi ke golongan darah {penerima}")
    else:
        print(f"Golongan darah {pendonor} tidak cocok untuk transfusi ke golongan darah {penerima}")

# Fungsi Golongan Darah B
def golongan_darah_B(penerima, pendonor):
    # Definisi golongan darah yang dapat didonasikan oleh golongan darah B
    darah_support_B = ['o', 'b']
    
    # Pengecekan kecocokan golongan darah
    if pendonor in darah_support_B:
        print(f"Golongan darah {pendonor} cocok untuk transfusi ke golongan darah {penerima}")
    else:
        print(f"Golongan darah {pendonor} tidak cocok untuk transfusi ke golongan darah {penerima}")

# Fungsi Golongan Darah AB
def golongan_darah_AB(penerima, pendonor):
    # Definisi golongan darah yang dapat didonasikan oleh golongan darah AB
    darah_support_AB = ['o', 'a', 'b', 'ab']
    
    # Pengecekan kecocokan golongan darah
    if pendonor in darah_support_AB:
        print(f"Golongan darah {pendonor} cocok untuk transfusi ke golongan darah {penerima}")
    else:
        print("Golongan darah pendonor tidak valid")

