import numpy as np

def CMAX(pi):     # dla x maszyn
    n = len(pi)         # len() - dlugosc
    m = len(pi[0].czasy)
    C = np.zeros((n,m), dtype=int)      # stworzenie zerowego wektora

    C[0,0] = pi[0].czasy[0]

    for i in range(1,m):
        C[0,i] = C[0,i-1] + pi[0].czasy[i]      # pierwszy wiersz macierzy
    
    for i in range(1,n):
        C[i,0] = C[i-1,0] + pi[i].czasy[0]      # pierwsza kolumna macierzy

    for i in range(1,n):
        for j in range(1,m):
            C[i,j] = max(C[i-1,j], C[i,j-1]) + pi[i].czasy[j]
    
    return int(C[n-1,m-1])
