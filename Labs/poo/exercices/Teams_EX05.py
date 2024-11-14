class Film:
    def __init__(self, titre, realisateur, duree_minutes):
        self._titre = titre
        self._realisateur = realisateur
        self._duree_minutes = duree_minutes
    def afficher(self):
        print(f"le filme est {self._titre} et le realisateur est {self._realisateur} et la durée de filme est {self._duree_minutes}")

class salle():
    def __init__(self, numero_salle, capacite, sieges = []):
        self.numero_salle = numero_salle
        self.capacite = capacite
        self.sieges = sieges
    def get_sieges(self):
        return self._sieges
    def afficher_salle(self):
        print(f"le numero de salle est {self.numero_salle} et son capacité {self.capacite}")
    def generer_siege(self):
        siege = 0
        for siege in range(self.capacite):
            if self.capacite > len(self.sieges):
                self.sieges.append(siege)
                siege += 1
            else:
                print("la salle est pleine")             
    def afficher_siege_disponibles(self):
        if len(self.sieges) < self.capacite:
            print(f"il y a {self.capacite - len(self.sieges)} siege disponibles")
        else:
            print("li n'y a pas de siege disponible")


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
        if self._disponible:
            self._disponible = False
            print("le siege est reserver")
    def liberer(self):
        if not self._disponible:
            self._disponible = True
            print("le siege est disponible")




class Projection(Film):
    def __init__(self, titre, realisateur, duree_minutes, salle, heure):
        super().__init__(titre, realisateur, duree_minutes)
        self._heure = heure
        self._salle = salle
    def afficher_details(self):
        super().afficher() + print(f" et le filme est projecter a la salle numero {self._salle} a {self._heure}", end=" ")
    def reserver_siege(self, numero_siege):
        self.numero_siege = numero_siege
        s = salle()
        for self.numero_siege in range (len(s._sieges)):
            if s._sieges[self.numero_siege].disponible == True:
                s._sieges[self.numero_siege].reserver()
            else:
                print(f"le siege {self.numero_siege} est deja reserver")

    def afficher_siege_reserver(self):
        for s in range(self._salle.sieges):
            if not s.disponible:
                print(f"les siege reserver sont {s.numero_siege}")


class Billet():
    def __init__(self, id_billet, projection, siege, prix):
        self._id_billet = id_billet
        self._projection = projection
        self._siege = siege
        self._prix = prix
    def afficher_billet(self):
        p = Projection()
        si = Siege()
        print(f"le billet numero {self._id_billet} est pour le filme {p.afficher_details} et votre siege est {si._numero_siege} et le prix de billet est {self._prix}")
        

class Client():
    def __init__(self, nom, id_client, billets = []):
        self.nom = nom
        self.id_client = id_client
        self.billets = billets
    def acheter_billet(self,projection, numero_siege, prix):
            
