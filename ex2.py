import math
from abc import ABC, abstractmethod
class FormeGeometrique(ABC):
    @abstractmethod
    def calculer_superficie(self):
        pass

    @abstractmethod
    def calculer_perimetre(self):
        pass

class Cercle(FormeGeometrique):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_superficie(self):
        return self.rayon **2 * math.pi
    def calculer_perimetre(self):
        return self.rayon * 2 * math.pi

class Carre(FormeGeometrique):
    def __init__(self, cote):
        self.cote = cote
    def calculer_superficie(self):
        return self.cote ** 2
    def calculer_perimetre(self):
        return self.cote * 4

cercle2 = Cercle(3)
print(f"""Superficie du cercle :"{cercle2.calculer_superficie()}
Perimetre du cercle :"{cercle2.calculer_perimetre()}""")
carre1 = Carre(3)
print("Superficie du carre :",carre1.calculer_superficie())
print("Perimetre du carre :",carre1.calculer_perimetre())
