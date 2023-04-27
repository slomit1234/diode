import socket
import hashlib

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        
        print(f"Server listening on {self.host}:{self.port}...")

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"Client connected: {addr}")

            # Receive file from client
            file_data = conn.recv(2048).decode('utf-8')
            print(file_data)
            
            print("File received from client.")
            
            # Calculate MD5 hash of file
            md5_hash = hashlib.md5(allf).hexdigest()
            print(f"MD5 hash of file: {md5_hash}")
            
            # Forward file to proxy 2 through the diode
            diode_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            diode_sock.sendto(allf, ("localhost", 8081))
            print("File forwarded to proxy 2 through the diode.")
            
            #conn.sendall(md5_hash.encode())
            #print(f"MD5 hash sent to client: {md5_hash}")
            
if __name__ == "__main__":
    server = Server("localhost", 8080)
    server.run()

