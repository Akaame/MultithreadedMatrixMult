from sys import argv
# kullanim: python single_matmul.py matris_boyutu
import numpy as np
n_size = int(argv[1])

A = [ [2 for i in range(n_size)] for k in range(n_size) ]
B = [ [3 for i in range(n_size)] for k in range(n_size) ]

def vecmatmult(vec, mat):
    c = []
    for idx, el in enumerate(vec):
        res = 0
        for inner in mat[idx]:
            res+= inner * el
        c.append(res)
    return c

def matmatmult(a,b):
    res = []
    for vec in a:
        res.append(vecmatmult(vec,b))
    return res

assert( np.array_equal(np.matmul(A,B), matmatmult(A,B)))
