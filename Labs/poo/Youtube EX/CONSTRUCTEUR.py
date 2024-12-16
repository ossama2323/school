# il y a 3 type de constructeur

# mais en python la classe prend seulement une constructeur
class perssone:
 
    # 1. constructeur par defaut ou constructeur sans parametre 
    # def __init__(self):
    #     self.nom = "ossama"
    
    # une method pour printing data members
    # def print_nom(self):
    #     print(self.nom)
    
    # 2. constructeur parametrer ou constructeur avec des parametre
    def __init__(self, name=None, age= None):
        self.name = name
        self.age = age

    # 3. constructeur de recopie
    def copy(self, perssone_copy): # on remplace init par copy car la class peut contient seulement une constructeur
        self.name = perssone_copy.name
        self.age = perssone_copy.age


 
 
# instanciation d'objet pour tester le constructeur par defaut
# perssone_1 = perssone()
# perssone_1.print_nom()



# instanciation d'objet pour tester le constructeur parametrer
perssone_1 = perssone("ossama", 19)
print(perssone_1.name)



# instanciation d'objet pour tester le constructeur de recopie , il recopie le perssone 1 dans le perssone 2
perssone_2 = perssone()
perssone_2.copy(perssone_1)
print(perssone_2.name, perssone_2.age)
