from Crypto.Hash import SHA256

f = open("6.1.intro.mp4_download","rb")
d = f.read()
f.close()
l = [d[i:min(len(d),i+1024)] for i in range(0,len(d),1024)]

b = b''
ho = SHA256.new()

while l:
    a = l.pop() + b
    b = SHA256.new(a).digest()

print(b.hex())
