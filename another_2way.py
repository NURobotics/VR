# import socket programming library
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
import socket

# import thread module
from _thread import *
import threading
import time

print_lock = threading.Lock()

# thread function
def recv_thread(conn):
    try:
        data = conn.recv(1024)
        if not data: return
        string_data = str(data.decode())
        print("from connected user: " + string_data)
    except:
        return

def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 1277
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    numsend = 0
    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        conn, addr = s.accept()

        while True:
            start_new_thread(recv_thread, (conn,))
            #print("threads:", threading.active_count())
            sending_thread(conn, numsend)
            numsend += 5

    s.close()

def sending_thread(conn, numsend):
    t2 = "hulu " + str(numsend)
    #t2 = input()
    conn.send(str(t2).encode())
    time.sleep(1)


if __name__ == '__main__':
	Main()
	
