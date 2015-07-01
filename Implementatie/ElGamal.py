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

    __slots__ = ['K', 'k', 'afbeelding']

    def __init__(self, K, k):
        self.K = K
        self.k = k
        self.afbeelding = dict()
        alfabet = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        return val #"Actieve afbeelding in het ElGamal systeem:\n%s" % (self.afbeelding)

    def verstelAfbeelding(self, afb):
        self.afbeelding = afb

    def vertaalPunt(self, P):
        #vertaalPunt
        return 0

    def vertaalKarakter(self, a):
        #vertaalLetter
        return 0

    def codeerBoodschap(self, m):
        #codeerBoodschap
        return 0

    def decodeerBoodschap(self, Em):
        #decodeerBoodschap
        return 0
