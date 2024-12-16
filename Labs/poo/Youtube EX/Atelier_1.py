class Salarie:
    def __init__(self, matricule = None, nom = None, prenom = None, salaire = None, tauxCs = None):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.tauxCs = tauxCs / 100
    def afficher(self):
        print(f"Matricule : {self.matricule}, Nom : {self.nom}, prenom :{self.prenom}, salaire :{self.salaire}, taux charge sociale : {self.tauxCs}")
    
    def calculer_salaire_net(self):
        salaire_net = self.salaire * self.tauxCs
        self.salaire -= salaire_net 
        return self.salaire
    

salarie1 = Salarie(53563, "ossama", "argaz" , 5000, 25)
salarie2 = Salarie(53564, "Ayoub", "argaz" , 10000, 25)

salarie1.afficher()
print(f"le salaire net est :{salarie1.calculer_salaire_net()} DH.")
print("---------------------------------------------------------------------")
salarie2.afficher()
print(f"le salaire net est :{salarie2.calculer_salaire_net()} DH.")
