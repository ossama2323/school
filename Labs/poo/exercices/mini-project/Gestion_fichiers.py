class Gestion_fichier():
    def lire_fichier(self, nom_fichier):
        self.nom_fichier = nom_fichier
        fichier = open(self.nom_fichier, "r", encoding="utf-8")
        contenu = fichier.read()
        return contenu
    def ecrire_fichier(self, nom_fichier, contenu):
        self.nom_fichier = nom_fichier
        self.contenu = contenu
        fichier = open(self.nom_fichier, "a", encoding="utf-8")
        fichier.write(self.contenu)
        fichier = open(self.nom_fichier, "r", encoding="utf-8")
        contenu = fichier.read()
