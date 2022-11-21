
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15

rng = Random.new().read

RSAkey = RSA.generate(1024, rng)

#1. have a plaintext and hash it
plaintext = b'the seed ubuntu vm is working'
hash = MD5.new(plaintext)

#2. use rsa public key to sign it
signature = pkcs1_15.new(RSAkey).sign(hash)

print(signature)

#3. verify signature using rsa private key
try:
	verification = pkcs1_15.new( RSAkey ).verify(hash, signature)
	print("true")
except:
	print("false")

