from Utilisateur import Utilisateur
from Serveur import Serveur

class ChefDeCuisine(Utilisateur):
    def afficher_info(self):
        for utilisateur in self.utilisateurs:
            if utilisateur in self.utilisateurs:
                return f"le nom d'utilisateur est {self._nom} de l'id {self._id_utilisateur}"
            else:
                return "il y a aucun utilisateur"
            
    def consulter_commandes(self):
        print(f"les commandes en cours sont: ")
        for commande in self.commandes:
            print(f"la commande {commande} est en cours")

c = ChefDeCuisine("achiko", 1, "ossama_argaz")

c.consulter_commandes()