from datetime import datetime

class Produit:
    def __init__(self, reference, prix_achat, prix_vent,designation, stock = 0):
        
        self.reference = reference
        self.prix_achat = prix_achat
        self.prix_vent = prix_vent
        self.designation = designation
        self.stock = stock

    def quantité_en_stock(self):
        return self.stock
    def info_produit(self):
        return self.stock
    def modifier_prix_achat(self, nouveau_prix_achat):
         self.prix_achat = nouveau_prix_achat
    def modifier_prix_vents(self,nouveau_prix_vents):
         self.prix_vent = nouveau_prix_vents
    def nombre_exempliare_stock(self, nouveau_nombre_exemplaire):
         self.stock += nouveau_nombre_exemplaire


class Commandes():
     now = datetime.now()
     def __init__(self):
          self.products = []
          self.stock_quantité = []
     
     def ajouter_produit(self, product, stock):
        self.products.append(product)
        self.stock_quantité.append(stock)

     def ajouter_produit(self, product,):
        self.products.pop(product)
        self.stock_quantité.pop(product)



        
        