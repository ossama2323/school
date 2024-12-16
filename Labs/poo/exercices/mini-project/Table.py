class Table():
    def __init__(self, numero_table, capacite):
        self._numero_table = numero_table
        self._capacite = capacite
        self._est_occupe = "libre"
        
    def afficher_info_table(self):
        print(f"La table numero {self._numero_table}, la capacite de la table est {self._capacite}")
    
    def occuper_table(self):
        if self._est_occupe == "libre":
            self._est_occupe = "occupe"
        else:
            print(f"la table {self._numero_table} est deja occupe")
    def liberer_table(self):
        if self._est_occupe == "occupe":
            self._est_occupe = "libre"
        else:
            print(f"la table {self._numero_table} est deja libre")