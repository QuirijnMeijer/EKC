# Representeert een implementatie van het Diffie-Hellman protocol

class DiffieHellman(object):
    """Encapsuleert de methoden gebruikt voor in het Diffie-Hellman protocol, K de elliptische kromme, k het genererend element"""

    __slots__ = ['K', 'k']

    def __init__(self, K, k):
        self.K = K
        self.k = k

    def __str__(self):
        return 'Actief: de groep (%s, +) met genererend element %s.' % (self.K, self.k)

    # Genereert een publieke sleutel xk
    def publiekeSleutel(self, x):
        return self.k**x

    # Vindt de gedeelde sleutel yxk
    def priveSleutel(self, P, y):
        return P**y
