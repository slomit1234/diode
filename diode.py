import socket

# Define the host and port for the network diode
DIODE_HOST = 'localhost'
DIODE_PORT = 9000

PROXY2_HOST = 'localhost'
PROXY2_PORT = 8001
# Define the buffer size for sending/receiving data
BUFFER_SIZE = 1024

# Create a socket for the network diode
diode_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
diode_socket.bind((DIODE_HOST, DIODE_PORT))
diode_socket.listen()

# Accept a connection from proxy 1
proxy1_socket, _ = diode_socket.accept()

# Create a socket for proxy 2
proxy2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy2_socket.connect((PROXY2_HOST, PROXY2_PORT))

# Forward data from proxy 1 to proxy 2
file_data = proxy1_socket.recv(BUFFER_SIZE)
while file_data:
    proxy2_socket.sendall(file_data)
    file_data = proxy1_socket.recv(BUFFER_SIZE)

# Close the sockets
proxy1_socket.close()
proxy2_socket.close()
diode_socket.close()
