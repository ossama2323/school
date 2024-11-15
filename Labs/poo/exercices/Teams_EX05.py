class Film:
    def __init__(self, titre, realisateur, duree_minutes):
        self._titre = titre
        self._realisateur = realisateur
        self._duree_minutes = duree_minutes
    def afficher(self):
        print(f"le filme est {self._titre} et le realisateur est {self._realisateur} et la durée de filme est {self._duree_minutes}")
f = Film("colombiana", "ossama", 120)
f.afficher()

class salle():
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
        self._heure = heure
        self._salle = salle
    def afficher_details(self):
        super().afficher() + print(f" et le filme est projecter a la salle numero {self._salle} a {self._heure}", end=" ")

    def reserver_siege(self, numero_siege):
        self.numero_siege = numero_siege
        s = salle(2, 50)
        if s.sieges[self.numero_siege].disponible == True:
            s.sieges[self.numero_siege].reserver()
        else:
            print(f"le siege {self.numero_siege} est deja reserver")

    def afficher_siege_reserver(self):
        s = salle(2, 50)
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
        b = Billet(44, p, 3, 320)
        billet = Billet(b.id_billet, b.projection, b.siege, b.prix)
        self.billets.append(billet)


            
sa = salle(2, 50)
sa.afficher_salle()
sa.generer_siege()
sa.afficher_siege_disponibles()
for s in sa.sieges:
    print(s)

p = Projection("colombiana", "ossama", 120, 2, 7)
p.reserver_siege(2)
p.reserver_siege(7)
p.reserver_siege(4)

for s in sa.sieges:
    print(s)

p.afficher_siege_reserver()

b = Billet(44, p, 3, 320)
b.afficher_billet()

c = Client("ossama", 21)
c.acheter_billet(p, 4, 320)