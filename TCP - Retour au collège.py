import socket
import math
import re

HOST = "challenge01.root-me.org"
PORT = 52002

# create socket and connect
s = socket.socket()
s.connect((HOST, PORT))

# read challenge
data = s.recv(1024).decode()
print(data)

# extract numbers using regex
match = re.search(r'square root of (\d+) and multiply by (\d+)', data)
if match:
    n1 = int(match.group(1))
    n2 = int(match.group(2))

    # compute result immediately
    ans = round(math.sqrt(n1) * n2, 2)

    # send answer quickly
    s.sendall(f"{ans}\n".encode())
    print("Sent:", ans)

    # read response (flag)
    response = s.recv(1024).decode()
    print(response)

s.close()