enc_flag được tạo ra bằng cách lấy secret_key ^ 'crypto{...}' = enc_flag. Khóa ở đây ta có thể dự đoán rằng nó được lặp lại liên tục tức là dùng 1 khóa < len(flag)
để xor. Như vậy thông thường key 1 byte có độ dài là 8 bit cho nên khi ta xor phần đầu là crypto{ sẽ chỉ được 7 bit đầu. Để tạo ra key đủ 8 bit ta cần lấy thêm 1 bit nữa.
```python
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) # output: 'myXORke+y...'
```
Có vẻ key chuẩn là `myXORkey`. 
Bài này mình thấy khá lạ vì thông thường ta không thể biết được liệu key gốc ban đầu có đúng là 8 bit hay không :)) tùy tình huống mà ta cần phải bruteforce hết tất cả các khả năng có thể có.
Tệ nhất là phải chọn ra một key có độ dài không vượt quá enc_flag.
Code như sau: 
```python
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) 
print(xor('myXORkey'.encode(),flag))
```
