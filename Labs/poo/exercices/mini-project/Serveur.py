from Utilisateur import Utilisateur

class Serveur(Utilisateur):
    def afficher_info(self):
        return f"Serveur: {self._nom}, ID: {self._id_utilisateur}"

    def prendre_reservation(self, reservation):
        # Logique pour enregistrer une nouvelle réservation
        pass

    def prendre_commande(self, commande):
        # Logique pour enregistrer une nouvelle commande
        pass

    def generer_facture(self, commande):
        # Logique pour créer une facture
        pass

    def consulter_reservations(self):
        # Logique pour afficher les réservations
        pass

    def consulter_commandes(self):
        # Logique pour afficher les commandes
        pass