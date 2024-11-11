class Membre:
    def __init__(self,nom,age, frais_adhesion):
        self.nom = nom
        self.age = age
        self.frais_adhesion = frais_adhesion
    def calculer_frais_annuels(self):
        return self.frais_adhesion
    def limit_emprunt(self):
        livres_empruntes = ["livre1", "livre2"]
        limite_livre = 3
        if len(livres_empruntes) > limite_livre:
            return "Vous avez atteint la limite d'emprunt"
        else:
            return "Vous pouvez emprunter des livres"

class AdultMembre(Membre):
    def __init__(self,nom,age, frais_adhesion, frais_supplementaire):
        super().__init__(nom, age, frais_adhesion)
        self.__frais_supplementaire = frais_supplementaire
    def calculer_frais_annuels(self):
        return super().calculer_frais_annuels() + self.__frais_supplementaire
    def limit_emprunt(self):
        livres_empruntes = ["livre1", "livre2"]
        limite_livre = 10
        # super().limit_emprunt()
        if self.age >= 18 and len(livres_empruntes) > limite_livre:
            return "Vous avez atteint la limite d'emprunt"
        else:    
            return "Vous êtes un adulte, vous pouvez emprunter plus de livres"
        

class EnfantMembre(Membre):
    def __init__(self,nom,age, frais_adhesion):
        super().__init__(nom, age, frais_adhesion)
    def calculer_frais_annuels(self):
        return super().calculer_frais_annuels() / 2
    def limit_emprunt(self):
        livres_empruntes = ["livre1", "livre2","livre3", "livre4","livre5", "livre6"]
        limite_livre = 5
        if self.age < 18 and len(livres_empruntes) > limite_livre:
            return "Vous avez atteint la limite d'emprunt"
        else:
            print("Autorisation parentale requise")
            return "Vous êtes un enfant, vous pouvez emprunter just 5 livres"


class SeniorMembre(Membre):
    def __init__(self, nom, age, frais_adhesion, pourcentage_rabais):
        super().__init__(nom, age, frais_adhesion)
        self.__pourcentage_rabais = pourcentage_rabais
    def calculer_frais_annuels(self):
        return super().calculer_frais_annuels() - self.__pourcentage_rabais
    def limit_emprunt(self):
        livres_empruntes = []
        limite_livre = 7
        if len(livres_empruntes) > limite_livre:
            return "Vous avez atteint la limite d'emprunt"
        else:
            return "Vous pouvez emprunter just 7 livres"
        



Nom = input("enter your name: ")
Age = int(input("enter your age: "))
Frais_adhesion = 20
Frais_supplementaire = 10
pourcentage_rabais = 25 / 100

membre = Membre(Nom, Age, Frais_adhesion)

adulte = AdultMembre(Nom, Age, Frais_adhesion, Frais_supplementaire)

enfant = EnfantMembre(Nom, Age, Frais_adhesion)

senior = SeniorMembre(Nom, Age, Frais_adhesion, pourcentage_rabais)

liste_object = [membre, adulte, enfant, senior]


for membres in liste_object:
    print(membres.calculer_frais_annuels())
    print("----------------------------------")
    print(membres.limit_emprunt())
    print("----------------------------------")
