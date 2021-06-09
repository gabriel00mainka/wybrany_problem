from neh import *
from RandomNumberGenerator import *
import numpy as np
from operator import attrgetter
from copy import copy
from random import randint
from random import random


def SimulatedAnnealing(zadania):
    T_start = CMAX(zadania) + 50 # temperatura poczatkowa
    T = T_start
    T_koniec = 0.1
    n = len(zadania)
    m = len(zadania[0].czasy)
    wewn_iter = int(np.sqrt(n*m))   # ilosc wewnetrznych iteracji

    pi = copy(zadania)  # rozwiazanie startowe
    pi_ = copy(pi)
    pi.sort(key=attrgetter("numer"))    # permutacja naturalna

    while T > T_koniec:
        for k in range(wewn_iter):
            i = randint(0,n-1)
            j = randint(0,n-1)
            pi_nowe = copy(pi)
            pi_nowe[i], pi_nowe[j] = pi_nowe[j], pi_nowe[i] # zamiana i na j
            Cpi = CMAX(pi)
            Cpi_nowe = CMAX(pi_nowe)
            dC = Cpi - Cpi_nowe
            if Cpi_nowe > Cpi:
                r = random()    # losowanie liczby z zakresu [0,1]
                if r >= np.exp(dC/T):
                    pi_nowe = copy(pi)
            pi = copy(pi_nowe)

            if CMAX(pi) < CMAX(pi_):
                pi_ = copy(pi)
        T = 0.97*T
    return pi_