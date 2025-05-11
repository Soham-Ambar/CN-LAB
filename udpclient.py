import socket
import os

# Server Configuration
SERVER_IP = "192.168.188.179"  # Change this to the receiver’s IP
SERVER_PORT = 5005
BUFFER_SIZE = 4096  # Match with the server

# Files to send (update paths as needed)
FILES_TO_SEND = {
    "soham.txt": "soham.txt"
}

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for label, file_path in FILES_TO_SEND.items():
    if not os.path.exists(file_path):
        print(f"File {file_path} not found, skipping.")
        continue

    print(f"Sending file: {file_path}")

    # Send filename
    client_socket.sendto(file_path.encode(), (SERVER_IP, SERVER_PORT))

    # Wait for acknowledgment
    ack, _ = client_socket.recvfrom(BUFFER_SIZE)
    if ack != b"ACK_FILENAME":
        print("Error: No ACK from server")
        continue

    # Open file and send data
    with open(file_path, "rb") as file:
        while (chunk := file.read(BUFFER_SIZE)):
            client_socket.sendto(chunk, (SERVER_IP, SERVER_PORT))
            # Debugging: Print the chunk being sent
            print(f"Sent chunk: {chunk.decode(errors='ignore')}")
            ack, _ = client_socket.recvfrom(BUFFER_SIZE)  # Wait for chunk ACK
            if ack != b"ACK":
                print("Error: No ACK for chunk")
                break

    # Send end-of-file signal
    client_socket.sendto(b"EOF", (SERVER_IP, SERVER_PORT))
    print(f"File {file_path} sent successfully.\n")

client_socket.close()
