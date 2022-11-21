from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

f = open('g_private.pem','rb')
my_key = f.read()
key = RSA.import_key(my_key)
f.close()

get_text = open('plain_g.txt', 'rb')
message = get_text.read()
get_text.close()

hash = SHA256.new(message)

signature = pkcs1_15.new(key).sign(  hash   )

new_signature = open('signed_with_GangRok_private.txt', 'wb')
new_signature.write(signature)
new_signature.close()
