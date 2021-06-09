from neh import *
from RandomNumberGenerator import *
import numpy as np
from operator import attrgetter
from copy import copy
from random import randint
from random import random


def SA(zadania):
    T_start = CMAX(zadania) + 50 # temperatura poczatkowa
    T = T_start
    Tend = 0.1
    n = len(zadania)
    m = len(zadania[0].czasy)
    L = int(np.sqrt(n*m))   # ilosc wewnetrznych iteracji

    pi = copy(zadania)  # rozwiazanie startowe
    pi_gw = copy(pi)
    pi.sort(key=attrgetter("numer"))    # permutacja naturalna

    while T > Tend:
        for k in range(L):
            i = randint(0,n-1)
            j = randint(0,n-1)
            pi_new = copy(pi)
            pi_new[i], pi_new[j] = pi_new[j], pi_new[i] # zamiana i na j
            Cpi = CMAX(pi)
            Cpi_new = CMAX(pi_new)
            dC = Cpi - Cpi_new
            if Cpi_new > Cpi:
                r = random()    # losowanie liczby z zakresu [0,1]
                if r >= np.exp(dC/T):
                    pi_new = copy(pi)
            pi = copy(pi_new)

            if CMAX(pi) < CMAX(pi_gw):
                pi_gw = copy(pi)

        T = 0.97*T
    
    return pi_gw