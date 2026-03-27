from abc import ABC, abstractmethod

class CompteBancaire(ABC):
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} effectué. Nouveau solde : {self.solde}")

    @abstractmethod
    def calculer_interets(self):
        pass

class CompteEpargne(CompteBancaire):
    def calculer_interets(self):
        interets = self.solde * 0.01
        print(f"Intérêts (Compte Épargne) : {interets}")
        return interets


class CompteCourant(CompteBancaire):
    def calculer_interets(self):
        print("Les comptes courants n'ont pas d'intérêts.")
        return 0

compte_courant = CompteCourant()

compte_epargne.deposer(1000)
compte_courant.deposer(1000)

compte_epargne.calculer_interets()
compte_courant.calculer_interets()