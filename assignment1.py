import numpy as np

def find_period(L0, L1):
    g = 9.81
    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print("When L = %4.1f m, T = %3.1f s" % (L, T))
    return

find_period(2, 10)
        
