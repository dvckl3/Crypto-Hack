import time
def brute_for_xor(data,delay=0):
    encrypted_data=bytes.fromhex(data)
    results=[]
    for key in range(256):
        try:
            xor_result=bytes([a ^ key for a in encrypted_data])
            utf8_result=xor_result.decode('utf-8')
            if utf8_result.isprintable():
                result=f"Key:{hex(key)} | Decrypted: {utf8_result}"
                results.append(result)
                print(result)
                if delay > 0 :
                    time.sleep(delay)
        except UnicodeDecodeError:
            continue
    return results
brute_for_xor('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d',delay=0.1)                
 
                    
