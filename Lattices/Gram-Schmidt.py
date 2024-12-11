from sage.all import *
v1 = vector([4, 1, 3, -1])
v2 = vector([2, 1, -3, 4])
v3 = vector([1, 0, -2, 7])
v4 = vector([6, 2, 9, -5])

def gram_schmidt(vectors):
    orthogonal_basic=[]
    for v in vectors:
      u=v
      for w in orthogonal_basic:
        u=u-(v.dot_product(w)/w.dot_product(w))*w
      orthogonal_basic.append(u)
    return orthogonal_basic


vectors=[v1,v2,v3,v4]
orthogonal_basic=gram_schmidt(vectors)
print(orthogonal_basic)


# hoặc trong sage cũng có tích hợp các hàm để tính cơ sở trực giao 
from sage.all import *
v1 = vector([4, 1, 3, -1])
v2 = vector([2, 1, -3, 4])
v3 = vector([1, 0, -2, 7])
v4 = vector([6, 2, 9, -5])
vectors=[v1,v2,v3,v4]
orthogonal_vectors, _ = matrix(vectors).gram_schmidt()
for vec in orthogonal_vectors:
    print(vec)
