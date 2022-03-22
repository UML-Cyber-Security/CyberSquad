import codecs

def hex_to_b64(hex):
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(hex_to_b64(hex))


