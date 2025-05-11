import random
import time

def sender(window_size, total_frames):
    frames = [{'data': f"Frame {i+1}", 'ack': False} for i in range(total_frames)]
    return frames

def selective_repeat(frames, window_size):
    total_frames = len(frames)
    base = 0
    while base < total_frames:
        print(f"\nSending frames in window: {base+1} to {min(base+window_size, total_frames)}")
        for i in range(base, min(base + window_size, total_frames)):
            if not frames[i]['ack']:
                print(f"Sending {frames[i]['data']}...")

        for i in range(base, min(base + window_size, total_frames)):
            if not frames[i]['ack']:
                ack = random.choice([True, False])  # Simulate acknowledgment
                if ack:
                    print(f"Acknowledgment received for {frames[i]['data']}")
                    frames[i]['ack'] = True
                else:
                    print(f"Timeout for {frames[i]['data']}. Resending...")

        while base < total_frames and frames[base]['ack']:
            base += 1

def main():
    total_frames = int(input("Enter the total number of frames: "))
    window_size = int(input("Enter the window size: "))

    frames = sender(window_size, total_frames)
    selective_repeat(frames, window_size)

    print("\nAll frames sent successfully.")

if __name__ == "__main__":
    main()
