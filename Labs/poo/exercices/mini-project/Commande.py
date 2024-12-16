from Menu import Menu
from Reservation import Reservation

class Commandes():
    def __init__(self, id_commande, reservation , articles = []): # articles[] Liste des objets Menu commandés.
        self._id_commande = id_commande
        self._reservation = reservation
        self._articles = articles
        self.statut = "en cours"
        
    def ajouter_article(self, article_menu):
        self._articles.append(article_menu)
    
    def afficher_commandes(self):
        print(f"Commande de l'id {self._id_commande}, la commande est {self.statut}, commandé par {self._reservation._nom_client}")
    
    def calculer_total(self):
        TVA = 20 / 100
        frais_service = 5 / 100
        total = 0
        for article in self._articles:
            total += article._prix + (article._prix * TVA)
            total += total * frais_service
        print(total)

    def __str__(self):
        return f"Commande de l'id {self._id_commande}, Réservation de l'ID: {self._reservation._id_reservation}, la commande est {self.statut}, commandé par {self._reservation._nom_client}"
    

menu_1 = Menu(1, "couscous", "avec les legumes", 160, "national")
reservation_1 = Reservation(1, "ossama", 5, "8/12", "18h30", 12)


commande_1 = Commandes(1, reservation_1)

commande_1.ajouter_article(menu_1)
commande_1.afficher_commandes()
commande_1.calculer_total()