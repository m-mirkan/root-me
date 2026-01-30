import socket
import codecs
import re

HOST = "challenge01.root-me.org"
PORT = 52021

s = socket.socket()
s.connect((HOST, PORT))

data = s.recv(2048).decode()
print(data)

# extract encoded string between quotes
encoded = re.search(r"'(.+?)'", data).group(1)

# ROT13 decode
decoded = codecs.decode(encoded, 'rot_13')
print("Decoded:", decoded)

# send answer immediately
s.sendall(f"{decoded}\n".encode())

# receive result (flag / success)
print(s.recv(1024).decode())

s.close()
