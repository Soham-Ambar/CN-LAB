import socket

SERVER_IP = '127.0.0.1'
PORT = 8000

def send_file(sock, filepath, addr):
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        sock.sendto(filepath.encode(), addr)
        sock.sendto(content, addr)
        print("FILE SENT:", filepath)
    except FileNotFoundError:
        print("File not found:", filepath)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (SERVER_IP, PORT)

    while True:
        print("\nEnter \n1.TEXT \n2.AUDIO \n3.VIDEO \n4.EXIT")
        choice = int(input("Choice: "))
        sock.sendto(choice.to_bytes(1, byteorder='big'), addr)

        if choice in [1, 2, 3]:
            filepath = input("Enter file name to send: ")
            send_file(sock, filepath, addr)
        elif choice == 4:
            print("Exiting client...")
            break
        else:
            print("Invalid choice")

    sock.close()

if __name__ == "__main__":
    client()
