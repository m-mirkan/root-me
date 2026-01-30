import socket
import base64
import zlib
import re

HOST = "challenge01.root-me.org"
PORT = 52022

s = socket.socket()
s.connect((HOST, PORT))

while True:
    data = s.recv(4096).decode()
    if not data:
        break

    print(data)

    # stop condition (flag / success)
    if "Congratulations" in data or "flag" in data.lower():
        break

    # extract base64 string
    match = re.search(r"'(.+?)'", data)
    if not match:
        continue

    encoded = match.group(1)

    # decode base64
    compressed = base64.b64decode(encoded)

    # decompress zlib
    decoded = zlib.decompress(compressed).decode()

    print("Decoded:", decoded)

    # send answer immediately
    s.sendall(f"{decoded}\n".encode())

s.close()
