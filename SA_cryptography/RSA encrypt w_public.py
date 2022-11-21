
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

get_text = open("plain_g.txt", "rb")
message = get_text.read()

#data2= "this is another text example".encode("utf-8")

file_out = open("encrypted_with_GangRok_public.bin", "wb")

f = open("g_public.pem")
key_in = f.read()
public_key = RSA.import_key(key_in)


cipher_RSA = PKCS1_OAEP.new(public_key)

enc_data = cipher_RSA.encrypt( message )

file_out.write(  enc_data    ) 
file_out.close()
