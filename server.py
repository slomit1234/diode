import socket
import hashlib

# Define the host and port for proxy 2
PROXY2_HOST = 'localhost'
PROXY2_PORT = 8001

# Define the buffer size for sending/receiving data
BUFFER_SIZE = 1024

# Define the MD5 hash function
md5 = hashlib.md5()

# Select a file to receive
file_path = '/path/to/save/file'

# Create a socket for the end user
user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect((PROXY2_HOST, PROXY2_PORT))

# Receive the file from the end user
file_data = user_socket.recv(BUFFER_SIZE)
with open(file_path, 'wb') as f:
    while file_data:
        md5.update(file_data)
        f.write(file_data)
        file_data = user_socket.recv(BUFFER_SIZE)

# Convert the MD5 hash to a string
md5_hash = md5.hexdigest()

# Close the socket for the end user
user_socket.close()

# Check the MD5 hash of the file received by the end user
with open(file_path, 'rb') as f:
    file_data = f.read()
    received_md5_hash = hashlib.md5(file_data).hexdigest()

if md5_hash == received_md5_hash:
    print('MD5 hash check passed.')
else:
    print('MD5 hash check failed.')
