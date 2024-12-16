# STATIQUES METHODES


def exterieur():     #statique methode en dehore de la classe
     print("statique methode a l'exterieur")


class perssone:
    @staticmethod    #statique methode en dedant ou a l'interieur d'une classe 
    def interieur():
        print("statique methode a l'interieur")




perssone.exterieur = staticmethod(exterieur)    #statique methode en dehore de la classe


perssone.exterieur()  #appel de la methode statique qui est al'exterieur 

perssone.interieur()  #appel de la methode statique qui est al'interieur 