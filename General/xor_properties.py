key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_key1='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_key3='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_key1_key3_key2='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

def xor_operation(data1,data2):
    bytes1=bytes.fromhex(data1)
    bytes2=bytes.fromhex(data2)
    return bytes([a^b for a,b in zip(bytes1,bytes2)]).hex()


k2=xor_operation(key1,key2_key1)
k3=xor_operation(k2,key2_key3)
flag=xor_operation(xor_operation(xor_operation(flag_key1_key3_key2,key1),k2),k3)
sol=bytes.fromhex(flag).decode('utf-8')
print(sol)
