def fixed_XOR(hex1, hex2):
    num = int(hex1,base=16) ^ int(hex2,base=16)
    return hex(num)  

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

print(fixed_XOR(hex1, hex2))