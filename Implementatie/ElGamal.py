# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Een specifieke maar overschrijfbare afbeelding E: m -> Em, Em op K(Fp)
from ElliptischeKromme import *

class ElGamal(object):
    """Bevat een overschrijfbare afbeelding E en bijbehorende vertaalmethoden"""

    __slots__ = ['K', 'k', 'C', 'afbeelding']

    def __init__(self, K, k, C):
        self.K = K
        self.k = k
        self.C = C
        self.afbeelding = dict()
        alfabet = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # Stel de afbeelding op
        P = k
        i = 0
        while i < len(alfabet):
            P += k
            self.afbeelding[alfabet[i]] = P
            i += 1

    def __str__(self):
        val = "Actieve afbeelding in het ElGamal systeem:"
        for i in sorted(self.afbeelding):
            val += '\n%s: %s' % (i, self.afbeelding[i])
        return val

    # Verstelt de afbeelding naar opgegeven afbeelding
    def verstelAfbeelding(self, afb):
        self.afbeelding = afb

    # Vertaalt een punt naar een karakter
    def vertaalPunt(self, P):
        for a, Q in self.afbeelding.items():
            if Q.x == P.x and Q.y == P.y:
                if a == '_':
                    a = ' '
                return a

    # Vertaalt een karakter naar een punt
    def vertaalKarakter(self, a):
        if a == ' ':
            a = '_'
        return self.afbeelding[str(a)]

    # De afbeelding E
    def codeerBoodschap(self, m):
        val = []
        boodschap = list(m)
        for i in boodschap:
            val.append(self.vertaalKarakter(str(i)) + self.C)
        return val

    # De inverse afbeelding E^-1
    def decodeerBoodschap(self, Em):
        val = ''
        for i in Em:
            val += self.vertaalPunt(i - self.C)
        return val

    # Formateert de gecodeerde boodschap zodat deze te knippen en plakken is
    def formateerCode(self, c):
        val = '['
        for i in c:
            val += 'Punt(K, %d, %d), ' % (i.x, i.y)
        val = val[:-2] + ']'
        return(val)

    # Print de gecodeerde boodschappen in de vorm van een lijst van geordende punten op K(Fp)
    def printCode(self, c):
        val = '['
        for i in c:
            val += '%s, ' % (i)
        val = val[:-2] + ']'
        return(val)
