# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bijeenkomst klassen benodigd om het baby step, giant step algoritme uit te voeren.

from ElliptischeKromme import *
from BabyStepGiantStep import *

# Start van het script

K = ElliptischeKromme(2, 2, 17)
k = Punt(K, 0, 6)
BSGS = BabyStepGiantStep(K, k, 0)
print(BSGS)
d = tuple(map(int,input('Geef een doel op: ')[1:-1].split(',')))
D = Punt(K, d[0], d[1])
assert K.verifieer(D), 'Het opgegeven punt is niet compatibel.'
BSGS.verstelDoel(D)
c = BSGS.vindMacht()
P = K.vermenigvuldig(k, c)
print('De gevonden waarde van ν is %d. Opgegeven is het punt %s. Er geldt ν%s = %s.' % (c, D, k, P))
