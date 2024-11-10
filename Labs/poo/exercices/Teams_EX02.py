class Compte:
    def __init__(self, Numero_compte, Solde):
        self.numero_compte = Numero_compte
        self.solde = Solde
    def deposer(self, montant):
        self.solde += int(montant)

    def retrait(self, montant):
        if solde > montant:
            self.solde -= int(montant)
        else:
            print("vous ne pouvez pas car votre sold ne dépasse pas le montant")
            print("---------------------------------------------------")
    def afficher_solde(self):
        print("votre solde est : " + str(self.solde))



class CheckingAccount(Compte):
    def __init__(self,numero_compte,solde, ft=0.02):
        super().__init__(numero_compte, solde)
        self.frais_transaction = ft

    def retrait(self, montant):
        ftrans = montant * self.frais_transaction
        if solde > montant:
            self.solde -= montant + ftrans
        else:
            print("vous ne pouvez pas car votre sold ne dépasse pas le montant")
            print("-----------------------------------------------------")
    
    def afficher_solde(self):
        print("votre solde avec les frais de transaction est : " + str(self.solde))
        print("-----------------------------------------------------")
    def __str__(self):
        return f"checkingAccount(numero_compte={self.numero_compte}, solde={self.solde})"


    
class SavingsAccount(Compte):
    def __init__(self,numero_compte, solde, taux_interet=4):
        super().__init__(numero_compte, solde)
        self.interet = int(taux_interet) / 100
    def appliquer_interet(self,solde):
        self.solde = solde
        self.solde = self.solde + (self.solde * self.interet)
        return self.solde
    def afficher_solde(self):
        print("votre solde avec les interet est : " + str(self.solde))
    def __str__(self):
        return f"SavingsAccount(numero_compte={self.numero_compte}, solde={self.solde})"

class Client:
    def __init__(self, Client_id, Nom, Comptes = []):
        self.client_id = Client_id
        self.nom = Nom
        self.comptes = Comptes
    def ouvrir_compte(self,type_compte):
        self.type_compte = type_compte
        if type_compte == "checking":
            compte = CheckingAccount(Numero_compte,Solde)
        elif type_compte == "savings":
            compte = SavingsAccount(Numero_compte,Solde)
        else:
            print("type de compte non valide")
            return None
        self.comptes.append(compte)
        print(f"Compte {type_compte}")
        return compte

    def fermer_compte(self,type_compte):
        type = CheckingAccount if type_compte == "checking" else SavingsAccount
        for self.compte in self.comptes:
            if isinstance(compte, type):
                self.comptes.remove(compte)
        print(f"Compte {type_compte} fermé avec succès")


    def afficher_comptes(self):
        for self.compte in self.comptes:
            compte.afficher_solde()





class Banque():
    def __init__(self,clients = []):
        self.clients = clients

    def ajouter_client(self,client):
        self.clients.append(client)
        print(f"Client {client.nom} ajouté.")

    def supprimer_client(self,client,client_id):
        for self.client in self.clients:
            if self.client.client_id == client_id:
                self.clients.remove(client)
        print(f"Client {client.nom} supprimé.")


    def transferer_fonds(self,compte_emetteur, compte_destination, montant):
        if  compte_emetteur.solde > montant:
            compte_emetteur.retrait(montant)
            compte_destination.deposer(montant)
            print("transfer effectué")
        else:
            print("Solde insuffisant pour effectuer la transfer")








compte = Compte(12, 18000)
Numero_compte = compte.numero_compte
solde = compte.solde
montant = int(input("enter montant"))
compte.deposer(montant)
compte.afficher_solde()

checkingAccount = CheckingAccount(Numero_compte, solde)
print("---------------------- cheking account ------------------------------")
checkingAccount.retrait(montant)
checkingAccount.afficher_solde()


taux_interet = int(input("enter taux interet"))
savingsAccount = SavingsAccount(Numero_compte, solde, taux_interet)
print("---------------------- saving account ------------------------------")
savingsAccount.appliquer_interet(solde)
savingsAccount.afficher_solde()

print("------------------------------------------------")



client = Client(1,"ossama")

Numero_compte = input("enter numero de compte")
Solde = input("enter solde de compte")
type_compte = input("enter type de compte a ouvrir: ")

compte1 = client.ouvrir_compte(type_compte)
compte2 = client.ouvrir_compte(type_compte)

client.afficher_comptes()

# type_compte = input("enter type de compte a fermer: ")
# client.fermer_compte(type_compte)


banque = Banque()

banque.ajouter_client(client)


banque.transferer_fonds(compte1, compte2, 300)