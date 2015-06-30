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
P = Punt(K, 0, 6)
Z = P**6
B = BabyStepGiantStep(K, P, 0)
B.verstelDoel(Z)
