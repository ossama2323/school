class Menu():
    def __init__(self, id_article, nom, prix, description = None, categorie = None):
        self._id_article = id_article
        self._nom = nom
        self._description = description
        self._prix = prix
        self._categorie = categorie
    def afficher_article(self):
        print(f"l'article {self._nom}, de l'id {self._id_article}, description {self._description}, Prix {self._prix}, categorie {self._categorie}")

    def __str__(self):
        return f"l'article {self._nom}, de l'id {self._id_article}, description {self._description}, Prix {self._prix}, categorie {self._categorie}"