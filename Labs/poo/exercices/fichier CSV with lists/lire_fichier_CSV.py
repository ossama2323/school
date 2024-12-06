import csv
fichier = open("data_list.csv", "r", encoding="utf-8")

fichier_reader = csv.reader(fichier, delimiter=";")

for row in fichier_reader:
    print(row)