import socket

# Define the host and port for the network diode
DIODE_HOST = 'localhost'
DIODE_PORT = 9000


# Define the host and port for proxy 1
PROXY1_HOST = 'localhost'
PROXY1_PORT = 8000

# Define the buffer size for sending/receiving data
BUFFER_SIZE = 1024

# Create a socket for proxy 1
proxy1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy1_socket.bind((PROXY1_HOST, PROXY1_PORT))
proxy1_socket.listen()

# Accept a connection from the source user
source_socket, _ = proxy1_socket.accept()

# Create a socket for the network diode
diode_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
diode_socket.connect((DIODE_HOST, DIODE_PORT))

# Send the file to the network diode
file_data = source_socket.recv(BUFFER_SIZE)
while file_data:
    diode_socket.sendall(file_data)
    file_data = source_socket.recv(BUFFER_SIZE)

# Close the sockets
source_socket.close()
proxy1_socket.close()
diode_socket.close()
