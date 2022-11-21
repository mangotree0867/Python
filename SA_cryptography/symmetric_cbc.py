from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

obj = DES.new(b'abcdefgh', DES.MODE_CBC, b'12345678')
plaintext = b'today is halloween'

message = obj.encrypt(pad(plaintext, DES.block_size))

print("encrypted message : ", message)

obj_d = DES.new(b'abcdefgh', DES.MODE_CBC, b'12345678')

print("decrypted message : ", unpad(obj_d.decrypt(message), DES.block_size))
