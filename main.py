import pyfiglet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os

# Deklarasi variabel global untuk menampung value dari hasil dekripsi yang dilakukan nanti
hasilDecrypted = ''

# Fungsi Enkripsi Teks
def encryptTeks(data, publicKeyFile):
    
    fileName = 'data'
    fileExtension = 'txt'

    # Konversi data ke bytes
    data = bytes(data)

    # membaca public key dari file
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()
    
    # membuat public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # melakukan proses enkripsi pada sesion key dengan menggunakan public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # melakukan proses enkripsi pada data yang diinput dengan menggunakan session key yang susah dibuat
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []


    # menyimpan hasil enkripsi ke dalam sebuah file
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print('Hasil Enkripsi tersimpan di dalam file ' + encryptedFile)
    

# Fungsi Dekripsi Teks
def decryptTeks(dataFile, privateKeyFile):

    # membaca private key dari file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)


    # membaca data dari file
    with open(dataFile, 'rb') as f:

        # membaca session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    
    # mendekripsikan session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # melakukan proses dekripsi pada data dengan session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    global hasilDecrypted
    hasilDecrypted = data


#Generate ASCII TEXT untuk menu pada variabel pesan1

pesan1 = pyfiglet.figlet_format("UAS KRIPTOGRAFI", font = "slant", width= 250)
pesan2 = pyfiglet.figlet_format("KELAS CR001", font = "slant", width= 250)

print ("\n"+ pesan1)
print (pesan2)
input("Pencet tombol apapun untuk melanjutkan...")


# MENU UTAMA PROGRAM
while True:
    os.system('clear')  
    print("\nMAIN MENU")  
    print("1. Asimetri Kriptografi untuk Citra/Gambar")  
    print("2. Asimetri Kriptografi untuk Teks")  
    print("3. Keluar Dari Program")  
    choice1 = int(input("\nMasukkan Pilihan Menu Anda:"))  
  
    if choice1 == 1: 
        print("apakek")

      
    elif choice1 == 2:  
        choice1a = (input("\nMasukkan teks yang ingin di enkripsi: "))
        data = choice1a.encode("ascii")
        publicKeyFile = 'public.pem'
        encryptTeks(data, publicKeyFile)

        print('\n===============')
        print('Hasil Dekripsi')
        print('===============')
        decryptFile = 'data_encrypted.txt'
        privateKeyFile = 'private.pem'
        decryptTeks(decryptFile, privateKeyFile)
        print('Hasil dekripsi dari file data_encrypted.txt adalah : ' + hasilDecrypted.decode("utf-8"))

        print('\n')
        input("Pencet tombol apapun untuk melanjutkan...")
      
    elif choice1 == 3:  
        break  
      
    else:  
        print("\n Oops! Menu yang dipilih ga ada nih!")  