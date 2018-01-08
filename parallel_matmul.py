
# input decomp stratejisi 
import multiprocessing
import numpy as np
from sys import argv
from functools import partial
# kullanim python parallel_matmul.py matris_boyutu thread_sayisi

n_thread = int(argv[1])
n_size = int(argv[2])

A = [ [2 for i in range(n_size)] for k in range(n_size) ]
B = [ [3 for i in range(n_size)] for k in range(n_size) ]

def vecmatmult(mat, vec):
    # global B use functools to get rid of this
    c = []
    for idx, el in enumerate(vec):
        res = 0
        for inner in mat[idx]:
            res+= inner * el
        c.append(res)

    return c

def main(a,b):
    pool = multiprocessing.Pool(n_thread)
    vecmatmultb = partial(vecmatmult, b) # Manual function currying
    c = pool.map(vecmatmultb, a)
    assert(np.array_equal(c, np.matmul(a,b)))

if __name__ == "__main__":
    main(A,B)