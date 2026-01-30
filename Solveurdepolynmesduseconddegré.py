import socket
import re
import math

HOST = "challenge01.root-me.org"
PORT = 52018

def round_root(x):
    r = round(x + 1e-9, 3)
    if r == -0.0:
        r = 0.0
    return r

s = socket.socket()
s.connect((HOST, PORT))

for i in range(25):
    data = s.recv(4096).decode()
    print(data)

    eq_match = re.search(r'please:\s*(.*)', data)
    if not eq_match:
        continue

    eq = eq_match.group(1).strip()

    # Robust regex parsing
    match = re.search(r'([+-]?\d+)\.x²\s*([+-]\s*\d+)\.x¹\s*([+-]\s*\d+)\s*=\s*([+-]?\d+)', eq)
    if not match:
        continue

    a = float(match.group(1))
    b = float(match.group(2).replace(" ", ""))
    c = float(match.group(3).replace(" ", ""))
    rhs = float(match.group(4))

    # Standard form
    c = c - rhs

    # Discriminant
    delta = b*b - 4*a*c

    if delta < 0:
        answer = "Not possible"
    elif delta == 0:
        x = round_root(-b / (2*a))
        answer = f"x: {x:.3f}"
    else:
        sqrt_d = math.sqrt(delta)
        x1 = round_root((-b - sqrt_d) / (2*a))
        x2 = round_root((-b + sqrt_d) / (2*a))
        x1, x2 = sorted([x1, x2])
        answer = f"x1: {x1:.3f} ; x2: {x2:.3f}"

    print("Answer:", answer)
    s.sendall((answer + "\n").encode())

# Receive final flag
final = s.recv(4096).decode()
print(final)
s.close()
