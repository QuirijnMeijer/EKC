# Beschrijft een willekeurig punt en relateert deze aan een elliptische kromme.

class Punt(object):
    """Groepselement van een verzameling gegenereerd door een elliptische kromme, (x,y) verbonden aan de elliptische kromme K"""

    __slots__ = ['K', 'x', 'y']

    def __init__(self, K, x=0, y=0):
        self.K = K
        self.x = x
        self.y = y

    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)

    def __add__(self, Q):
        return self.K.vermeerder(self, Q)

    def __radd__(self, Q):
        return self.__add__(Q)

    def __sub__(self, Q):
        return self.K.verminder(self, Q)

    def __rsub__(self, Q):
        if Q == 'O':
            return self.K.negatie(self)
        else:
            return self.__sub__(Q)

    def __mul__(self, n):
        return self.K.vermenigvuldig(self, n)
    
    def __rmul__(self, n):
        return self.__mul__(n)

    def __pow__(self, n):
        return self.__mul__(n)

    # Controleert of het punt gelijk is aan het gegeven punt
    def isGelijk(self, Q):
        val = False
        if type(Q) == Punt and (Q.K.a == self.K.a and Q.K.b == self.K.b and Q.K.p == self.K.p) and self.x == Q.x and self.y == Q.y:
            val = True
        return val
        
