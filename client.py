# import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1239


# Function to listen to messages from server and show it to the client
def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('UTF-8')
        if message != '':
            username = message.split('~')[0]
            content = message.split('~')[1]
            print("[{}] {}".format(username, content))
        else:
            print("Message received can not be empty!!")


# Function that allows user to send a message to server
def send_message_to_server(client):
    while 1:
        message = input("Message: ")
        if message != '':
            client.sendall(message.encode())
        else:
            print("Message can not be empty!!")


# Function to take the username from the client and send it to the server
def communicate_to_server(client):
    username = input("Enter Username :")
    if username != '':
        client.sendall(username.encode())
    else:
        print("User name can not be empty!!")
        exit(0)
    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
    send_message_to_server(client)


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
    communicate_to_server(client)


if __name__ == '__main__':
    main()
