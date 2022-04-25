from Crypto.Hash import SHA256
from itertools import product
from string import ascii_lowercase


'''
produces a file in the following format (word hash):

drubbing ac747669ea65501ec906927d4c74d025bc2ecd1d606098b38c307922ffc29ff4
drubbings 0b6a97b95718b3bef2ee9d03aca2549605b35601bf0dc572a134824b10b4b15e
drubble 7849443f3614fd341506ae7168d8b7f17e701976febe4f87a16009af2bcf0c05
drubbly d461f3c5bc2bbf6ac542601bd4f1428f56376633e3aa1ea1db417225b6e92b9f
'''

def random():
    with open("hashes", 'w+') as f:
        for i in range(1,6):
            for combination in product(ascii_lowercase, repeat=i):
                h = SHA256.new()
                h.update(''.join(combination).encode())
                f.write(''.join(combination) + ' ' + h.hexdigest() + '\n')

def dictionary():
    with open("/usr/share/dict/words", 'r') as words:
        with open("hashes-d", 'w') as f:
            for word in words:
                word = word.strip()
                h = SHA256.new()
                h.update(word.encode())
                f.write(word + ' ' + h.hexdigest() + '\n')


def passwords():
    with open("~/Documents/SecLists/Passwords/xato-net-10-million-passwords-1000000.txt", 'r') as words:
        with open("hashes-d", 'w') as f:
            for word in words:
                word = word.strip()
                h = SHA256.new()
                h.update(word.encode())
                f.write(word + ' ' + h.hexdigest() + '\n')

dictionary()
