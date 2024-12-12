# Successive Powers


![image](https://github.com/user-attachments/assets/6fea2732-8090-40b5-ab8a-d63c3e2c36f0)

Ta có thể bruteforce như sau:
```python
from sympy import isprime
powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
prime=[x for x in range(100,1000) if isprime(x)]

for p in prime:
    for x in range(1,p):
        for i,power in enumerate(powers):
            if i==len(powers)-1:
                print(f"valid p and x is {p},{x}")
            elif not (x*power)%p==powers[i+1]: break
```
Một cách khác đó là ta biết rằng các số $\displaystyle 588,665,216,113,642,...$ là các lũy thừa với số mũ tăng dần giữa $\displaystyle x$ và $\displaystyle p$ tức là $\displaystyle x^{n} =588(\bmod p) ,x^{n+1} =665(\bmod p)$ và cứ như vậy. 
