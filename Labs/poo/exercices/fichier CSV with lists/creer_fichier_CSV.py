import csv

data = [["Name", "Age", "Country"],
    ["John", 25, "USA"],
    ["Anna", 32, "UK"],
    ["Peter", 45, "Australia"]]

fichier = open("data_list.csv", "w", encoding="utf-8")

fichier_writer = csv.writer(fichier, delimiter=";")

for ligne in data:
    fichier_writer.writerow(ligne)
    
fichier_writer.writerow(["ici on a creer un fichier CSV et on le donne ou on l'écrit une list avec la methode <w>"])