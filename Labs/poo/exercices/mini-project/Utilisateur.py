from abc import ABC, abstractmethod
class Utilisateur(ABC):
    def __init__(self, nom, id_utilisateur, mot_de_passe):
        self._nom = nom
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe
    
    @abstractmethod
    def afficher_info(self):
        print(f"Administrateur: {self._nom}, ID: {self._id_utilisateur}")

    
    def modifier_mot_de_passe(self, nouveau_mot_de_passe):
        self._mot_de_passe = nouveau_mot_de_passe
    
    def __str__(self):
        return f"le nom est {self._nom} et l'id est {self._id_utilisateur}"

