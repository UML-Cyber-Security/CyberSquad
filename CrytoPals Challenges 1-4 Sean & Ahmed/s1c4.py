import fileinput
import linecache

def single_bit_xor(hex):
    best_score = 0
    message = None
    key = None
    ciphertext = bytes.fromhex(hex)
    ascii_table = list(range(97, 122)) + [32] 

    for letter in range(256):  
        byte_str = letter.to_bytes(1, byteorder='big')  * len(ciphertext)        
        plaintext = bytes([ x^y for (x,y) in zip(ciphertext, byte_str)]) 
        score = sum([j in ascii_table for j in plaintext]) 

        
        if score > best_score or not best_score:
            best_score = score 
            message = plaintext.decode("utf-8", "ignore")              
            key = chr(letter)       
      
    return key, message, best_score

oldBest = 0
i = 0

for line in fileinput.input(files ='s1c4text.txt'):
    i = i + 1
    key, message, best = single_bit_xor(line)
    if(best > oldBest):
        oldBest = best
        keyAt = i

print(single_bit_xor(linecache.getline('s1c4text.txt', keyAt)))