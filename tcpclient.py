import socket

def main():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    print(client_socket.recv(1024).decode())

    file_name = "received_file.txt"
    file_content = b""

    while True:
        data = client_socket.recv(1024)
        if b"EOF" in data:  
            data = data.replace(b"EOF", b"")  
            file_content += data
            break  

        file_content += data

    with open(file_name, "wb") as file:
        file.write(file_content)

    print("File received successfully. Check 'received_file.txt'.")
    
    # Display received file content
    print("\n Content of Received File:\n")
    print(file_content.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
