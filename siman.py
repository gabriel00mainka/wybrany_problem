from RandomNumberGenerator import *
import numpy as np
from random import randint
from random import random
from cmax import *
from operator import attrgetter
from copy import copy

n = 15   # zadania
m = 3   # maszyny
z = 752 # seed

random1 = RandomNumberGenerator(z)

class zrob:
    def __init__(self,numer):
        self.numer = numer
        self.czasy = []
        for i in range(m):
            self.czasy.append(random1.nextInt(1,29))   # dodawanie czasów na m maszyn

tab_zadania = []    # pusta tabela zadan
for k in range(n):
    tab_zadania.append(zrob(k))  # przydzielanie zadań z przydzielonymi czasami na m maszyn

def Simulated_Annealing(zadania):
    T_start = 1234 # temperatura poczatkowa
    T = T_start
    T_koniec = 0.1
    n = len(zadania)
    m = len(zadania[0].czasy)
    wewn_iter = int(np.sqrt(n*m))   # ilosc wewnetrznych iteracji

    pi = copy(zadania)  # rozwiazanie startowe
    pi_z_gwiazdka = copy(pi)
    pi.sort(key=attrgetter("numer"))    # permutacja naturalna

    while T > T_koniec:
        for k in range(wewn_iter):
            i = randint(0,n-1)
            j = randint(0,n-1)
            pi_nowe = copy(pi)
            pi_nowe[i], pi_nowe[j] = pi_nowe[j], pi_nowe[i] # zamiana i na j
            Calc_pi = CMAX(pi)
            Calc_pi_nowe = CMAX(pi_nowe)
            delta_C_max = Calc_pi - Calc_pi_nowe
            if Calc_pi_nowe > Calc_pi:
                r = random()    # losowanie liczby z zakresu [0,1]
                if r >= np.exp(delta_C_max/T):
                    pi_nowe = copy(pi)
            pi = copy(pi_nowe)

            if CMAX(pi) < CMAX(pi_z_gwiazdka):
                pi_z_gwiazdka = copy(pi)

        T -= 80 # zmniejszanie liniowe
    
    return pi_z_gwiazdka

pi = Simulated_Annealing(tab_zadania)
print([i.numer for i in pi])