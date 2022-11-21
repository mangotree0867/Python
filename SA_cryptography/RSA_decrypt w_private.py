
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#from Crypto.Cipher import AES


file_in = open("encrypted_with_GangRok_public.bin", "rb")

enc_data = file_in.read()
file_in.close()

f = open("g_private.pem")
key_in = f.read()
f.close()
private_key = RSA.import_key(key_in)

cipher_RSA = PKCS1_OAEP.new(private_key)

plain_data = cipher_RSA.decrypt( enc_data  )

f = open("decrypted_rsa.txt", "wb")
f.write(plain_data)
f.close()

print(   plain_data   )
