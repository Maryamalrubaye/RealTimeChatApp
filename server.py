# importing required modules
import socket  # socket will be used for the main communication part
import threading

HOST = '127.0.0.1'
PORT = 12344  # You can use any port between 0 to 65535
LISTENER_LIMIT = 5
active_client = []  # list of all currently connected users


# Function that listen to the upcoming messages from the client
def listen_for_messages(client, username):
    while 1:
        message = client.recv(2048).decode('UTF-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print("Client {} message is empty!".format(username))


# Function to send message to single client
def send_message_to_client(client, message):
    client.sendall(message.encode())


# Function to send ant new message ro all clients that
# are currently connected to the server
def send_messages_to_all(message):
    for user in active_client:
        send_message_to_client(user[1], message)


# function handle client
def client_handler(client):
    # Server will listen for client message that will
    #   Contain the username
    while 1:
        username = client.recv(2048).decode('UTF-8')
        if username != '':
            active_client.append((username, client))
            break
        else:
            print("Client username is empty!")
    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


# main function
def main():
    # CREATING THE SOCKET CLASS OBJECT
    # AF_INET : we are going to use IPv4 address
    # SOCK_STREAM : we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try and catch block
    try:
        # provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print('Running the server on {} {}'.format(HOST, PORT))
    except:
        print("Unable to bind to host {} and port {}".format(HOST, PORT))
    # set server limit
    server.listen(LISTENER_LIMIT)
    # this while loop will keep listening to the client connection
    while 1:
        client, address = server.accept()
        print("Successfully connected to client {} {} ".format(address[0], address[1]))

        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == '__main__':
    main()
