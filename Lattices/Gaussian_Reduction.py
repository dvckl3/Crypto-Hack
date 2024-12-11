from sage.all import *
def gaussian_lattice_reduction(v1, v2):
    while True:
        if v2.norm() < v1.norm():
            v1, v2 = v2, v1
        m = round(v1.dot_product(v2) / v1.dot_product(v1))
        if m == 0:
            return v1, v2
        v2 = v2 - m * v1
v1 = vector([846835985, 9834798552])
v2 = vector([87502093, 123094980])
v1_reduced, v2_reduced = gaussian_lattice_reduction(v1, v2)
print("Vector rút gọn v1:", v1_reduced)
print("Vector rút gọn v2:", v2_reduced)
print(v1_reduced.dot_product(v2_reduced))
