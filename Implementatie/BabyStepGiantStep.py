# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bundeling van methoden benodigd voor een poging het discreet logaritmisch probleem te breken.
from Paar import *
import math

class BabyStepGiantStep(object):
    """Algoritme om het discreet logaritmisch probleem in een groep gegenereerd door het punt k op de elliptische kromme K te breken. Stel m=0 wanneer de |K(fp)| onbekend is."""

    __slots__ = ['K', 'k', 'm', 'D', 'Z', 'tabel']

    def __init__(self, K, k, m):
        assert K.p > 0, 'De opgegeven elliptische kromme is ongeldig.'
        self.K = K
        self.k = k
        self.m = m
        if self.m == 0:
            self.m = math.ceil(2 * math.sqrt(K.p) + K.p + 1)
        self.reset()

    def __str__(self):
        return 'Actief: de groep [%s, +] met genererend element %s en doel %s.' % (self.K, self.k, self.D)

    # Herstelt de gehele instantie naar standaardwaarden
    def reset(self):
        self.tabel = []
        self.verstelDoel('O')
        self.vulTabel()

    # Vult de tabel met elementen k^j
    def vulTabel(self):
        self.tabel.append(Paar(0, 'O'))
        j = 1
        while j < self.m:
            self.tabel.append(Paar(j, self.k**j))
            j += 1

    # Verkrijg het element op index j in de tabel
    def verkrijgElement(self, j):
        return self.tabel[j].aP

    # Verstelt het element waar naar gezocht wordt
    def verstelDoel(self, D):
        self.D = D
        self.Z = D

    # Doorzoekt de tabel en vergelijkt alle elementen om ν te bepalen
    def vindMacht(self):
        i = 1
        increment = self.K.negatie(self.k)**self.m
        while i < self.m:
            self.Z += increment
            j = 1
            while j < self.m:
                if not (self.verkrijgElement(j) == 'O' and self.Z == 'O') and self.Z.isGelijk(self.verkrijgElement(j)):
                    return i*self.m+j
                elif self.verkrijgElement(j) == 'O' and self.Z == 'O':
                    return i*self.m+j
                j += 1
            i += 1
