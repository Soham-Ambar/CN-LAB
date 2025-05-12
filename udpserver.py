import socket

MAX_SIZE = 1000000
PORT = 8000

def save_file(file_name, data):
    with open(file_name, 'wb') as f:
        f.write(data)
    print(f"File '{file_name}' received and saved successfully.")

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', PORT))
    print("UDP Server is running and listening on port", PORT)

    while True:
        choice, addr = sock.recvfrom(1)
        choice = int.from_bytes(choice, byteorder='big')

        if choice == 1:
            # Text file
            fname, _ = sock.recvfrom(1024)
            fname = fname.decode()
            print("TEXT FILE NAME RECEIVED:", fname)

            data, _ = sock.recvfrom(4096)
            print("TEXT CONTENT RECEIVED:\n", data.decode())

            save_file(fname, data)

        elif choice == 2:
            # Audio file
            fname, _ = sock.recvfrom(1024)
            fname = fname.decode()
            print("AUDIO FILE NAME RECEIVED:", fname)

            data, _ = sock.recvfrom(MAX_SIZE)
            save_file(fname, data)

        elif choice == 3:
            # Video file
            fname, _ = sock.recvfrom(1024)
            fname = fname.decode()
            print("VIDEO FILE NAME RECEIVED:", fname)

            data, _ = sock.recvfrom(MAX_SIZE)
            save_file(fname, data)

        elif choice == 4:
            print("Exiting server...")
            break

    sock.close()

if __name__ == "__main__":
    start_server()
