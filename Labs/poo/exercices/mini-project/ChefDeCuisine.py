from Utilisateur import Utilisateur
from Serveur import Serveur
from Commande import Commandes
from Reservation import Reservation


class ChefDeCuisine(Utilisateur):
    def afficher_info(self):
        print(f"Administrateur: {self._nom}, ID: {self._id_utilisateur}")

    def consulter_commandes(self,serveur):
        print(f"les commandes en cours sont: ")
        for commande in serveur.commandes:
            print(f"la commande {commande._id_commande} est en cours")
    
    def mettre_a_jour_statut_commande(self, serveur, commande, statut):
        self.commande = commande
        self.statut = statut
        for self.commande in serveur.commandes:
            if self.commande._id_commande == commande._id_commande:
                self.commande.statut = statut
                print(self.commande)
            else:
                print("la commandes n'existe pas")

s = Serveur()


reservation_1 = Reservation(1, "ossama", 5, "8/12", "18h30", 12)
commande_1 = Commandes(1, reservation_1)

c = ChefDeCuisine("achiko", 1, "ossama_argaz")
print("---------------------------------------------------")
c.consulter_commandes(s)
print("---------------------------------------------------")
c.mettre_a_jour_statut_commande(s, commande_1, "terminer")
