
from Crypto.Cipher import DES

obj = DES.new(b'abcdefgh', DES.MODE_ECB)
d = open("plain_g.txt", "rb")
plaintext = d.read()
d.close()

print(len(plaintext))

message = obj.encrypt(plaintext + b'0000')

print("encrypted message : ", message)

print("decrypted message : ", obj.decrypt(message)[:-4])
