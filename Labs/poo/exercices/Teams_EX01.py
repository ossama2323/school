class Livre:
    def __init__(self, titre, auteur, isbn, nbrExemplaire):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nbrExemplaire = nbrExemplaire

    def afficherDetails(self):
        print(f"Titre:{self.titre}\nAuteur:{self.auteur}\nISBN:{self.isbn}\nnombre d'exemplaires:{self.nbrExemplaire}")

class Membre:
    id=1
    def __init__(self, nom):
        self.nom=nom
        self.member_id = Membre.id
        self.livres_empruntes=[]
        Membre.id += 1

    def emprunter_livre(self, livre):
        if livre not in self.livres_empruntes:
            self.livres_empruntes.append(livre)

    def afficher_liste_emprunts(self):
        for livre in self.livres_empruntes:
            print(livre.titre)

    def __str__(self):
        return f"Id:{self.member_id} Nom:{self.nom}"

class Bibliotheque:
    def __init__(self):
        self.liste_livres = []
        self.liste_membres = []

    def ajouter_livre(self, livre):
        self.liste_livres.append(livre)

    def supprimer_livre(self, livre):
        self.liste_livres.remove(livre)

    def enregistrer_membre(self, membre):
        self.liste_membres.append(membre)

    def chercher_livre_par_titre(self, titre):
        for livre in self.liste_livres:
            if livre.titre == titre:
                return livre

    def emprunter_livre(self, membre, livre):
        if livre not in membre.livres_empruntes:
            membre.livres_empruntes.append(livre)
        else:
            print(f"Livre {livre.titre} est déjà emprunté par {membre.nom}")

    def retourner_livre(self, membre, livre):
        if membre in self.liste_membres:
            if livre in membre.livres_empruntes:
                membre.livres_empruntes.remove(livre)
            else:
                print(f"Livre {livre.titre} n'est pas emprunté par {membre.nom}")

def menu():
    print("-------------------- Menu --------------------")
    print("1 - Voir la liste des livres")
    print("2 - Ajouter un livre")
    print("3 - Ajouter un membre")
    print("4 - Afficher les emprunts d'un membre")
    print("5 - Enregistrer un emprunt")
    print("6 - Enregistrer un retour")
    print("0 - Quitter")

if __name__ == '__main__':
    #l'instanciation
    biblio = Bibliotheque()
    choice = 5
    while choice != 0:
        menu()
        choice = int(input("Saisir votre choix : "))
        if choice == 1:
            if len(biblio.liste_membres) > 0:
                print("---------------------------- Livres ----------------------------")
                for livre in biblio.liste_livres:
                    livre.afficherDetails()
                    print("------------------------------")
            else:
                print("\nListe de livres vide.\n")
        elif choice == 2:
            try:
                titre = input("Saisir le titre:")
                auteur = input("Saisir l'auteur:")
                isbn = input("Saisir l'ISBN:")
                nbrEx = int(input("Saisir le nombre d'exemplaires:"))
                livre = Livre(titre, auteur, isbn, nbrEx)
                biblio.ajouter_livre(livre)
                print("Livre ajouté avec succès.")
            except:
                print("Saisie incorrecte")
        elif choice == 3:
            try:
                nom = input("Saisir le nom:")
                membre = Membre(nom)
                biblio.enregistrer_membre(membre)
                print("Membre ajouté avec succès.")
            except:
                print("Saisie incorrecte")
        elif choice == 4:
            for membre in biblio.liste_membres:
                print(f"{biblio.liste_membres.index(membre)} {membre.nom}")

            membreSelectionne = int(input("Saisir le numéro du membre pour voir la liste des emprunts:"))
            if biblio.liste_membres[membreSelectionne] is not None:
                biblio.liste_membres[membreSelectionne].afficher_liste_emprunts()
        elif choice == 5:
            for membre in biblio.liste_membres:
                print(f"{biblio.liste_membres.index(membre)} {membre.nom}")

            membreSelectionne = None
            while membreSelectionne is None:
                numMembre = int(input("Saisir le numéro du membre:"))
                membreSelectionne = biblio.liste_membres[numMembre]

            for livre in biblio.liste_livres:
                nbrEmprunt = 0
                for m in biblio.liste_membres:
                    for l in m.livres_empruntes:
                        if l==livre:
                            nbrEmprunt+=1
                if nbrEmprunt < livre.nbrExemplaire:
                    print(f"{biblio.liste_livres.index(livre)} {livre.titre}")

            livreSelectionne = None
            while livreSelectionne is None:
                numLivre = int(input("Saisir le numéro du livre:"))
                livreSelectionne = biblio.liste_livres[numLivre]

            biblio.emprunter_livre(membreSelectionne, livreSelectionne)
        elif choice == 6:
            print("---------------------------- Membres ----------------------------")
            for membre in biblio.liste_membres:
                print(f"{biblio.liste_membres.index(membre)} {membre.nom}")

            membreSelectionne = None
            while membreSelectionne is None:
                numMembre = int(input("Saisir le numéro du membre:"))
                membreSelectionne = biblio.liste_membres[numMembre]

            print("---------------------------- Livres ----------------------------")
            for livre in membreSelectionne.livres_empruntes:
                print(f"{membreSelectionne.livres_empruntes.index(livre)} {livre.titre}")

            livreSelectionne = None
            while livreSelectionne is None:
                numLivre = int(input("Saisir le numéro du livre:"))
                livreSelectionne = membreSelectionne.livres_empruntes[numLivre]

            biblio.retourner_livre(membreSelectionne, livreSelectionne)