def hex_to_base64(hex_string):
    bytes_data = binascii.unhexlify(hex_string)
    base64_data = base64.b64encode(bytes_data)
    return base64_data.decode('utf-8')
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
base64_string = hex_to_base64(hex_string)
print(base64_string)  
