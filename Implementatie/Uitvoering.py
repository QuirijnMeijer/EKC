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

# <Uit te voeren code>

# ~ Onderstaand moet nog zo verwerkt worden dat het werkt in de command line.

# ~~~>
K = ElliptischeKromme(0, 17, 0)
P = Punt(K, -1, 4)
DH = DiffieHellman(K, P)
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
