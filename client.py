import socket
import hashlib

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 8081))
        filename = '//home/magshimim/Downloads/diode/test.txt'
        
        print(f"Connected to server {self.host}:{self.port}.")
        
    def send_file(self, filename):
        # Read file contents
        with open(filename, "rb") as f:
            file_data = f.read()
        
        # Send file to proxy 1
        self.sock.sendall(file_data)
        print("File sent to server.")
        
        # Receive MD5 hash from server
        md5_hash = self.sock.recv(1024).decode()
        print(f"MD5 hash of file received from server: {md5_hash}")
        
if __name__ == "__main__":
    client = Client("localhost", 8080)
    client.send_file("test.txt")
