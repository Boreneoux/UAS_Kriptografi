from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

# Menyimpan private key ke file
with open('private.pem', 'wb') as f:
    f.write(privateKey)

# Menyimpan public key ke file
with open('public.pem', 'wb') as f:
    f.write(publicKey)

print('Private key disimpan ke private.pem')
print('Public key disimpan ke public.pem')
print('Selesai')