class Film:
    def __init__(self, titre, realisateur, duree_minutes):
        self.titre = titre
        self.realisateur = realisateur
        self.duree_minutes = duree_minutes
    def afficher(self):
        print(f"le filme est {self.titre} et le realisateur est {self.realisateur} et la durée de filme est {self.duree_minutes}")

class Salle():
    def __init__(self, numero_salle, capacite, sieges = []):
        self.numero_salle = numero_salle
        self.capacite = capacite
        self.sieges = sieges
    def afficher_salle(self):
        print(f"le numero de salle est {self.numero_salle} et son capacité {self.capacite}")
    def generer_siege(self):
        for i in range(len(self.sieges), self.capacite):
            siege = Siege(i + 1)
            self.sieges.append(siege)

    def afficher_siege_disponibles(self):
            print(f"il y a {len(self.sieges)} siege disponibles")


class Siege():
    def __init__(self, numero_siege, disponible = True):
        self.numero_siege = numero_siege
        self.disponible = disponible
    def afficher_status(self):
        if self._disponible:
            print("le siege est disponible")
        else:
            print("le siege est reserve")
    def reserver(self):
        self.disponible = False
    def liberer(self):
        self.disponible = True
    
    def __str__(self):
        return f" {self.numero_siege} {self.disponible}"


class Projection(Film):
    def __init__(self, titre, realisateur, duree_minutes, salle, heure):
        super().__init__(titre, realisateur, duree_minutes)
        self.heure = heure
        self.salle = salle
    def afficher_details(self):
        print(f"le filme est {self.titre} et le realisateur est {self.realisateur} et la durée de filme est {self.duree_minutes}  et le filme est projecter a la salle numero {self.salle} a {self.heure}", end=" ")

    def reserver_siege(self, numero_siege):
        self.numero_siege = numero_siege
        s = Salle(2, 50)
        if s.sieges[self.numero_siege].disponible == True:
            s.sieges[self.numero_siege].reserver()
        else:
            print(f"le siege {self.numero_siege} est deja reserver")

    def afficher_siege_reserver(self):
        s = Salle(2, 50)
        for m in s.sieges:
            if not m.disponible:
                print(f"les siege reserver sont {m.numero_siege}")


class Billet():
    def __init__(self, id_billet, projection, siege, prix):
        self.id_billet = id_billet
        self.projection = projection
        self.siege = siege
        self.prix = prix
    def afficher_billet(self):
        print(f"le billet numero {self.id_billet} est pour le filme {self.projection} et votre siege est {self.siege} et le prix de billet est {self.prix}")
        

class Client():
    def __init__(self, nom, id_client, billets = []):
        self.nom = nom
        self.id_client = id_client
        self.billets = billets
    def acheter_billet(self, projection, numero_siege, prix):
        self.projection = projection
        self.numero_siege = numero_siege
        self.prix = prix
        billet = Billet(len(self._billets) + 1, projection, projection._salle._sieges[numero_siege - 1], prix)
        self.billets.append(billet)
        
    def aficher_billets(self):
        if not self.billets:
            print("vous n'avez pas de billet")
            return
        print(f"les billets acheter par {self.nom} :")
        for billet in self.billets:
            print(billet)




class cinema():
    def __init__(self, films=[], salles=[], projection=[], clients=[]):
        self.films = films
        self.salles = salles
        self.projection = projection
        self.clients = clients

    def ajouter_film(self, film):
        self.films.append(film)

    def ajouter_salle(self, salle):
        self.salles.append(salle)

    def programmer_projection(self, projection):
        self.projection.append(projection)

    def enregistrer_client(self, client):
        self.clients.append(client)

    def afficher_projections(self):
        for p in self.projection:
            print(p)

    def afficher_client(self):
        for c in self.clients:
            print(c)



film1 = Film("fury", "HDO box", 270)
film2 = Film("jocker", "netflex", 140)
film3 = Film("1997", "egybest", 220)
salle1 = Salle(1, 50)
salle2 = Salle(2, 60)
salle3 = Salle(3, 45)

cinema.ajouter_film(film1)
cinema.ajouter_film(film2)
cinema.ajouter_film(film3)

cinema.ajouter_salle(salle1)
cinema.ajouter_salle(salle2)
cinema.ajouter_salle(salle3)


projection1 = Projection(film1.titre, film1.realisateur, film1.duree_minutes, 1, 16)
projection2 = Projection(film2.titre, film2.realisateur, film2.duree_minutes, 3, 20)
projection3 = Projection(film3.titre, film3.realisateur, film3.duree_minutes, 2, 23)


cinema.programmer_projection(projection1)
cinema.programmer_projection(projection2)
cinema.programmer_projection(projection3)
cinema.afficher_projections()

Salle.generer_siege(salle1.numero_salle, salle1.capacite)
Salle.generer_siege(salle2.numero_salle, salle2.capacite)
Salle.generer_siege(salle3.numero_salle, salle3.capacite)


client1 = Client("ossama", 1)
client2 = Client("ilyas", 2)
client3 = Client("ayoub", 3)

cinema.enregistrer_client(client1.nom, client1.id_client)
cinema.enregistrer_client(client2.nom, client2.id_client)
cinema.enregistrer_client(client3.nom, client3.id_client)


