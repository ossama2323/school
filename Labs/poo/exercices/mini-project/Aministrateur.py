from Utilisateur import Utilisateur

class Administrateur(Utilisateur):
    def afficher_info(self):
        return f"Administrateur: {self._nom}, ID: {self._id_utilisateur}"

    def gerer_utilisateurs(self, action, utilisateur):
        # Logique pour gérer les utilisateurs
        pass

    def gerer_menus(self, action, article_menu):
        # Logique pour gérer les articles du menu
        pass

    def generer_rapports(self):
        # Logique pour générer des rapports
        pass