import string 
import sys

digits = "0123456789"
b64_alphabet = string.ascii_uppercase + string.ascii_lowercase + digits + '+' + '/'

def encoding(data):

    encoded = ""

    data_bytes = "" # each char of data represented as byte 

    for char in data: # replace each char by it's byte value
        char_dec = ord(char)
        char_binary = format(char_dec, '08b') # 10 --> 00001010
        data_bytes += char_binary


    while len(data_bytes) % 6 != 0:  # we make data_bytes divisible by 6
        data_bytes += '0'

    chunks = [data_bytes[i:i+6] for i in range(0, len(data_bytes), 6)] # split data_bytes in chunks of 6 bits

    for chunk in chunks:
        chunk_dec = int(chunk, 2)
        encoded += b64_alphabet[chunk_dec]
    
    while len(encoded) % 4 != 0:  # adding base64 padding
        encoded += '='

    return encoded


def decoding(encoded):

    decoded = ""

    data_bytes = "" 

    for char in encoded:
        if char != '=': 
            char_dec = b64_alphabet.index(char)
            char_binary = format(char_dec, '06b') # 10 --> 001010
            data_bytes += char_binary

    chunks = [data_bytes[i:i+8] for i in range(0, len(data_bytes), 8)] # split data_bytes in chunks of 8 bits

    if '=' in encoded: # removing useless trailing zeros 
        chunks.pop()

    for chunk in chunks: # converting bytes to ascii char
        chunk_dec = int(chunk, 2)
        if chunk_dec != 0:
            decoded += chr(chunk_dec)

    return decoded


if len(sys.argv) > 2:

    option = sys.argv[1]
    data = sys.argv[2]

    if option == '-d' or option == '--decode':
        
        print( decoding(data))

    elif option == '-e' or option == '--encode':

        print( encoding(data))

    else:

        print("usage : pyb64.py <option> <data>")
    

else :

        print("usage : pyb64.py <option> <data>")

