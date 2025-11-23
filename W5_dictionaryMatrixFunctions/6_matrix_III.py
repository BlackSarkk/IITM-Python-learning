# Initialise C to Zero.
# I need to consider two matrices A and B.
# I need to find the dot product of two lists.
# I need to pick ith row and jth column in a matrix.


def initialize_mat(dim):
# Code_Verified, works perfectly fine on the test cases

    C = []
    for i in range (dim):
        C.append([])
    for i in range (dim):
        for j in range(dim):
            C[i].append(0)
    return C


def dot_product(u, v):      # Assuming u = v
    dim = len(u)    
    ans = 0
    for i in range (dim):
        ans += u[i]*v[i]
    return ans

def row(M, i):
    dim=len(M)
    l=[]
    for k in range (dim):
        l.append(M[i][k])
    return l

def column(M, j):
    dim=len(M)
    l=[]
    for k in range (dim):
        l.append(M[k][j])
    return l


def mat_multiplication(A, B):
    dim=len(A)
    C=initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A, i), column(B, j))
    return C







A = [[1, 2, 3],[1, 8, 3],[2, 2, 4]]
B = [[1, 2, 6],[11, 8, 3],[21, 2, 4]]

print(mat_multiplication(A, B))


import numpy
print(numpy.mat(A)*numpy.mat(B))