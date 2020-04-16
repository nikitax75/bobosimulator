# Le bobo est un être vivant qui:
# a un age qui va de 0 a 100 ans. Il meurt à cent ans. Quand le bobo meurt, il genere 100 de bobo food.
# un bobo consomme 1 de bobo food par jour.
# un bobo genere 2.5 de bobo food par jour quand son age est entre 15 et 50 ans
# deux bobos entre 25 et 50 ans ont une chance de 0.25 par jour de se reproduire et de creer un nouveau bobo.
# n'importe quel bobo a une probilité de 0.1 de mourir chaque jour d'un accident malheureux.
# Le but est de coder le simulateur de la ville de Paris qui démarre avec 10 bobos (20a)
# , 300 de bobo_food et donne les evénements
# , le nombre de bobos en vie et leur age chaque jour. Le nombre initial de bobos et de bobo food est paramétrable.

# import des modules nécessaires

import random

# Création de la bobofood

bobofood = 300

# Création du bobo


class Bobo:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        self.alive = alive

    def get_bobo_age(self):
        return self.age

    def bobo_eats(self):
        if bobofood > 0:
            bobofood -= 1

    def bobo_generates_food(self):
        if self.age > 15 < 50:
            bobofood += 2.5
        else:
            pass

# liste des morts possibles:

    def bobo_dies_old_age(self):
        if age == 100:
            alive is False
            bobofood += 100

    def bobo_dies_starving(self):
        if bobofood < 1:
            alive is False

    def bobo_dies_sad_accident(self):
        sad_accident = random.choice(range(101))
        print(sad_accident)

bobo1 = Bobo("Nick", 20, True)
bobo2 = Bobo("Toto", 20, True)
bobo3 = Bobo("NV", 20, True)
bobo4 = Bobo("Vivouz", 20, True)
bobo5 = Bobo("Juju", 20, True)
bobo6 = Bobo("Titi", 20, True)

# Création du simulateur qui donne le résultat. Les paramètres sont le nombre initial et la bobo-food

# def bobo_simulator(bobo_people,bobofood):