import socket
import hashlib

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        
        print(f"Connected to server {self.host}:{self.port}.")
        
    def send_file(self, filename):
        # Read file contents
        with open(filename, "rb") as f:
            file_data = f.read()
        print("****************")
        # Send file to proxy 1
        self.sock.sendall("{file_dataf}".encode('utf-8'))
        print("File sent to server.")
        
        md5_hash = hashlib.md5(file_data).hexdigest()
        print(f"MD5 hash of file: {md5_hash}")
        # Receive MD5 hash from server
        #md5_hash = self.sock.recv(1024).decode()
        #print(f"MD5 hash of file received from server: {md5_hash}")
        
if __name__ == "__main__":
    client = Client("localhost", 8080)
    client.send_file("test.txt")

