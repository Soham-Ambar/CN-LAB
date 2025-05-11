import socket

def main():
    HOST = "127.0.0.1"
    PORT = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server started. Waiting for clients...")

    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    client_socket.sendall(b"Server: Hello!\n")

    file_name = "read.txt"
    try:
        with open(file_name, "rb") as file:
            data = file.read()
            client_socket.sendall(data)  
        client_socket.sendall(b"EOF")  
        print("File sent successfully.")

        # Show file content on server
        print("File Content Sent to Client:\n")
        print(data.decode())

    except FileNotFoundError:
        print("Error: File not found.")
        client_socket.sendall(b"ERROR: File not found.")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
