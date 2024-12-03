from Utilisateur import Utilisateur
from Serveur import Serveur
from Commande import Commandes

class ChefDeCuisine(Utilisateur):
    def afficher_info(self):
        pass            
    def consulter_commandes(self):
        print(f"les commandes en cours sont: ")
        for commande in Serveur.commandes:
            print(f"la commande {commande} est en cours")
    
    def mettre_a_jour_statut_commande(self, commande, statut):
        self.commande = commande
        self.statut = statut
        if commande in Serveur.commandes:
            Commandes.statut = statut
        else:
            print("la commandes n'existe pas")

c = ChefDeCuisine("achiko", 1, "ossama_argaz")
c.consulter_commandes()
