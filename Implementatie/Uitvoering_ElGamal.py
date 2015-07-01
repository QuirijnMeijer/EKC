# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Samenvoeging klassen voor een demonstratie van het ElGamal systeem.

from ElliptischeKromme import *
from ElGamal import *

# Start van het script

K = ElliptischeKromme(5, 1, 23)
k = Punt(K, 0, 1)
EG = ElGamal(K, k)
print(EG)
