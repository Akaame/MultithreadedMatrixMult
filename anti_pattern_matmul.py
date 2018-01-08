
# input decomp stratejisi 
import multiprocessing
import numpy as np
from sys import argv
# kullanim python anti_pattern_matmul.py matris_boyutu thread_sayisi

n_size = int(argv[1])
n_thread = int(argv[2])

A = [ [2 for i in range(n_size)] for k in range(n_size) ]
B = [ [3 for i in range(n_size)] for k in range(n_size) ]

def vecmatmult(vec):
    global B # BAD!
    c = []
    for idx, el in enumerate(vec):
        res = 0
        for inner in B[idx]:
            res+= inner * el
        c.append(res)

    return c

def main(a):
    pool = multiprocessing.Pool(n_thread)
    c = pool.map(vecmatmult, a) # map sadece top-level scope icinde mevcut olan fonksiyonlar ile calisiyor.
    assert(np.array_equal(c, np.matmul(A,B)))

if __name__ == "__main__":
    main(A)