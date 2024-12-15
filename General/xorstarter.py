from Cryptodome.Util.number import *
strings="label"
xor_value=13
result=''.join(chr(ord(char)^xor_value) for char in strings)
print(result)


