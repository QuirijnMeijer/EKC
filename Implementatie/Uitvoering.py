# --->
# Voor gebruik in IDLE (Windows):
# --->
import sys
import os
z = os.path.dirname(os.path.abspath(__file__))
sys.path.append(z)
# <---

# Bundeling van de verscheidene klassen, centraal punt voor uitvoering van de scripts.

from Ondersteuning import *
from ElliptischeKromme import *
from DiffieHellman import *

# ~ Onderstaand moet nog zo verwerkt worden dat het werkt in de command line.

# ~~~>
K = ElliptischeKromme(1, 1, 5)
k = Punt(K, 0, 1)
DH = DiffieHellman(K, k)
a = int(input('λ? '))
publiekeSleutelA = DH.publiekeSleutel(a)
print('De publieke sleutel van persoon A is %s' % publiekeSleutelA)
b = int(input('μ? '))
publiekeSleutelB = DH.publiekeSleutel(b)
print('De publieke sleutel van persoon B is %s' % publiekeSleutelB)
gedeeldeSleutelA = DH.priveSleutel(publiekeSleutelB, a)
gedeeldeSleutelB = DH.priveSleutel(publiekeSleutelA, b)
print('De geheime sleutel is [A] %s == %s [B]' % (gedeeldeSleutelA, gedeeldeSleutelB))
# <~~~
