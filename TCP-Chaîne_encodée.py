import socket
import base64
import codecs
import re

HOST = "challenge01.root-me.org"
PORT = 52023

def is_printable(s):
    return all(32 <= ord(c) <= 126 for c in s)

s = socket.socket()
s.connect((HOST, PORT))

data = s.recv(2048).decode()
print(data)

encoded = re.search(r"'(.+?)'", data).group(1)

candidates = []

#  Base64 only
try:
    c = base64.b64decode(encoded).decode()
    candidates.append(c)
except:
    pass

# Base64 → ROT13
try:
    c = codecs.decode(base64.b64decode(encoded).decode(), 'rot_13')
    candidates.append(c)
except:
    pass

# ROT13 → Base64
try:
    c = base64.b64decode(codecs.decode(encoded, 'rot_13')).decode()
    candidates.append(c)
except:
    pass

# choose printable answer
for c in candidates:
    if is_printable(c):
        answer = c
        break

print("Final answer:", answer)

s.sendall(f"{answer}\n".encode())
print(s.recv(1024).decode())

s.close()
