fichier = open("test_fichier.txt", "a", encoding="utf-8")

fichier.write("\n c'est le text ajouter a la fin de fichier avec la methode <a>")


fichier = open("test_fichier.txt", "r", encoding="utf-8")
print(fichier.read())