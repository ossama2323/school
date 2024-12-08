class CalculateurFinancier():
    def calculer_tva(self, montant, taux=0.20):
        self.montant = montant
        tva = montant + montant * taux
        print(tva)
        
    def calculer_frais_service(self, montant, taux=0.05):
        self.montant = montant
        frais_service = montant + montant * taux
        print(frais_service)