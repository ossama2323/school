class Reservation():
    def __init__(self, id_reservation, nom_client, nombre_perssones, date, heure, table):
        self._id_reservation = id_reservation
        self._nom_client = nom_client
        self._nombre_perssones = nombre_perssones
        self._date = date
        self._heure = heure
        self._table = table

    def afficher_reservation(self):
        print(f"Reservation de L'id {self._id_reservation}, par {self._nom_client}, a {self._date}, a l'heure {self._heure}, nombre de perssone {self._nombre_perssones}, au table {self._table}")

    def __str__(self):
        return f"Reservation de L'id {self._id_reservation}, par {self._nom_client}, a {self._date}, a l'heure {self._heure}, nombre de perssone {self._nombre_perssones}, au table {self._table}"
    