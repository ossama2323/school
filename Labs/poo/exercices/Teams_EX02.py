class Compte:
    def __init__(self, Numero_compte, Solde):
        self.numero_compte = Numero_compte
        self.solde = Solde
    def deposer(self, montant):
        self.solde += int(montant)
    def retrait(self, montant):
        self.solde -= int(montant)
    def afficher_solde(self):
        print("votre solde est : " + str(self.solde))



class CheckingAccount(Compte):
    def __init__(self,numero_compte,solde, montant):
        super().__init__(numero_compte, solde, montant)
        self.frais_transaction = montant * 0.02
    def retrait(self,solde, montant):
        self.solde = solde
        self.solde -= montant + self.frais_transaction
        return super().retrait(montant)
    def afficher_solde(self):
        print("votre solde avec les frais de transaction est : " + str(self.solde))

    
class SavingsAccount(Compte):
    def __init__(self,numero_compte, solde, montant, taux_interet):
        super().__init__(numero_compte, solde, montant)
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
        if type_compte == "compte courant":
            self.comptes.append(CheckingAccount(Numero_compte,solde,montant))
        elif type_compte == "compte d'épargne":
            self.comptes.append(SavingsAccount(Numero_compte,solde,montant,taux_interet))
        else:
            print("type de compte non valide")
    def fermer_compte(self,type_compte):
        self.type_compte = type_compte
        if type_compte == "compte courant":
            self.comptes.pop()
        elif type_compte == "compte d'épargne":
            self.comptes.pop()
        else:
            print("type de compte non valide")
    






compte = Compte(12, 18000)
Numero_compte = compte.numero_compte
solde = compte.solde
montant = int(input("enter montant"))
compte.retrait(montant)
compte.afficher_solde()

checkingAccount = CheckingAccount(Numero_compte, solde, montant)
checkingAccount.retrait(solde, montant)
checkingAccount.afficher_solde()


taux_interet = int(input("enter taux interet"))
savingsAccount = SavingsAccount(Numero_compte, solde, montant, taux_interet)
savingsAccount.appliquer_interet(solde)
savingsAccount.afficher_solde()



