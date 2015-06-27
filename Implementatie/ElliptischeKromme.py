# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Beschrijft een elliptische kromme, desgewenst over een eindig lichaam.
import copy
from Punt import *

class ElliptischeKromme(object):
    """Een elliptische kromme y^2 = x^3 + ax + b over Fp vermeerderd met groepsoperaties"""

    __slots__ = ['a', 'b', 'p']

    def __init__(self, a=0, b=0, p=0):
        self.a = a
        self.b = b
        if p in range(1,4):
            p = 0
            print('De waarde p mag niet gelijk zijn aan 1, 2 of 3. De waarde 0 wordt gebruikt.')
        self.p = p

    def __str__(self):
        lichaam = 'R'
        if self.p > 0:
            lichaam = 'F' + str(self.p)
        return 'K(%s): y^2 = x^3 + %fx + %f' % (lichaam, self.a, self.b)

    # Optelling van twee punten gelegen op de kromme
    def vermeerder(self, P, Q):
        assert self.verifieer(P) and self.verifieer(Q), 'De parameters zijn niet compatibel.'
        if P == 'O' or Q == 'O':
            if P == 'O' and not Q == 'O':
                return Q
            elif Q == 'O' and not P == 'O':
                return P
            else:
                return 'O'
        elif P.x == Q.x and P.y == -1 * Q.y:
            return 'O'
        Z = Punt(self)
        if self.p == 0 and not P.isGelijk(Q):
            dydx = (Q.y - P.y)/(Q.x - P.x)
            Z.x = dydx**2 - P.x - Q.x
            Z.y = dydx * (Z.x - P.x) + P.y
        elif self.p == 0 and P.isGelijk(Q):
            dydx = (3 * (P.x)**2 + self.a)/(2 * P.y)
            Z.x = dydx**2 - 2 * P.x
            Z.y = dydx * (Z.x - P.x) + P.y
        elif self.p > 0 and not P.isGelijk(Q):
            # ---> Werkt nog niet
            dydx = ((Q.y - P.y) * (Q.x - P.x)**(-1)) % self.p
            Z.x = (dydx**2 - P.x - Q.x) % self.p
            Z.y = (dydx * (Z.x - P.x) + P.y) % self.p
            # <---
        elif self.p > 0 and P.isGelijk(Q):
            # ---> Werkt nog niet
            dydx = ((3 * (P.x)**2 + self.a) * (2 * P.y)**(-1)) % self.p
            Z.x = (dydx**2 - P.x - Q.x) % self.p
            Z.y = (dydx * (Z.x - P.x) + P.y) % self.p
            # <---
        Z = self.negatie(Z)
        return Z

    # Aftrekken van een punt gelegen op de kromme van een andere punt gelegen op de kromme
    def verminder(self, P, Q):
        return self.vermeerder(P, self.negatie(Q))

    # Scalaire vermenigvuldiging van een punt op de kromme
    def vermenigvuldig(self, P, n):
        Z = copy.deepcopy(P)
        i = 0
        while i < (n - 1):
            Z = self.vermeerder(Z, P)
            i += 1
        return Z

    # Negatie van een punt
    def negatie(self, P):
        if P == 'O':
            return 'O'
        Z = copy.deepcopy(P)
        Z.y *= -1
        return Z
    
    # Verifieert of het gegeven punt een punt op de kromme is
    def verifieer(self, P):
        val = False
        if type(P) == Punt and (P.K.a == self.a and P.K.b == self.b and P.K.p == self.p) and ((self.p == 0 and abs(P.x**3 + self.a * P.x + self.b - P.y**2) < 0.1) or (self.p > 0 and (P.y**2) % self.p == (P.x**3 + self.a * P.x + self.b) % self.p)):
            val = True
        if P == 'O':
            val = True
        return val
