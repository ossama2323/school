# HERITAGE

class Perssone:
    # Methode
    def __init__(self,Nom,Age):
    # attribute  
        self.nom = Nom
        self.age = Age
    def afficher(self):
        print("Nom :" ,self.nom , "and Age :" ,self.age)
    

#Heritage d'une class
class Professeur(Perssone):
    def __init__(self,Nom,Age,Salaire):
        Perssone.__init__(self,Nom,Age)
        self.salaire = Salaire
    def afficher(self):
        super().afficher()

#Heritage d'une class
class Etudiant(Perssone):
    def __init__(self,Nom,Age,Note):
        Perssone.__init__(self,Nom,Age)
        self.note = Note


Prof1 = Professeur("Rachid",57,18000)
Etud1 = Etudiant("Ahmed",20,18)
print(Prof1.nom,Prof1.age,Prof1.salaire)
print(Etud1.nom,Etud1.age,Etud1.note)
Etud1.afficher()
