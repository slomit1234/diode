import socket
import hashlib

# Define the host and port for proxy 1
PROXY1_HOST = 'localhost'
PROXY1_PORT = 8000

# Define the buffer size for sending/receiving data
BUFFER_SIZE = 1024

# Define the MD5 hash function
md5 = hashlib.md5()

# Select a file to send
file_path = '//home/magshimim/Downloads/diode2/test.txt'
with open(file_path, 'rb') as f:
    file_data = f.read()
    md5.update(file_data)

# Convert the MD5 hash to a string
md5_hash = md5.hexdigest()

# Create a socket for proxy 1
proxy1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy1_socket.connect((PROXY1_HOST, PROXY1_PORT))

# Send the file to proxy 1
proxy1_socket.sendall(file_data)

# Close the socket for proxy 1
proxy1_socket.close()

# Print the MD5 hash of the file
print(f'MD5 hash: {md5_hash}')
