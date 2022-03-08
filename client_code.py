import socket
import time
import numpy as np

HOST = "10.106.6.215"  # replace with raspbery pi IP address later
PORT = 1031
test_matrix = np.matrix('1 2; 3 4')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"1 2 3; 4 5 6; 7 8 9")
    data = s.recv(1024)
    print(f"First server response: {data!r}")
    time.sleep(2)

    '''
    s.sendall(b"0")
    data = s.recv(1024)
    time.sleep(2)
    print(f"Second server response: {data!r}")
    '''
