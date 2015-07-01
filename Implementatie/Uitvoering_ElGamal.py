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
C = Punt(K, 5, 6)
EG = ElGamal(K, k, C)
print(EG)
boodschap = input('\nVoer een boodschap bestaand uit enkel kleine letters en spaties in:\n')
c = EG.codeerBoodschap(boodschap)
print('\nDe boodschap "%s" is gecodeerd:\n%s' % (boodschap, EG.printCode(c)))
origineel = EG.decodeerBoodschap(c)
print('\nDe code is terugvertaald naar:\n%s' % (origineel))
