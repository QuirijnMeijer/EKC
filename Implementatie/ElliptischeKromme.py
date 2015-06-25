# Beschrijft een elliptische kromme, desgewenst over een eindig lichaam.
import copy

class ElliptischeKromme(object):
    """Een elliptische kromme vermeerderd met groepsoperaties"""

    # y^2 = x^3 + ax + b

    __slots__ = ['a', 'b', 'p', 'foutmelding']

    # Standaardwaarden a,b,p moeten nog gekozen worden.
    def __init__(self, a=0, b=0, p=0):
        self.foutmelding = 'De opgegeven punten zijn niet compatibel.'
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
        assert verifieer(P) and verifieer(Q), self.foutmelding
        Z = Punt(self)
        if self.p == 0:
            dydx = (Q.y - P.y)/(Q.x - P.x)
            Z.x = dydx**2 - P.x - Q.x
            Z.y = dydx * (Z.x - P.x) + P.y
        else:
            Z.x = 0; Z.y = 0
        Z = self.negatie(Z)
        return Z

    # Aftrekken van een punt gelegen op de kromme van een andere punt gelegen op de kromme
    def verminder(self, P, Q):
        assert verifieer(P) and verifieer(Q), self.foutmelding
        return vermeerder(P, self.negatie(Q))

    # Scalaire vermenigvuldiging van een punt op de kromme
    def vermenigvuldig(self, P, n):
        assert verifieer(P) and verifieer(Q), self.foutmelding
        Z = copy.deepcopy(P)
        i = 0
        while i < n:
            self.vermeerder(Z, P)
            i += 1
        return Z

    # Negatie van een punt
    def negatie(self, P):
        Z = copy.deepcopy(P)
        Z.y *= -1
        return Z
    
    # Verifieert of P een punt op de kromme is
    def verifieer(self, P):
        val = False
        if type(P) == Punt: # en voldoet aan de vergelijking over Fp
            val = True
        return val
