from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

d = open("plain_g.txt","rb")
data = d.read()
d.close

secret_key = get_random_bytes(16)

save_key = open("AES_key_g.txt", "wb")
save_key.write(secret_key)
save_key.close()

file_key = open("AES_key_g.txt", "rb")
secret_key = file_key.read()
file_key.close()


pad = len(data) % len(secret_key)
if (pad != 0):
    padding = len(secret_key) - pad
    data = data.ljust(len(data)+padding, b'0')

print(len(secret_key))
print(len(data))


cipher_AES = AES.new(secret_key, AES.MODE_CBC)
cipher_text = cipher_AES.encrypt(data)


file_out = open("AES_encrypted.bin", "wb")
file_out.write(cipher_AES.iv)
file_out.write(cipher_text)
file_out.close()
