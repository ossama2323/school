from Utilisateur import Utilisateur

class Administrateur(Utilisateur):
    def gerer_utilisateur(self, action, utilisateur, utilisateurs = []):
        if action == "ajouter utilisateur":
            utilisateurs.append(utilisateur)
            print(utilisateurs)
        elif action == "suprimer utilisateur":
            if utilisateur in utilisateurs:
                utilisateurs.remove(utilisateur)
                print(utilisateurs)
            else:
                print("L'utilisateur n'existe pas")
        elif action == "modifier l'utilisateur":
            if utilisateur in utilisateurs:
                utilisateur = input("Entrez le nouveau nom de l'utilisateur : ")
                utilisateur = input("Entrez le nouveau id de l'utilisateur : ")
                super().modifier_mot_de_passe(input("entrer le nouveau mot de passe : "))
            else:
                print("L'utilisateur n'existe pas")

    def afficher_info(self):
        return f"le nom d'utilisateur est {utilisateur._nom} de l'id {utilisateur._id_utilisateur}"
    
    def gerer_menus(self, action, article,article_menu = []):
        if action == "ajouter article":
            article_menu.append(article)
        elif action == "supprimer article":
            if article in article_menu:
                article_menu.remove(article)
            else:
                print("L'article n'existe pas")
        elif action == "modifier article":
            if article in article_menu:
                article = input("Entrez le nouveau nom de l'article : ")
        else:
            print("L'action n'est pas valide")


utilisateur = Administrateur("achiko", 1, "ossama_argaz")
utilisateur.gerer_utilisateur("ajouter utilisateur", utilisateur)
print(utilisateur.afficher_info())
# utilisateur.gerer_utilisateur("suprimer utilisateur", utilisateur)
utilisateur.gerer_utilisateur("modifier l'utilisateur", utilisateur)
print(utilisateur.afficher_info())
