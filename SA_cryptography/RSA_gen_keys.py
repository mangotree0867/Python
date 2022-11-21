from Crypto.PublicKey import RSA
from Crypto import Random

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

print(private_key)
print(public_key)

file_out = open("g_private.pem", "wb")
file_out.write(private_key)
file_out.close()

file_out = open("g_public.pem", "wb")
file_out.write(public_key)
file_out.close()
