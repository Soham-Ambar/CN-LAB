# Python program to determine IP class and type

def get_ip_class(first_octet):
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'
    return 'X'

def is_private_ip(first_octet, second_octet):
    if (first_octet == 10 or 
        (first_octet == 172 and 16 <= second_octet <= 31) or 
        (first_octet == 192 and second_octet == 168)):
        return True
    return False

def main():
    ip = input("Enter an IP address: ")

    try:
        octets = list(map(int, ip.split('.')))
        if len(octets) != 4 or not all(0 <= octet <= 255 for octet in octets):
            raise ValueError
    except ValueError:
        print("Invalid IP address!")
        return

    ip_class = get_ip_class(octets[0])
    print(f"IP Class: {ip_class}")

    if is_private_ip(octets[0], octets[1]):
        print("Type: Private IP")
    else:
        print("Type: Public IP")

if __name__ == "__main__":
    main()