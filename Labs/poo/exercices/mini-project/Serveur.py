from Utilisateur import Utilisateur
from Reservation import Reservation
from Commande import Commandes
from Facture import Facture
from Menu import Menu

class Serveur(Utilisateur):
    def __init__(self, reservations = [], commandes = []):
        self.reservations = reservations
        self.commandes = commandes

    def afficher_info(self):
        print(f"Administrateur: {self._nom}, ID: {self._id_utilisateur}")
    
    def prendre_reservation(self, reservation):
        self.reservation = reservation
        self.reservations.append(self.reservation)
        print(f"{self.reservation} a été enregistré avec succes: ")

    def prendre_commande(self, commande):
        self.commande = commande
        self.commandes.append(self.commande)
        print(f"{self.commande}. a été enregistré avec succes")

    def generer_facture(self,commande, facture):
        self.commande = commande
        self.facture = facture
        if self.commande in self.commandes:
            facture = f"facture d'id numero {self.facture.id_facture}, pour la commande d'ID numero {self.commande._id_commande}, commandé par {self.commande._reservation._nom_client}, la commande est {self.commande.statut}."
            print(facture)
            return facture
        else:
            print("la commande n'est pas enregistrée")

    def consulter_reservation(self):
        if not self.reservations:
            print("aucun reservation enregistrer")
        else:
            print("les reservation sont: ")
            for reservation in self.reservations:
                print(reservation)

    def consulter_commandes(self):
        if not self.commandes:
            print("aucun commande enregistrer")
        else:
            print("les commandes sont: ")
            for commande in self.commandes:
                print(commande)





s = Serveur()

reservation_1 = Reservation(1, "ossama", 5, "8/12", "18h30", 12)
commande_1 = Commandes(1, reservation_1)
menu_1 = Menu(1, "couscous", "avec les legumes", 160, "national")
facture_1 = Facture(1, commande_1, menu_1._prix, 20/100, 5/100)


s.prendre_reservation(reservation_1)
print("---------------------------------------------------")
s.prendre_commande(commande_1)
print("---------------------------------------------------")
s.generer_facture(commande_1, facture_1)
print("---------------------------------------------------")
s.consulter_reservation()
print("---------------------------------------------------")
s.consulter_commandes()
