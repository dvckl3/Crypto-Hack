from Crypto.Util.number import *
from sage.all import *
from gmpy2 import *
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
plaintext=gmpy2.iroot(ct,3)[0]
flag=long_to_bytes(plaintext)
print(flag)
