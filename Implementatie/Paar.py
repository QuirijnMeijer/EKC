# Bevat een natuurlijk getal a en het scalair product aP

class Paar(object):
    """Ondersteunende klasse voor het BabyStepGiantStep algoritme dat opslagruimte biedt voor paren [a, aP]"""

    __slots__ = ['a', 'aP']

    def __init__(self, a, aP):
        self.a = a
        self.aP = aP
