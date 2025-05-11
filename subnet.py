import math

def print_ip(ip):
    print(".".join(map(str, ip)))

def get_ip_class(first_octet):
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    return 'X'

def get_default_subnet_mask(ip_class):
    if ip_class == 'A':
        return [255, 0, 0, 0]
    elif ip_class == 'B':
        return [255, 255, 0, 0]
    elif ip_class == 'C':
        return [255, 255, 255, 0]
    return [0, 0, 0, 0]

def and_operation(ip, subnet_mask):
    return [ip[i] & subnet_mask[i] for i in range(4)]

def generate_subnets(network_address, subnet_bits, num_subnets):
    subnet_increment = int(math.pow(2, (8 - subnet_bits)))

    print("\nSubnet Ranges:")
    for i in range(num_subnets):
        start_ip = network_address[:]
        end_ip = network_address[:]

        start_ip[3] = i * subnet_increment
        end_ip[3] = start_ip[3] + subnet_increment - 1

        print(f"Subnet {i + 1}: ", end="")
        print_ip(start_ip)
        print(" to ", end="")
        print_ip(end_ip)
        print()

def main():
    ip_address = input("Enter IP address: ")
    ip = list(map(int, ip_address.split('.')))

    ip_class = get_ip_class(ip[0])
    if ip_class == 'X':
        print("Invalid or unsupported IP class!")
        return

    subnet_mask = get_default_subnet_mask(ip_class)

    print(f"IP Class: {ip_class}")
    print("Default Subnet Mask: ", end="")
    print_ip(subnet_mask)

    network_address = and_operation(ip, subnet_mask)
    print("Network Address (IP AND Default Subnet Mask): ", end="")
    print_ip(network_address)

    num_subnets = int(input("Enter the number of subnets to create: "))
    subnet_bits = math.ceil(math.log2(num_subnets))
    generate_subnets(network_address, subnet_bits, num_subnets)

if __name__ == "__main__":
    main()
