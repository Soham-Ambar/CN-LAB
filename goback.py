import random
import time

def transmission(i, N, tf):
    tt = 0  # Initialize total transmissions counter
    while i <= tf:
        z = 0
        # Sending frames in the current window
        for k in range(i, i + N):
            if k > tf:
                break
            print(f"Sending Frame {k}...")
            tt += 1

        # Checking acknowledgments for the frames in the current window
        for k in range(i, i + N):
            if k > tf:
                break
            f = random.randint(0, 1)  # Randomly decide if the frame is acknowledged or not
            if f == 0:
                print(f"Acknowledgment for Frame {k}...")
                z += 1
            else:
                print(f"Timeout!! Frame Number : {k} Not Received")
                print("Retransmitting Window...")
                break

        print("\n")
        i += z

    return tt


def main():
    random.seed(time.time())
    tf = int(input("Enter the Total number of frames: "))
    N = int(input("Enter the Window Size: "))
    i = 1

    total_transmissions = transmission(i, N, tf)

    print(f"Total number of frames which were sent and resent are: {total_transmissions}")


if __name__ == "__main__":
    main()
