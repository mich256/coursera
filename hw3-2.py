from hashlib import sha256

f = open("6.2.birthday.mp4_download","rb")
d = f.read()
f.close()
l = [d[i:min(len(d),i+1024)] for i in range(0,len(d),1024)]

b = b''

while l:
    a = l.pop() + b
    b = sha256(a).digest()

print(b.hex())
