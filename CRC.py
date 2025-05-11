# Python program to implement CRC (Cyclic Redundancy Check)

def xor_operation(a, b):
    return [a[i] ^ b[i] for i in range(len(b))]

def sender_side(frame, generator):
    fs = len(frame)
    gs = len(generator)
    rs = gs - 1

    print("\nSender Side--")
    print("Frame:", ''.join(map(str, frame)))
    print("Generator:", ''.join(map(str, generator)))

    print("Number of 0's to be appended:", rs)
    frame.extend([0] * rs)

    temp = frame[:]

    for i in range(fs):
        if temp[i] == 1:
            temp[i:i+gs] = xor_operation(temp[i:i+gs], generator)

    crc = temp[fs:]
    print("CRC bits:", ''.join(map(str, crc)))

    transmitted_frame = frame[:fs] + crc
    print("Transmitted Frame:", ''.join(map(str, transmitted_frame)))

    return transmitted_frame

def receiver_side(received_frame, generator):
    fs = len(received_frame) - len(generator) + 1
    gs = len(generator)

    print("\nReceiver Side")
    print("Received Frame:", ''.join(map(str, received_frame)))

    temp = received_frame[:]

    for i in range(fs):
        if temp[i] == 1:
            temp[i:i+gs] = xor_operation(temp[i:i+gs], generator)

    remainder = temp[fs:]
    print("Remainder:", ''.join(map(str, remainder)))

    if all(bit == 0 for bit in remainder):
        print("Since Remainder is 0, the message is correct (No Errors).")
    else:
        print("Since Remainder is NOT 0, the message contains errors!")

def main():
    frame_size = int(input("Enter Frame size: "))
    print("\nEnter Frame:")
    frame = [int(input()) for _ in range(frame_size)]

    generator_size = int(input("\nEnter Generator size: "))
    print("\nEnter Generator:")
    generator = [int(input()) for _ in range(generator_size)]

    transmitted_frame = sender_side(frame, generator)

    print("\nEnter Received Frame (Manually Enter Bits):")
    received_frame = [int(input()) for _ in range(len(transmitted_frame))]
    receiver_side(received_frame, generator)

if __name__ == "__main__":
    main()