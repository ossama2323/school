from Utilisateur import Utilisateur

class Authentification(Utilisateur):
    def __init__(self, nom, id_utilisateur, mot_de_passe, role):
        super().__init__(nom, id_utilisateur, mot_de_passe)
        self.role = role

    def se_connecter(self, id_utilisateur, mot_de_passe, role):
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe
        self._role = role
        