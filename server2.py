import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Bind to localhost and port 12345
    server_socket.listen(1)  # Listen for incoming connections
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connection established with {addr}")

    # Receive and print the message from the client
    message = conn.recv(1024).decode('utf-8')
    print(f"Received from client: {message}")

    # Send a response back to the client
    conn.sendall("Hello from Server!".encode('utf-8'))

    conn.close()  # Close the connection
    server_socket.close()

if __name__ == "__main__":
    start_server()