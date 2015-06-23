# Beschrijft een elliptische kromme, desgewenst over een eindig lichaam.
import copy

class ElliptischeKromme(object):
    """Een elliptische kromme vermeerderd met groepsoperaties"""

    # y^2 = x^3 + ax + b

    __slots__ = ['a', 'b', 'p']

    # Standaardwaarden a,b,p moeten nog gekozen worden.
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def __str__(self):
        lichaam = 'R'
        if self.p > 0:
            lichaam = 'F' + str(self.p)
        return 'K(%s): y^2 = x^3 + %fx + %f' % (lichaam, self.a, self.b)

    # ------>
    # Deze methoden overhevelen naar de klasse Punt? Rest uit te vinden hoe de parameters van de kromme overgedragen worden.
    # ------>
    #def __add__(self, P, Q):
    #    return self.vermeerder(P, Q)
    #
    #def __sub__(self, P, Q):
    #    return self.vermeerder(P, self.vermenigvuldig(-1, Q))
    #
    #def __mul__(self, s, P):
    #    return self.vermenigvuldig(s, P)
    # <------

    # Optelling van twee punten gelegen op de kromme
    def vermeerder(self, P, Q):
        return 0

    # Scalaire vermenigvuldiging van een punt op de kromme
    def vermenigvuldig(self, s, P):
        return 0

    # Negatie van een punt gelegen op de kromme
    def negatie(self, P):
        Z = copy.deepcopy(P)
        Z.y *= -1
        return Z

    # Herhaalde optelling van een punt gelegen op de kromme
    def macht(self, P, m):
        Z = copy.deepcopy(P)
        i = 0
        while i < m:
            self.vermeerder(Z, P)
            i += 1
        return Z
