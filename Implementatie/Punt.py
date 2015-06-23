# Beschrijft een punt gelegen op een elliptische kromme.
# Aggratie door een instantie van een elliptische kromme.

class Punt(object):
    """Groepselement van een verzameling gegenereerd door een elliptische kromme"""

    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
