import socket
import hashlib

class Proxy2:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        
        print(f"Proxy 2 listening on {self.host}:{self.port}.")
        
    def receive_file(self, filename):
       
        #orig
        print("11111111111")
        self.sock.listen()
        print("2222222222")
        conn, addr = self.sock.accept()
        print(f"Connected by {addr}")
        
        # Receive file data
        file_data = b""
        while True:
            chunk = conn.recv(1024)
            print(chunk)
            print("****************")
            if not chunk:
                break
        
        
        print("end reading file")
        # Write received data to file
        with open(filename, "wb") as f:
            f.write(file_data)
            f.write(chunk)
        #print("333333333")
        # Calculate MD5 hash of received file
        md5_hash = hashlib.md5(file_data).hexdigest()
        print(f"MD5 hash of received file: {md5_hash}")
        c = hashlib.md5(chunk).hexdigest()
        print(f"MD5 hash of received file: {c}")
        # Send MD5 hash back to client
        conn.sendall(md5_hash.encode())
        conn.close()
        
if __name__ == "__main__":
    proxy2 = Proxy2("localhost", 8084)
    proxy2.receive_file("received.txt")

