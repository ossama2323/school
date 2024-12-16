# il y a 3 methode d'utilisé get and set 

# methode 1 to use get and set 
# class get_set:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.__age = age #privat Attribute
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age):
#         self.__age = age
    
# g = get_set("ossama", 18)


# print(g.get_age())
# g.set_age(32)
# print(g.get_age())
# print(g.nom)




# methode 2 to use get and set  avec propertie
# class get_set:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.__age = age #privat Attribute
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         self.__age = age
#     def delete_age(self):
#         del self.__age

#     age = property(get_age,set_age,delete_age,"age de perssone")

# g = get_set("ossama", 18)


# g.age = 22 # set just en utilisant le mot cle age de property
# print(g.age) # get methode and the output 22
# # print(g.__age) #AttributeError: 'get_set' object has no attribute '__age
# # del g.age # delete methode
# print(g.age)



# methode 3 to use get and set avec propertie decorateur

# class get_set:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.__age = age #privat Attribute
#     @property
#     def Age(self):
#         return self.__age
#     @Age.setter
#     def Age(self, age):
#         self.__age = age
#     @Age.deleter
#     def Age(self):
#         del self.__age

# g = get_set("ossama", 18)

# print(g.Age)

# g.Age = 22

# print(g.Age) # output 22

# del g.Age

# # print(g.Age) si on le décommenté va nous donne error car Age a été supprimer
