# Biedt ondersteunende methoden zonder directe verbindtenis aan de hoofdklassen.
import time

# Evalueert een getal als priemgetal
def isPriem(getal):
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

# Registreert verstreken tijd benodigd voor uitvoering van een methode
# ---> klok(f, [argumenten])
def klok(f, args):
    A = time.perf_counter()
    result = f(*args)
    B = time.perf_counter()
    return [result, B-A]
