from abc import ABC, abstractmethod


class Media(ABC):
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculer_frais_location(self, duree: int):
        pass

class Livre(Media):
    def __init__(self, titre, auteur, prix):
        super().__init__(titre, auteur)
        self.prix = prix

    def get_info(self):
        return f"Livre: {self.titre} , Auteur: {self.auteur}"

    def calculer_frais_location(self, duree: int):
        return self.prix * duree

class magazine(Media):
    def __init__(self, titre, auteur, prix):
        super().__init__(titre, auteur)
        self.prix = prix

    def get_info(self):
        return f"Magazine: {self.titre} , Auteur: {self.auteur}"

    def calculer_frais_location(self, duree: int):
        return self.prix * duree

class DVD(Media):
    def __init__(self, titre, auteur, prix):
        super().__init__(titre, auteur)
        self.prix = prix

    def get_info(self):
        return f"DVD: {self.titre} , Auteur: {self.auteur} "

    def calculer_frais_location(self, duree: int):
        return self.prix * duree

class Bibliotheque:
    def __init__(self):
        self.medias = []

    def ajouter_media(self, media):
