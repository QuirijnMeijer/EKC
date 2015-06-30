# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bundeling van alles benodigd voor een poging het discreet logaritmisch probleem te breken.
from Paar import *
import math

class BabyStepGiantStep(object):
    """Algoritme om het discreet logaritmisch probleem in een groep gegenereerd door het punt k op de elliptische kromme K te breken"""

    __slots__ = ['K', 'k', 'm', 'D', 'Z', 'tabel']

    def __init__(self, K, k, m):
        self.K = K
        self.k = k
        self.m = m
        if self.m == 0:
            self.m = math.ceil(2 * math.sqrt(K.p) + K.p + 1)
        self.reset()

    # Herstelt de gehele instantie naar standaardwaarden
    def reset(self):
        self.tabel = []
        self.D = 'O'
        self.Z = self.D
        self.vulTabel()

    # Vult de tabel met elementen jk
    def vulTabel(self):
        j = 0
        while j < self.m:
            self.tabel.append(Paar(j, self.k**j))
            j += 1

    # Verstelt het element waar naar gezocht wordt
    def verstelDoel(self, D):
        self.D = D
        self.Z = D

    # Doorzoekt de tabel en vergelijkt alle elementen om ν te bepalen
    def vindMacht(self):
        i = 0
        while i < self.m:
            self.Z += self.K.negatie(self.k)
            j = 1
            while j < self.m:
                if not self.verkrijgElement(i) == 'O' and not self.Z == 'O' and self.Z.isGelijk(self.verkrijgElement(i)):
                    return i*self.m+j
                j += 1
            i += 1

    # Verkrijg het element op index j in de tabel
    def verkrijgElement(self, j):
        return self.tabel[j].aP
