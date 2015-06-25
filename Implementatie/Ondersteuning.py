# Biedt ondersteunende methoden zonder directe verbindtenis aan de hoofdklassen.
import time

class Ondersteuning(object):
    """Algemene methoden"""

    # Evalueert een getal als priemgetal
    def isPriem(self, getal):
        if getal < 2:
            return False
        elif getal == 2:
            return True
        # Een even getal is nooit een priemgetal
        elif getal%2 == 0:
            return False
        # Wanneer deze stap bereikt wordt is het getal > 2
        else:
            i = 3; m = getal/2
            while i < m:
                if getal % i == 0:
                    return False
                # Sla even getallen over
                i += 2
            return True

    #
    # bevatPunt wordt vervangen door ElliptischeKromme::verifieer(P)
    #
    
    # Controleert of een kromme een punt bevat
    def bevatPunt(self, kromme, punt):
        a = kromme.a; b = kromme.b; p = kromme.p
        x = punt.x; y = punt.y
        # Indien p = 0 is het lichaam R. Zoniet, 0 < x,y < p.
        if (p == 0 or (x in range(0, p) and y in range(0, p))) and x**3 + a*x + b - y**2 == 0:
            return True
        else:
            return False

    # Registreert verstreken tijd na uitvoering verzameling methoden.
    def klok(self, methoden):
        A = time.perf_counter()
        # Voer methoden in de list methoden uit. Moet nog bepaald worden hoe parameters en returns afgehandeld worden.
        B = time.perf_counter()
        return B-A
