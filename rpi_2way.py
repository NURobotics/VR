# import socket programming library
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
import socket

# import thread module
from _thread import *
import threading
import time

print_lock = threading.Lock()

# thread function
def threaded():
    #sendNum = 0
    #while True:
    HOST = "10.105.155.53"  # replace with raspbery pi IP address later
    PORT = 1037
    #test_matrix = np.matrix('1 2; 3 4')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #data = s.recv(1024)
        #print(f"First server response: {data!r}")
        while True:
            sendNum = input()
            s.send(sendNum.encode())
            print("Sent string", sendNum)
            #sendNum += 2
            #time.sleep(2)


def Main():
    print("in main")
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12377
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        conn, addr = s.accept()

        while True:
            # lock acquired by client
            #print_lock.acquire()
            data = conn.recv(1024)
            if not data: break
            string_data = str(data.decode())
            print("from connected user: \n" + string_data)


        #print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier

    s.close()


if __name__ == '__main__':
    start_new_thread(threaded, ())
    Main()
