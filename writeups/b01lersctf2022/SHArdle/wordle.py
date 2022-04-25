from pwn import *
from itertools import product
import sys
import re
import random
 
colors = {
    b'[40m': 'white',
    b'[42m': 'green',
    b'[43m': 'yellow',
}
e = re.compile(b'\x1b(\[[\d]+m)([\d\w]+)')
clear = '\033[39m'
red = '\033[31m'
green = '\033[32m'

hashes = {}
debug = False


def read_hashes():
    with open('hashes-d') as f:
        for line in f:
            try:
                p, h = line.split(' ')
                hashes[p] = h.strip().encode()
            except:
                print(line)


read_hashes()

c = remote('ctf.b01lers.com', 9102)
print(c.recvuntil(b'choose: '))
c.send(b'1\n')
print(c.recvuntil(b'guess: '))


def check(i, byte):
    count = 0
    for k in list(hashes.keys()):
        h = hashes[k].decode()
        if chr(hashes[k][i]) != byte.decode():
            if debug:
                print(h[0:i-1]+red+h[i]+clear+h[i:])
                print(chr(hashes[k][i]), byte.decode())
            hashes.pop(k)
            count += 1
            if debug:
                input("next hash? ")
        elif debug:
           print(h[0:i-1]+green+h[i]+clear+h[i:])

    return count


def send_guess(guess):
    global c, hashes
    state = ""
    c.send(guess.encode())
    c.send(b'\n')
    line = c.recvline()
    if b'INVALID' not in line:
        line = line.decode().split('score: ')[1].strip()
        print(line)
        success = 0
        for idx, m in enumerate(re.finditer(e, line.encode())):
            if colors[m.group(1)] == 'green':
                if check(idx, m.group(2)) == 0:
                    success += 1
        if success > 60:
            print(c.recvline().decode())
            hashes = h_copy
            return "success"
    else:
        hashes.pop(guess)
        state = "invalid"
    c.send(b'1\n')
    c.recvuntil(b'guess: ')
    return state


h_copy = hashes.copy()
while hashes:
    guess = list(hashes.keys())[random.randint(0, len(hashes.keys())-1)]
    print(f"Sending {guess}")
    state = send_guess(guess)
    if state == "invalid":
        continue
    if state == "success":
        if 'y' in input("Shell? "):
            print("starting shell")
            while True:
                print(c.recvline().decode())
                c.send(input('$ ').encode())
        else:
            print(c.recvuntil(b'choose: '))
            c.send(b'1\n')
            print(c.recvuntil(b'guess: '))

    input('continue? ')
