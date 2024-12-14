# EXERCICE N1
# class CompteBancaire:
#     def __init__(self,numeroCompte,nom,solde):
#         self.numeroCompte = numeroCompte
#         self.nom = nom
#         self.solde = solde

#     def versement(self,versement):
#         self.solde = self.solde + versement
#     def retrait(self,versement):
#         self.solde = self.solde - versement
#     def __str__(self):
#          return "numero de compte :"+ str(self.numeroCompte) +"\n nom et prenom :"+ str(self.nom) + "\n solde :" + str(self.solde)

# moncompte = CompteBancaire(2005072300200, "Argaz Ossama", 18000)
# # print(moncompte.solde)
# # moncompte.versement(2300)
# # print(moncompte.solde)
# # moncompte.retrait(1000)
# # print(moncompte.solde)

# moncompte.__str__()
# print(moncompte.__str__())










# EXERCICE N2
# class Eleve:
#     def __init__(self, nom,note):
#         self.Nom = nom
#         self.Note = note
#     def moyenne(self):
#         return sum(self.Note)/len(self.Note)
#     def __str__(self):
#         return "Nom et Prenom :" +str(self.Nom) +"\n Moyenne :"+ str(self.moyenne())
    
# eleve1 = Eleve("argaz ossama",[17,18,10,10])
# print(eleve1)









# EXERCICE N3
class DateNaissance:
    from datetime import datetime

    def __init__(self,jour,mois,année):
        self.jour = jour
        self.mois = mois
        self.année = année
    def ToString(self):
        return str(self.jour) + "/"+str(self.mois) + "/" + str(self.année)
    
class Perssone:
    def __init__(self, nom, prenom, naissance):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
    def afficher(self):
        return "Nom and Prenom :" + str(self.nom) + " " + str(self.prenom)+ "\n Date de Naissance :"+ str(self.naissance)+"\n"
    
class Employé(Perssone):
    def __init__(self, nom, prenom, naissance,salaire):
        super().__init__(nom, prenom, naissance)
        self.salaire = salaire
    def afficher(self):
        return "Nom and Prenom :" + str(self.nom) + " " + str(self.prenom) + "\n Date de Naissance :" + str(self.naissance) + "\n Salaire :" + str(self.salaire)+ "\n"
    
class Chef(Employé):
    def __init__(self, nom, prenom, naissance,salaire, service):
        super().__init__(nom,prenom,naissance,salaire)
        self.service = service
    def afficher(self):
        return "Nom and Prenom :" + str(self.nom) + " " + str(self.prenom) + "\n Date de Naissance :"+ str(self.naissance)+ "\n Salaire :" + str(self.salaire) + "\n Service :" + str(self.service)

p= Perssone("Ossama","Argaz",DateNaissance(23,7,2005).ToString())
print(p.afficher())
E= Employé("ayoub","Argaz",DateNaissance(29,1,1999).ToString(),18000)
print(E.afficher())
CH= Chef("Ilyas","Argaz",DateNaissance(13,11,2000).ToString(),4000,"resource humaine")
print(CH.afficher())