class Repas:
    def __init__(self, nom, cout):
        self._nom = nom
        self._cout = cout
    def preparer(self):
        print("Preparation de repas")
    def calculer_prix(self):
        return self._cout

class Entree(Repas):
    def __init__(self, _nom, _cout, taille_portion):
        super().__init__(_nom , _cout)
        self._taille_portion = taille_portion
    def preparer(self):
        print(f"preparation de l'imperitif: {self._nom}, taille de la portion: {self._taille_portion}")
    def calculer_prix(self):
        if self._taille_portion == "Grandes":
            print(self._cout + self._cout * 0.05)
        else:
            print(self._cout)

class Plat_Principal(Repas):
    def __init__(self, _nom, _cout, cuisine_type):
        super().__init__(_nom, _cout)
        self._cuisine_type = cuisine_type
    def preparer(self):
        print(f"cuisson du plat principal: {self._nom} dans le style {self._cuisine_type}")
    def calculer_prix(self):
        if self._cuisine_type == "international":
             print(self._cout + self._cout * 0.1)
        else:
            print(self._cout)

class Dessert(Repas):
    def __init__(self,_nom, _cout, sans_sucre):
        super().__init__(_nom, _cout)
        self._sans_sucre = sans_sucre
    def preparer(self):
        sans_sucre = self._sans_sucre == "sans sucre"
        dessert_sans = f"Preparation de dessert {self._nom}, sans sucre"
        dessert_avec = f"Preaparation de dessert {self._nom}, avec sucre"
        print (dessert_sans if sans_sucre else dessert_avec)
    def calculer_prix(self):
        print(self._cout - self._cout * 0.1)
        






nom = input("entrer nom de Repas: ")
cout = float(input("entrer cout de repas: "))
R = Repas(nom, cout)

taille_portion = input("entrer la taille de portion: ")
E = Entree(nom, cout, taille_portion)

cuisine_type = input("entrer le type de la cuisine: ")
P = Plat_Principal(nom, cout, cuisine_type)

dessert = input("entrer le nom de dessert")
sans_sucre = input("entrer si vous voulez avec sucre: ")
D = Dessert(dessert, cout, sans_sucre)

list_object = [R, E, P, D]



for repas in list_object:
    repas.preparer()
    print("--------------------------------------------------------")
    repas.calculer_prix()
    print("--------------------------------------------------------")
