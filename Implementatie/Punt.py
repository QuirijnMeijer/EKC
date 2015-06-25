# Beschrijft een punt gelegen op een elliptische kromme.
# Aggratie door een instantie van een elliptische kromme.

class Punt(object):
    """Groepselement van een verzameling gegenereerd door een elliptische kromme"""

    __slots__ = ['K', 'x', 'y']

    def __init__(self, K, x=0, y=0):
        self.K = K
        self.x = x
        self.y = y

    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)

    def __add__(self, Q):
        return K.vermeerder(self, Q)

    def __sub__(self, Q):
        return K.verminder(self, Q)

    def __mul__(self, n):
        return K.vermenigvuldig(self, n)

    # Controleert of het punt gelijk is aan het gegeven punt.
    def isGelijk(self, Q):
        val = False
        if type(Q) == Punt and self.x == Q.x and self.y == Q.y:
            val = True
        return val
        
