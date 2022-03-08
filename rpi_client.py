import socket
import sys
import RPi.GPIO as GPIO
import time
import numpy as np

LED_PIN = 17

#connection for listening
def make_connection(port):
    host = "" #blank means listens for all IP addresses
    # create a socket, sockstream == tcp, protocol set to 0
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind to specific IP and port number
    s.bind((host, port))
    #listens for connection request
    s.listen(5) #default backlog

    while True:
        GPIO.cleanup()
        print("listening on port" ,port,"...")
        #when request intercepted, accept and identify client socket with its address
        conn, addr = s.accept()
        print("Connection from: " + str(addr))
        #with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            string_data = str(data.decode())
            print("from connected user: \n" + string_data)
            print(f"r: {parse_matrix(string_data)}")

            #if  string_data.isdigit():
            #    print("light up")
                #light_up(int(string_data))
            #else:
            #    print("not valid")

def parse_matrix(input):
    #given 1 2; 5 3
    output = input.split("; ")
    
    new_list = []
    
    for u in output:
        again = u.split(" ")
        for a in again:
            b = int(a)
            new_list.append(b)
    
    print(new_list)
    r = np.array(new_list)
    r = np.reshape(r, (3, 3))
    return r

def setup_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)


def light_up(input):
    #GPIO.output(LED_PIN, GPIO.HIGH if input else GPIO.LOW)
    if input == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif input == 0:
        GPIO.output(LED_PIN, GPIO.LOW)
    elif input == 2:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    #input variable
    try:
        port_input = int(sys.argv[1])
    except:
        #sys.stderr.write("You need to enter a valid input \nEx. 'python filename.py port_num'")
        #sys.exit(3)
        port_input = 1031
    
    #if port_input < 1024:
     #   sys.stderr.write("Only ports >= 1024")
     #   sys.exit(3)

    #set up GPIO
    #setup_led()
    data = make_connection(port_input)