# import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234


# main function
def main():
    # Creating a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # CONNECT TO THE SERVER
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to server")
    except:
        print("Unable to connect to server {} {}".format(HOST, PORT))



if __name__ == '__main__':
    main()
