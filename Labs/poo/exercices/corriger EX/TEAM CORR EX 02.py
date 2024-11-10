class Compte:
    def __init__(self, nc, solde):
        self.numero_compte = nc
        self._solde = solde

    def deposer(self, montant):
        self._solde += montant

    def retrait(self, montant):
        self._solde -= montant

    def afficher_solde(self):
        print(f"Compte {self.numero_compte} solde: {self._solde}")
        return self._solde

class CheckingAccount(Compte):
    def __init__(self, nc, solde=0, ft=0.02):
        super().__init__(nc,solde)
        self.frais_transaction = ft

    def retrait(self, montant):
        total = montant + (montant * self.frais_transaction)
        if total <= self._solde:
            self._solde -= total
            print(f"{montant} retiré du compte cheque {self.numero_compte} avec frais. Nouveau solde: {self._solde}")
        else:
            print("Solde Insuffisant pour cette opération.")

class SavingsAccount(Compte):
    def __init__(self, nc, solde=0, ti=0.04):
        super().__init__(nc,solde)
        self.taux_interet = ti

    def appliquer_interet(self):
        self._solde += (self._solde * self.taux_interet)
        print(f"Intérét appliqué au compte Epargne {self.numero_compte}. Nouveau solde: {self._solde}")

class Client:
    def __init__(self, id, nom):
        self.client_id = id
        self.nom = nom
        self.comptes = []

    def ouvrir_compte(self, type_compte, numero_compte):
        if type_compte == "checking":
            compte = CheckingAccount(numero_compte)
        elif type_compte == "savings":
            compte = SavingsAccount(numero_compte)
        else:
            print("Type de compte invalide.")
            return None

        self.comptes.append(compte)
        print(f"Compte {type_compte} ouvert avec succès")
        return compte

    def fermer_compte(self, type_compte):
        type = CheckingAccount if type_compte == "checking" else SavingsAccount
        for compte in self.comptes:
            if isinstance(compte, type):
                self.comptes.remove(compte)
        print(f"Compte {type_compte} fermé avec succès")

    def afficher_comptes(self):
        print(f"Comptes de {self.nom}:")
        for compte in self.comptes:
            compte.afficher_solde()

class Banque:
    def __init__(self):
        self.clients = []

    def ajouter_client(self, client):
        self.clients.append(client)
        print(f"Client {client.nom} ajouté.")

    def supprimer_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                print(f"Client {client.nom} supprimé.")

    def transferer_fonds(self, compte_emetteur, compte_destination, montant):
        if compte_emetteur._solde > montant:
            compte_emetteur.retrait(montant)
            compte_destination.deposer(montant)
            print(f"Transfer de {montant} du compte {compte_emetteur.numero_compte} au compte {compte_destination.numero_compte}.")
        else:
            print("Solde Insuffisant pour le transfer.")

# Create bank
bank = Banque()

# Create clients
client1 = Client(1, "Alice")
client2 = Client(2, "Bob")

bank.ajouter_client(client1)
bank.ajouter_client(client2)

account1 = client1.ouvrir_compte("checking", 101)
account2 = client1.ouvrir_compte("savings", 102)

account3 = client2.ouvrir_compte("savings", 201)

account1.deposer(1000)
account2.deposer(500)
account3.deposer(300)

account2.appliquer_interet()

account1.retrait(100)

bank.transferer_fonds(account2, account3, 100)

client1.afficher_comptes()
client2.afficher_comptes()
