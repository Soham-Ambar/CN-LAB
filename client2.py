import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connect to the server on localhost and port 12345
    # Send a message to the server
    client_socket.sendall("Hello from Client!".encode('utf-8'))
    # Receive and print the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    client_socket.close()  # Close the connection

if __name__ == "__main__":
    start_client()