import csv
from Administrateur import Administrateur
from Gestion_fichiers import Gestion_fichier

class Authentification():            
    # accounts = [["mot de passe", "ID", "Role"],
    #             ["ossama", 1, "admin"],
    #             ["ilyas", 2, "serveur"],
    #             ["ayoub", 3, "chef_de_cuisin"]]
    # def __init__(self):
    #     comptes = open("comptes_users.csv", "w", encoding="utf-8")
    #     comptes_writer = csv.writer(comptes, delimiter=";")
    #     for ligne in Administrateur._utilisateurs:
    #         comptes_writer.writerow(ligne)
    
    def afficher_info(self):
        print(f"Administrateur: {self._nom}, ID: {self._id_utilisateur}")
    
    def se_connecter(self, nom,  id_utilisateur , mot_de_passe):
        self._nom = nom
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe

        with open("comptes_users.csv", "r", encoding="utf-8") as comptes:
            comptes_reader = csv.reader(comptes, delimiter=";")
            next(comptes_reader)
            for line in comptes_reader:
                    if line:
                        if line[0] == str(nom) and line[1] == str(id_utilisateur) and line[2] == str(mot_de_passe):
                            print("Connexion réussie")
                            return
            print("Connexion échouée")


a = Authentification()
a.se_connecter("ilias", 2, "ilias_argaz")

        