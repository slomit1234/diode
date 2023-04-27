import socket

class EndUser:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        
        print(f"End user listening on {self.host}:{self.port}...")
        
    def receive_file(self, filename):
        conn, addr = self.sock.accept()
        print(f"Connected by {addr}")
        
        # Receive file data
        file_data = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            file_data += chunk
        
        # Write received data to file
        with open(filename, "wb") as f:
            f.write(file_data)
            
        conn.close()
        print(f"File received and saved as {filename}.")

if __name__ == "__main__":
    end_user = EndUser("localhost", 8083)
    end_user.receive_file("received.txt")

