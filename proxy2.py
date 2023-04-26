import socket

# Define the host and port for proxy 2
PROXY2_HOST = 'localhost'
PROXY2_PORT = 8001

# Define the host and port for the network diode
DIODE_HOST = 'localhost'
DIODE_PORT = 9000

# Define the buffer size for sending/receiving data
BUFFER_SIZE = 1024

# Create a socket for proxy 2
proxy2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy2_socket.bind((PROXY2_HOST, PROXY2_PORT))
proxy2_socket.listen()

# Accept a connection from the end user
user_socket, _ = proxy2_socket.accept()

# Create a socket for the network diode
diode_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
diode_socket.connect((DIODE_HOST, DIODE_PORT))

# Receive the file from the end user
file_data = user_socket.recv(BUFFER_SIZE)
while file_data:
    diode_socket.sendall(file_data)
    file_data = user_socket.recv(BUFFER_SIZE)

# Close the socket for the network diode
diode_socket.close()

# Close the socket for the end user
user_socket.close()
