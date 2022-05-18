# import socket programming library
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
import socket

# import thread module
from _thread import *
import threading
import time

print_lock = threading.Lock()

# thread function
def recv_thread(s):
    data = s.recv(1024).decode()
    print(f"First server response: {data!r}")

def Main():
    sendNum = 0
    HOST = "localhost"  # replace with computer IP address later
    PORT = 1277

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            start_new_thread(recv_thread, (s,))
            s.send(str(sendNum).encode())
            sendNum += 21
            time.sleep(1)

def sending_thread(conn):
    t2 = time.time()
    conn.send(str(t2).encode())


if __name__ == '__main__':
	Main()
	
