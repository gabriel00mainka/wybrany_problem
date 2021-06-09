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

# tab = np.zeros([n,m],dtype=int)
# for i in range(n):
#     for j in range(m):
#         tab[i,j]=random.nextInt(1,29)
# print(tab)

# def NEH(tab_zadania):
#     pi = np.zeros((n,1),dtype=int)  # stworzenie zerowego wektora
#     k = 1

#     W=np.zeros([tab_zadania.shape[0],2],dtype=int)
#     for i in range(tab_zadania.shape[0]):
#         W[i,0]=tab_zadania[i,:].sum()
#         W[i,1]=i

#     while W.shape[0]:   # shape -> ile jest zadan
#         numer_zadania=W[np.argmax(W[:,0]),1]

#         for l in range(1,k+1):
#             if 
# NEH(tab)