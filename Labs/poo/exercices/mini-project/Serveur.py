from Utilisateur import Utilisateur

class Serveur(Utilisateur):
    def __init__(self):
        self.reservations = []
        self.commandes = []
    def afficher_info(self):
        for utilisateur in self.utilisateurs:
            if utilisateur in self.utilisateurs:
                return f"le nom d'utilisateur est {self._nom} de l'id {self._id_utilisateur}"
            else:
                return "il y a aucun utilisateur"
    def prendre_reservation(self, reservation):
        self.reservation = reservation
        self.reservations.append(self.reservation)
        print(f"{self.reservation} a été enregistré avec succes: ")
    def prendre_commande(self, commande):
        self.commande = commande
        self.commandes.append(self.commande)
        print(f"{self.commande}. a été enregistré avec succes")
    def generer_facture(self,commande):
        self.commande = commande
        if self.commande in self.commandes:
            facture = f"facture pour la commande {self.commande}."
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

s.prendre_reservation("la table 12 le 8/12 a 18h30")
print("---------------------------------------------------")
s.prendre_commande("un couscous marocain pour deux perssone et deux limonades et un flan")
print("---------------------------------------------------")
s.generer_facture("un couscous marocain pour deux perssone et deux limonades et un flan")
print("---------------------------------------------------")
s.consulter_reservation()
print("---------------------------------------------------")
s.consulter_commandes()