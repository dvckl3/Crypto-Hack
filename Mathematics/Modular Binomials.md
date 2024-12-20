# Modular Binomials
![image](https://github.com/user-attachments/assets/935656ce-3586-46bc-841c-fb465745fa4b)

Bài này yêu cầu ta tìm hai ước nguyên tố $p,q$ của số $N$. Mọi người có thể lên [factordb.com](https://factordb.com/index.php?query=14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073)
để phân tích ra $p,q$ hoặc giả sử web bị sập thì mình có thể làm cách khác như sau :) 

Ta có 

$$\begin{cases}
c_{1} =( 2p+3q)^{e_{1}}\bmod N & \\
c_{2} =( 5p+7q)^{e_{2}}\bmod N & 
\end{cases}$$

Bằng khai triển nhị thức Newton ta sẽ có được 

$$\begin{cases}
c_{1} \equiv ( 2p)^{e_{1}} +( 3q)^{e_{1}}(\bmod N) & \\
c_{2} \equiv ( 5p)^{e_{2}} +( 7q)^{e_{2}}(\bmod N) & 
\end{cases}$$

Ta xét 

$$\begin{array}{l}
c_{1} \equiv ( 2p)^{e_{1}}(\bmod q)\\
c_{2} \equiv ( 5p)^{e_{2}}(\bmod q)\\
\Longrightarrow c_{1}^{e_{2}} \times 5^{e_{1} e_{2}} =( 10p)^{e_{1} e_{2}}\bmod q\\
\Longrightarrow c_{2}^{e_{1}} \times 2^{e_{1} e_{2}} =( 10p)^{e_{1} e_{2}}\bmod q
\end{array}$$


Sau đó ta lấy $\displaystyle \gcd\left( N,c_{1}^{e_{2}} \times 5^{e_{1} e_{2}} -c_{2}^{e_{1}} \times 2^{e_{1} e_{2}}\right) =q$ và tính được nốt $\displaystyle p$ còn lại. $ $

Code như sau : 
```python

```
