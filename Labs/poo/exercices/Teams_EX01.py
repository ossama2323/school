class Livre:
    def __init__(self, titre, auteur, isbn, nbrExemplaire):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nbrExemplaire = nbrExemplaire

    def afficher_details(self):
        print("enter titre : " + self.titre)
        print("enter auteur : " + self.auteur)
        print("enter isbn : " + str(self.isbn))
        print("enter nbrExemplaire : " + str(self.nbrExemplaire))

livre1 = Livre("harry poter", "ossama", "123", 1)
print("----------------------------------- livre ------------------------------------")
print(Livre.afficher_details(livre1))


class membre(Livre):
    def __init__(self, nom, member_id, livres_empruntes =[]):
        self.nom = nom
        self.member_id = member_id
        self.livres_empruntes = livres_empruntes
    def emprunter_livre(self,livre):
        for livre in self.livres_empruntes:
            if livre == self.titre:
                return self.livres_empruntes.append(livre)
            else:
                print("livre deja emprenter")
    def afficher_listes_empruntes(self):
        print("livres empruntes : ")
        print(self.livres_empruntes)



class bibliotheque(Livre):
    def __init__(self,livres = [], membre = []):
        self.livres = livres
        self.membres = membre

    def ajouter_livre(self, livre,):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres.remove(livre)

    def enregistrer_membre(self, membre):
        self.membres.append(membre)

    def chercher_livre_par_titre(self,titre):
        for livre in self.livres:
            if titre == livre.titre:
                return livre
        return None
    