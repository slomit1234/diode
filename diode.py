import socket

class Diode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        
        print(f"Diode listening on {self.host}:{self.port}...")
        
    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            print(f"Data received from {addr}: {data}")
            
            # Forward data to proxy 2
            proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_sock.connect(("localhost", 8084))
            proxy_sock.sendall(data)
            print("Data forwarded to proxy 2.")
            
if __name__ == "__main__":
    diode = Diode("localhost", 8081)
    diode.run()

