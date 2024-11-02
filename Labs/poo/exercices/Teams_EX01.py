class Livre:
    def __init__(self, titre, auteur, isbn, nbrExemplaire):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nbrExemplaire = nbrExemplaire

    def afficher_details(self):
        print(f"Titre:{self.titre}\nAuteur:{self.auteur}\nISBN:{self.isbn}\nnombre d'exemplaires:{self.nbrExemplaire}")


class Membre(Livre):
    id = 1
    def __init__(self, nom, livres_empruntes =[]):
        self.nom = nom
        self.member_id = id
        self.livres_empruntes = livres_empruntes
        Membre.id+=1
    def emprunter_livre(self,livre):
        if livre not in self.livres_empruntes:
            self.livres_empruntes.append(livre)

    def afficher_listes_empruntes(self):
        for livre in self.livres_empruntes:
            print(livre.titre)

    def __str__(self):
        return f"id :{self.member_id} Nom : {self.nom}"



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
    def emprenter_livre(self,membre, livre):
        if livre not in self.membres.livres_empruntes:
            membre.livres_empruntes.append(livre)
        else:
            print(f"livre {livre.titre} est déja emprunter par {membre.nom}")
    def retourner_livre(self,membre, livre):
        if membre in self.membres:
            if livre in self.membres.liste_empruntes:
                membre.livres_empruntes.remove(livre)
            else:
                print(f"livres {livre.titre} n'est pas été emprunté par {membre.nom}")

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
    biblio = bibliotheque()
    choice = 5
    while choice != 0:
        menu()
        if choice == 1:
            if len(biblio.membres) > 0:
                print("-------------------- Livres ------------------")
                for livre in biblio.livres:
                    livre.afficher_details()
                    print("----------------------------------")
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
                print("membre ajouté avec succes")
            except:
                print("Saisie incorrecte")
        elif choice == 4 :
            for membre in biblio.membres:
                print(f"{biblio.membres.index(membre)} {membre.nom}")
            membreSelection = input("saisir le numero de membre pour afficher leur liste des empruntes: ")
            if biblio.membres[membreSelection] is not None:
                biblio.membres[membreSelection].afficher_listes_empruntes()
        elif choice == 5:
            for membre in biblio.membres:
                print(f"{biblio.membres.index(membre)} {membre.nom}")

            membreSelection = None
            while membreSelection is None:
                NumMembre = int(input("saisir le numero de membre : "))
                membreSelection = biblio.membres[NumMembre]
            
            for livre in biblio.membres:
                nbrEmprunt = 0
                for m in biblio.membres:
                    for l in m.liste_empruntes:
                        if l == livre:
                            nbrEmprunt += 1
                if nbrEmprunt < livre.nbrExemplaire:
                    print(f"{biblio.membres.index(livre)} {livre.titre}")

            livreSelection = 0
            while livreSelection is None:
                numlivre = input("saisir le numero de livre pour emprunter: ")
                livreSelection = biblio.membres[numlivre]
            biblio.emprenter_livre(membreSelection, livreSelection)

        elif choice == 6:
            print("---------------------------- Membres ----------------------------")
            for membre in biblio.membres:
                print(f"{biblio.membres.index(membre)} {membre.nom}")

            membreSelectionne = None
            while membreSelectionne is None:
                numMembre = int(input("Saisir le numéro du membre:"))
                membreSelectionne = biblio.membres[numMembre]

            print("---------------------------- Livres ----------------------------")
            for livre in membreSelectionne.livres_empruntes:
                print(f"{membreSelectionne.livres_empruntes.index(livre)} {livre.titre}")

            livreSelectionne = None
            while livreSelectionne is None:
                numLivre = int(input("Saisir le numéro du livre:"))
                livreSelectionne = membreSelectionne.livres_empruntes[numLivre]

            biblio.retourner_livre(membreSelectionne, livreSelectionne)

                




                






    