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
      
    return key, message

   
print(single_bit_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
