from copy import copy
import numpy as np
from operator import attrgetter
from RandomNumberGenerator import *
from cmax import *

n = 15   # zadania
m = 3   # maszyny
z = 752 # seed

random = RandomNumberGenerator(z)

class zrob:
    def __init__(self,numer):
        self.numer = numer
        self.czasy = []
        for i in range(m):
            self.czasy.append(random.nextInt(1,29))   # dodawanie czasów na m maszyn

tab_zadania = []    # pusta tabela zadań
for k in range(n):
    tab_zadania.append(zrob(k))  # przydzielanie zadań z przydzielonymi czasami na m maszyn

print("---------------------\nczasy zadan:\n---------------------")
for i in tab_zadania:
    print(i.czasy)

def NEH(tab_zadania):
    pi = np.zeros((n,1),dtype=int)  # stworzenie zerowego wektora
    k = 1

    W = np.zeros((n,2),dtype=int)
    i = 0
    for j in tab_zadania:
        w = sum(j.czasy)
        W[i,0] = w
        W[i,1] = i
        i+=1
    print(W)
    pi1 = []    # pi'
    pi2 = []    # pi*

    numer_zadania = np.argmax(W,axis=0)[0]
    for a in tab_zadania:
        if a.numer == W[numer_zadania,1]:
            ob = a
    print(numer_zadania)
    pi1.append(ob)
    pi2.append(ob)
    k = 2
    W = np.delete(W,numer_zadania,axis=0)
    print(W)
    while W.shape[0] > 0:
        lista = []
        numer_zadania = np.argmax(W,axis=0)[0]
        for a in tab_zadania:
            if a.numer == W[numer_zadania,1]:
                ob = a
        # print(numer_zadania)
        for l in range(k):
            pi1 = copy(pi2)
            pi1.insert(l,copy(ob))
            lista.append(CMAX(pi1))
            pi1.pop(l)      # usuwanie l
        print(lista)
        najmniejsza = min(lista)    # wartosc cmax
        index = lista.index(najmniejsza) # index zadania dla ktorego cmax mnajmniejszy
        
        print(index)    #
        pi2.insert(index,copy(ob))
        W = np.delete(W,numer_zadania,axis=0)
        print(W)    # to co zostalo do uszeregowania
        k+=1
    for i in pi2:    
        print(i.numer+1,end=" ")    # kolejnosc wykonywania zadan
    print()
    print(CMAX(pi2))
NEH(tab_zadania)