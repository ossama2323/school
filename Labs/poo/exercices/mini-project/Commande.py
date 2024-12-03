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
        
