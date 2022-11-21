from os import urandom

def genKey(size_of_key):
    print(size_of_key)
    key = urandom(size_of_key)
    print(key)
    bytearray_key = bytearray(key)
    print(bytearray_key)
    return bytearray_key


def encrypt(plain, key):
    original = [ ord(plain[i]) for i in range(len(plain))]
    print(original)
    result = [ key[i] ^ ord(plain[i]) for i in range(len(plain))]
    return result

def decrypt(cipher, key):
    result = [ key[i] ^ cipher[i] for i in range(len(cipher))]
    print(result)
    string_result = [chr( i ) for i in result]
    print(string_result)
    return result

###################################################

myMessage = "This is a secret message"

print(myMessage)

block = "12345678"

myKey = genKey(len(myMessage))

cipherText = encrypt(myMessage, myKey)
print(cipherText)

plain_text = decrypt(cipherText, myKey)
