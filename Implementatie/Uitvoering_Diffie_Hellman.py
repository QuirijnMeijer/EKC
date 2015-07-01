# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bundeling van de verscheidene klassen, centraal punt voor uitvoering van de scripts gerelateerd aan het Diffie-Hellman protocol.

from ElliptischeKromme import *
from DiffieHellman import *

# Start van het script

K = ElliptischeKromme(1, 1, 5)
k = Punt(K, 0, 1)
DH = DiffieHellman(K, k)
print(DH)
a = int(input('λ? '))
publiekeSleutelA = DH.publiekeSleutel(a)
print('De publieke sleutel van persoon A is %s' % publiekeSleutelA)
b = int(input('μ? '))
publiekeSleutelB = DH.publiekeSleutel(b)
print('De publieke sleutel van persoon B is %s' % publiekeSleutelB)
gedeeldeSleutelA = DH.priveSleutel(publiekeSleutelB, a)
gedeeldeSleutelB = DH.priveSleutel(publiekeSleutelA, b)
print('De gedeelde geheime sleutel is [A] %s == %s [B]' % (gedeeldeSleutelA, gedeeldeSleutelB))
