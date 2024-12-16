class Facture():
    def __init__(self, id_facture, commande, total_ht, tvA, frais_service, totla_ttc = None): #Commande est Objet Commande associé.
        self.id_facture = id_facture
        self.commande = commande
        self.total_ht = total_ht
        self.tvA = tvA
        self.frais_service = frais_service
        self.totla_ttc = totla_ttc

    def afficher_facture(self):
        print(f"la facture de commande {self.commande}, d'id {self.id_facture}, le total hors taxes {self.total_ht}, le montant de tva {self.tvA}, les frais de service {self.frais_service}, et le total ttc {self.totla_ttc}")
        
    def calculer_total(self):
        TVA = 20 / 100
        frais_service = 5 / 100
        total = 0
        for article in self.commande._articles:
            total_ht = article._prix
            total_tva = article._prix + (article._prix * TVA)
            total_fs = article._prix + (article._prix * frais_service)
            total += total_ht + total_fs + total_tva + self.totla_ttc