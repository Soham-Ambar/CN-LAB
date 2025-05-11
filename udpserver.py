import socket
import os

# Server Configuration
UDP_IP = "0.0.0.0"  # Listen on all interfaces
UDP_PORT = 5005
BUFFER_SIZE = 4096  # Adjust based on network performance

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"UDP File Server started on {UDP_IP}:{UDP_PORT}")

try:
    while True:
        # Receive filename (but ignore it for saving purposes)
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        filename = data.decode()
        print(f"Receiving file: {filename} from {addr}")

        # Acknowledge filename reception
        server_socket.sendto(b"ACK_FILENAME", addr)

        # Open a predefined file to write (e.g., saved.txt)
        received_data = False  # Track if any data is received
        with open("saved.txt", "wb") as file:
            while True:
                # Receive data chunks
                data, addr = server_socket.recvfrom(BUFFER_SIZE)
                if data == b"EOF":  # End of file signal
                    break
                file.write(data)
                received_data = True  # Mark that data was received
                # Print the content of the received chunk
                try:
                    print(f"Received chunk: {data.decode()}")
                except UnicodeDecodeError:
                    print(f"Received chunk (binary data): {data}")
                # Acknowledge received chunk
                server_socket.sendto(b"ACK", addr)

        if not received_data:
            print(f"Error: No data received for file {filename}. File not saved.")
            os.remove("saved.txt")  # Delete the empty file
        else:
            print(f"File saved as saved.txt successfully.\n")

except KeyboardInterrupt:
    print("\nServer stopped by user.")
finally:
    server_socket.close()
    print("Socket closed. Exiting...")
