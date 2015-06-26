# Representeert een implementatie van het Diffie-Hellman protocol

class DiffieHellman(object):
    """Encapsuleert de methoden gebruikt voor in het Diffie-Hellman protocol"""

    __slots__ = ['K', 'k']

    def __init__(self, K, k):
        self.K = K
        self.k = k

    def __str__(self):
        return 'Actief: de groep (%s, +) met genererend element %s.' % (self.K.__str__(), self.k.__str__())
    
