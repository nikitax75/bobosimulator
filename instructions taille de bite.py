# ma_liste_de_bobos = [age_bobo1, age_bobo2]
#
# simulate_mort_bobo(age_bobo, probabilite_mort_bob, age_max_mort)
​
#LES DEFINITIONS
def augmentation_de_taille_de_bite(taille_de_ma_bite):
    return taille_de_ma_bite + 17
​
#Ceci est un exemple de programmation orientée objet absolument incroyable
class Bobo:
    def __init__(self, name, age):
        #Stocke les parametres de creation dans l'objet bobo
        self.name = name
        self.age = age
​
        #Initialise le bobo comme etant vivant dès le depart
        self.vivant = True
​
    def rendre_plus_vieux(self):
        self.age = self.age + 1
​
    def donne_moi_lage_plus_50_de_ce_connard(self):
        return self.age / 0
​
# LES EXECUTIONS
augmentation_de_taille_de_bite(54)
​
bobo_du_coin = Bobo("LE BOBO DU COIN", 23)
bobo_de_mareil_le_guyon = Bobo("LE BOBO DE MAREIL", 26)
​
​
#Ces deux lignes font la meme chose
age_du_bobo_du_coin = bobo_du_coin.age
age_du_bobo_du_coin = bobo_du_coin.donne_moi_lage_plus_50_de_ce_connard()
​
​
print("Age du bobo du coin: " + str(bobo_du_coin.age))
Réduire