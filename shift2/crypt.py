import base64
import hashlib

import .layers

def sumstr(x: str) -> int:
    output = 0

    for char in x:
        output += ord(char)

    return output

def key2shifts(key: str) -> list:
    output = []

    # Check if key should get hashed
    if sumstr(key) % 2 == 1:
        key = str(hashlib.sha256(key.encode()).hexdigest())
        #print(key)

    for char in key:
        output.append(ord(char))

    return output

# def encode(file, key):
#     # Encode once to allow for binary data
#     file = base64.b64encode(file.encode()).decode()
#     output = ""

#     # Iterate and shift
#     for i, byte in enumerate(file):
#         # Mod the current bit
#         output += chr(ord(byte) + key[i%len(key) - 1])

#         # Mod the key
#         key.append(i%key[0])

#     # Final encoding
#     output = base64.b64encode(output.encode())

#     # Return as string
#     return output.decode()

# def decode(file, key):
#     # Decode the file to shifted bytes
#     file = base64.b64decode(file.encode()).decode()
#     output = ""

#     for i, byte in enumerate(file):
#         # Unmod the current byte
#         mod = ord(byte) - key[i%len(key) - 1]
#         if mod not in range(0x110000):
#             mod = 0
#         output += chr(mod)

#         # Mod the current key
#         key.append(i%key[0])

#     # Pull the resulting b64 back to binary if needed
#     # This may fail due to "incorrect padding" from a wrong key
#     # Just return some random text in this case for now
#     try:
#         output = base64.b64decode(output.encode()).decode()
#     except:
#         output = output

#     # Return as bytes
#     return output

crypt_layers = [
    layers.DataHeaderLayer(),
    layers.BitshiftLayer()
    
]

def encode(file, key):
    return layers.execLayerSeq(crypt_layers, file, key)

def decode(file, key):
    return layers.execLayerSeq(crypt_layers, file, key, decode=True)