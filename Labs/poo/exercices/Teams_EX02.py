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

class Client:
    def __init__(self, Client_id, Nom, Comptes = []):
        self.client_id = Client_id
        self.nom = Nom
        self.comptes = Comptes
    def ouvrir_compte(self,type_compte):
        self.type_compte = type_compte
        for type_compte in self.comptes:
            if type_compte == "checking":
                self.comptes.append(CheckingAccount(numero_compte, Solde))
            elif type_compte == "savings":
                self.comptes.append(SavingsAccount(Numero_compte,Solde))
            else:
                print("type de compte non valide")

    def fermer_compte(self,type_compte):
        self.type_compte = type_compte
        if type_compte == "courant":
            self.comptes.pop()
        elif type_compte == "d'épargne":
            self.comptes.pop()
        else:
            print("type de compte non valide")

    def afficher_comptes(self):
            print(self.comptes)



compte = Compte(12, 18000)
Numero_compte = compte.numero_compte
solde = compte.solde
montant = int(input("enter montant"))
compte.retrait(montant)
compte.afficher_solde()

checkingAccount = CheckingAccount(Numero_compte, solde)
checkingAccount.retrait(montant)
checkingAccount.afficher_solde()


taux_interet = int(input("enter taux interet"))
savingsAccount = SavingsAccount(Numero_compte, solde, taux_interet)
savingsAccount.appliquer_interet(solde)
savingsAccount.afficher_solde()



client = Client(12,"ossama")
numero_compte = input("enter numero de compte")
Solde = input("enter numero de compte")
type_compte = input("enter type de compte a ouvrir: ")
client.ouvrir_compte(type_compte)
client.afficher_comptes()