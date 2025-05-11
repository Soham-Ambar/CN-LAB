# Python program to implement Hamming Code (7,4) and (15,11)

def main():
    data = [0] * 16
    dataatrec = [0] * 16

    print("Choose parity option:")
    print("1. Hamming(7,4) - 3 parity bits")
    print("2. Hamming(15,11) - 4 parity bits")
    choice = int(input())

    if choice == 1:
        print("Enter 4 bits of data one by one:")
        data[7] = int(input())
        data[6] = int(input())
        data[5] = int(input())
        data[3] = int(input())

        # Calculating 3 Parity Bits (Even Parity)
        data[1] = data[3] ^ data[5] ^ data[7]
        data[2] = data[3] ^ data[6] ^ data[7]
        data[4] = data[5] ^ data[6] ^ data[7]

        print("\nEncoded data is:")
        for i in range(1, 8):
            print(data[i], end=" ")

        print("\n\nEnter received 7-bit data one by one:")
        for i in range(1, 8):
            dataatrec[i] = int(input())

        # Checking for errors
        c1 = dataatrec[1] ^ dataatrec[3] ^ dataatrec[5] ^ dataatrec[7]
        c2 = dataatrec[2] ^ dataatrec[3] ^ dataatrec[6] ^ dataatrec[7]
        c3 = dataatrec[4] ^ dataatrec[5] ^ dataatrec[6] ^ dataatrec[7]

        c = c3 * 4 + c2 * 2 + c1

    else:
        print("Enter 11 bits of data one by one:")
        data[15] = int(input())
        data[14] = int(input())
        data[13] = int(input())
        data[12] = int(input())
        data[11] = int(input())
        data[10] = int(input())
        data[9] = int(input())
        data[7] = int(input())
        data[6] = int(input())
        data[5] = int(input())
        data[3] = int(input())

        # Calculating 4 Parity Bits (Even Parity)
        data[1] = data[3] ^ data[5] ^ data[7] ^ data[9] ^ data[11] ^ data[13] ^ data[15]
        data[2] = data[3] ^ data[6] ^ data[7] ^ data[10] ^ data[11] ^ data[14] ^ data[15]
        data[4] = data[5] ^ data[6] ^ data[7] ^ data[12] ^ data[13] ^ data[14] ^ data[15]
        data[8] = data[9] ^ data[10] ^ data[11] ^ data[12] ^ data[13] ^ data[14] ^ data[15]

        print("\nEncoded data is:")
        for i in range(1, 16):
            print(data[i], end=" ")

        print("\n\nEnter received 15-bit data one by one:")
        for i in range(1, 16):
            dataatrec[i] = int(input())

        # Checking for errors
        c1 = dataatrec[1] ^ dataatrec[3] ^ dataatrec[5] ^ dataatrec[7] ^ dataatrec[9] ^ dataatrec[11] ^ dataatrec[13] ^ dataatrec[15]
        c2 = dataatrec[2] ^ dataatrec[3] ^ dataatrec[6] ^ dataatrec[7] ^ dataatrec[10] ^ dataatrec[11] ^ dataatrec[14] ^ dataatrec[15]
        c3 = dataatrec[4] ^ dataatrec[5] ^ dataatrec[6] ^ dataatrec[7] ^ dataatrec[12] ^ dataatrec[13] ^ dataatrec[14] ^ dataatrec[15]
        c4 = dataatrec[8] ^ dataatrec[9] ^ dataatrec[10] ^ dataatrec[11] ^ dataatrec[12] ^ dataatrec[13] ^ dataatrec[14] ^ dataatrec[15]

        c = c4 * 8 + c3 * 4 + c2 * 2 + c1

    if c == 0:
        print("\nCongratulations! No error detected.")
    else:
        print(f"\nError detected at position: {c}")
        print("Corrected message is:")

        # Correcting the error
        dataatrec[c] = 1 if dataatrec[c] == 0 else 0

        for i in range(1, (7 if choice == 1 else 15) + 1):
            print(dataatrec[i], end=" ")

if __name__ == "__main__":
    main()
