from Crypto.Util.number import *
from sage.all import *
e=65537
ct=948553474947320504624302879933619818331484350431616834086273
n=984994081290620368062168960884976209711107645166770780785733
factors=factor(n)
p,q=factors[0][0],factors[1][0]
phi=(p-1)*(q-1)

d=inverse(e,phi)
result=(pow(ct,d,n))
print(long_to_bytes(result))

