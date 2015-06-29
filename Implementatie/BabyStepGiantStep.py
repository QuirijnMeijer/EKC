# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bundeling van alles benodigd voor een poging het discreet logaritmisch probleem te breken.
from Paar import *

class BabyStepGiantStep(object):
    """Algoritme om het discreet logaritmisch probleem in een groep gegenereerd door het punt k op de elliptische kromme K te breken"""

    __slots__ = ['K', 'k', 'tabel']

    def __init__(self, K, k):
        self.K = K
        self.k = k
        self.leegTabel()

    def leegTabel(self):
        self.tabel = []

    def voegIn(sigma, ksigma):
        self.tabel.append(Paar(sigma, ksigma))
