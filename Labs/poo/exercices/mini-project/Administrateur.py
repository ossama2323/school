from Utilisateur import Utilisateur

class Administrateur(Utilisateur):
    def afficher_info(self):
        print(f"Administrateur: {self._nom}, ID: {self._id_utilisateur}")
    
    def gerer_utilisateur(self, action, utilisateur, utilisateurs = []):
        self.action = action
        self.utilisateur = utilisateur
        self.utilisateurs = utilisateurs
        if action == "ajouter utilisateur":
            utilisateurs.append(utilisateur)
            print(f"l'utilisateur {self._nom} a été ajouter avec succes")
        elif action == "suprimer utilisateur":
            if utilisateur in utilisateurs:
                utilisateurs.remove(utilisateur)
                print(f"l'utilisateur {self._nom} a été supprimer avec succes et les utilisateurs sont: ")
                for u in utilisateurs:
                    print(u._nom)
            else:
                print("L'utilisateur n'existe pas")
        elif action == "modifier l'utilisateur":
            utilisateur._nom = input("Entrez le nouveau nom de l'utilisateur : ")
            utilisateur._id_utilisateur = int(input("Entrez le nouveau id de l'utilisateur : "))
            super().modifier_mot_de_passe(input("entrer le nouveau mot de passe : "))
            print(f"l'utilisateur {self._nom} a ete modifier avec succes.")
            print("les utilisateurs sont :")
            for u in utilisateurs:
                print(u)
        else:
            print("entrer une action valide")
    def gerer_menus(self, action, article = None, article_menu = []):
        self.action = action
        self.article = article
        if action == "ajouter article":
            article_menu.append(article)
            print(f"l'article {article} a été ajouter par {self.utilisateur._nom} avec succes")
            print("les articles disponible sont: ")
            for a in article_menu:
                    print(a)
        elif action == "supprimer article":
            if article in article_menu:
                article_menu.remove(article)
                print(f"l'article {article} a été supprimer par {self.utilisateur._nom} avec succes et les articles disponible sont: ")
                for a in article_menu:
                    print(a)
            else:
                print("L'article n'existe pas")
        elif action == "modifier article":
            print("voici le menu des article: ")
            for a in enumerate(article_menu):
                print(a)
            article_index = int(input("entrer l'index de l'element a modifier: "))
            if article_menu[article_index] in article_menu:
                article_menu[article_index] =  input("Entrez le nouveau nom de l'article : ")
                print("l'article a été modifier avec succes et les article disponible sont : ")
                for a in enumerate(article_menu):
                    print(a)
            else:
                print("L'article n'existe pas")
        else:
            print("L'action n'est pas valide")

utilisateur_1 = Administrateur("achiko", 1, "ossama_argaz")
utilisateur_2 = Administrateur("ilias", 2, "ilias_argaz")
utilisateur_3 = Administrateur("ayoub", 3, "ayoub_argaz")

utilisateur_1.gerer_utilisateur("ajouter utilisateur", utilisateur_1)
utilisateur_2.gerer_utilisateur("ajouter utilisateur", utilisateur_2)
utilisateur_3.gerer_utilisateur("ajouter utilisateur", utilisateur_3)

print("-------------------------------------------------------------------------")
# utilisateur_1.gerer_utilisateur("suprimer utilisateur", utilisateur_1)
print("-------------------------------------------------------------------------")
# utilisateur_2.gerer_utilisateur("suprimer utilisateur", utilisateur_2)
print("-------------------------------------------------------------------------")
# utilisateur_3.gerer_utilisateur("suprimer utilisateur", utilisateur_3)
# utilisateur_1.gerer_utilisateur("modifier l'utilisateur", utilisateur_1)
# utilisateur_2.gerer_utilisateur("modifier l'utilisateur", utilisateur_2)
# utilisateur_3.gerer_utilisateur("modifier l'utilisateur", utilisateur_3)
print("-------------------------------------------------------------------------")
# utilisateur_1.gerer_menus("ajouter article", "flan")
print("-------------------------------------------------------------------------")
# utilisateur_1.gerer_menus("ajouter article", "flan")
print("-------------------------------------------------------------------------")
# utilisateur_1.gerer_menus("supprimer article", "flan")
print("-------------------------------------------------------------------------")
# utilisateur_1.gerer_menus("modifier article")