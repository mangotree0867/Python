import pyotp

secret = pyotp.random_base32()
secret2 = pyotp.random_base32()

otpad = []
file_in = open("test.txt", "r")
o = file_in.readlines()
for line in o:
    otpad.append(line)
otpad = [item.strip() for item in otpad]
file_in.close()

otpad.append(secret)

otpad.append(secret2)

i = open("test.txt" , "w")
for meh in otpad:
    i.writelines("%s\n" % meh)
i.close()

print(str(secret))

print("<<<<<<<<<")

print(secret2)
