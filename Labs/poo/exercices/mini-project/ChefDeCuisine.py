from Utilisateur import Utilisateur

class ChefDeCuisine(Utilisateur):
    def afficher_info(self):
        return f"Chef de Cuisine: {self._nom}, ID: {self._id_utilisateur}"

    def consulter_commandes(self):
        # Logique pour afficher les commandes en cours
        pass

    def mettre_a_jour_statut_commande(self, commande, statut):
        # Logique pour mettre à jour le statut d'une commande
        pass