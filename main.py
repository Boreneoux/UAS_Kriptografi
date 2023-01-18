import pyfiglet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os

# Deklarasi variabel global untuk menampung value dari hasil dekripsi yang dilakukan nanti
hasilDecryptedGbr = ''
hasilDecrypted = ''


# Fungsi Enkripsi Teks
def encryptGambar(data, publicKeyFile):
    
    fileName = 'dummy'
    fileExtension = 'png'

    # Konversi data ke bytes
    # data = bytes(data)
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
    print('\nHasil Enkripsi tersimpan di dalam file ' + encryptedFile + '\n')
    

# Fungsi Dekripsi Teks
def decryptGambar(dataFile, privateKeyFile):

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

    global hasilDecryptedGbr
    hasilDecryptedGbr = data

    # save the decrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)

    print('\nHasil gambar yang terdecypted tersimpan dalam file: ' + decryptedFile + '\n')

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
input("Pencet tombol enter untuk melanjutkan...")


# MENU UTAMA PROGRAM
while True:
    os.system('clear')  
    print("\nMAIN MENU")  
    print("1. Asimetri Kriptografi untuk Citra/Gambar")  
    print("2. Asimetri Kriptografi untuk Teks")  
    print("3. Keluar Dari Program")  
    choice1 = int(input("\nMasukkan Pilihan Menu Anda:"))  
  
    if choice1 == 1:
        while True:
            os.system('clear')
            print("===== Menu Kriptografi untuk Citra/Gambar =====")  
            print("1. Enkripsi")  
            print("2. Dekripsi")  
            print("3. Balik ke menu utama")  
            choice2 = int(input("\nMasukkan Pilihan Menu Anda:"))
            if choice2 == 1:
                choice2a = (input("\nMasukkan nama file gambar yang ingin di enkripsi dengan ekstensinya (ex: dummy.png):"))
                publicKeyFile = 'public.pem'
                privateKeyFile = 'private.pem'
                with open(choice2a, "rb") as image:
                    f = image.read()
                encryptGambar(f, publicKeyFile)
                input("Pencet tombol enter untuk melanjutkan...")
                
            elif choice2 == 2:
                try:
                    choice2b = (input("\nMasukkan file gambar yang ingin di dekripsi dengan ekstensinya (ex: dummy_encrypted.png): "))
                    publicKeyFile = 'public.pem'
                    privateKeyFile = 'private.pem'
                    decryptFile = choice2b
                    decryptGambar(decryptFile, privateKeyFile)
                    f = open('dummy_encrypted_decrypted.png', 'wb')
                    f.write(hasilDecryptedGbr)
                    f.close()
                    with open("dummy_encrypted_decrypted.png", "wb") as img:
                        img.write(hasilDecryptedGbr)
                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                input("Pencet tombol enter untuk melanjutkan...")
            elif choice2 == 3:
                break
            else:  
                print("\n Oops! Menu yang dipilih ga ada nih!")
                input("Pencet tombol enter untuk melanjutkan...")


      
    elif choice1 == 2: 
        while True:
            os.system('clear')
            print("===== Menu Kriptografi untuk Citra/Gambar =====")  
            print("1. Enkripsi")  
            print("2. Dekripsi")  
            print("3. Balik ke menu utama")  
            choice3 = int(input("\nMasukkan Pilihan Menu Anda:")) 
            if choice3 == 1:
                choice3a = (input("\nMasukkan teks yang ingin di enkripsi: "))
                data = choice3a.encode("ascii")
                publicKeyFile = 'public.pem'
                encryptTeks(data, publicKeyFile)
                input("\nPencet tombol enter untuk melanjutkan...")
       
            elif choice3 == 2 :
                choice3b = (input("\nMasukkan file teks yang ingin di dekripsi dengan ekstensinya (ex: data_encrypted.txt): "))
                print('\n================================================================================')
                print('\t\t\t\tHasil Dekripsi')
                print('================================================================================')
                decryptFile = choice3b
                privateKeyFile = 'private.pem'
                decryptTeks(decryptFile, privateKeyFile)
                print('Hasil dekripsi dari file data_encrypted.txt adalah : ' + hasilDecrypted.decode("utf-8"))

                print('\n')
                input("Pencet tombol enter untuk melanjutkan...")
            elif choice3 == 3:
                break
            else:  
                print("\n Oops! Menu yang dipilih ga ada nih!")
                input("Pencet tombol enter untuk melanjutkan...")
        
      
    elif choice1 == 3:  
        break  
      
    else:  
        print("\n Oops! Menu yang dipilih ga ada nih!")  
        input("Pencet tombol enter untuk melanjutkan...")
