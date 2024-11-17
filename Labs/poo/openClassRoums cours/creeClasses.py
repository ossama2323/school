class boiteAOutils:
    def __init__(self, outils):
        self.outils = outils
    def ajouter_outils():
        pass
    def supprimer_outil():
        pass

class marteau:
    def __init__(self, couleur= "rouge"):
        self.couleur = couleur
    def planter(self):
        pass
    def retirer(self):
        pass
    def changer(self):
        pass

class tourneuvis:
    def __init__(self, taille):
        self.taille = taille
    def serrer(self):
        pass 
    def deserre(self):
        pass


#Instanciez des objet

outile1 = boiteAOutils("crique")
outile1.ajouter_outils
outile1.supprimer_outil

marteau1 = marteau("bleu")
marteau1.planter()
marteau1.changer()
marteau1.retirer()


tourneuvis1 = tourneuvis(19)
tourneuvis1.serrer()
tourneuvis1.serrer()