from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

f = open('g_public.pem', 'rb')
public_key = RSA.import_key(   f.read()    )
f.close()

get_text = open('plain_g.txt','rb')
message = get_text.read()
get_text.close()

get_sign = open('signed_with_GangRok_private.txt', 'rb')
signature = get_sign.read()
get_sign.close()

h = SHA256.new(message)

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("true")
except:
    print("false")
