class Etudiante:
    def __init__(self, Nom, Age, Note):
        self.__Nom = Nom
        self.Age = Age
        self.Note = Note


    # get methode
    def getNom(self):
        return self.__Nom
    
    # set methode
    def setNom(self,Nom):
        self.__Nom = Nom


# objects
etd1 = Etudiante("ahmed", 18, 14) 
print(etd1.getNom())

etd1.setNom("achiko")
print(etd1.getNom())
