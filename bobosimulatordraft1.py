#Le bobo est un être vivant qui:
# a un age qui va de 0 a 100 ans. Il meurt à cent ans. Quand le bobo meurt, il genere 100 de bobo food.
# un bobo consomme 1 de bobo food par jour.
# un bobo genere 2.5 de bobo food par jour quand son age est entre 15 et 50 ans
# deux bobos entre 25 et 50 ans ont une chance de 0.25 par jour de se reproduire et de creer un nouveau bobo.
# n'importe quel bobo a une probilité de 0.1 de mourir chaque jour d'un accident malheureux.
# Le but est de coder le simulateur de la ville de Paris qui démarre avec 10 bobos (20a), 300 de bobo_food et donne les evénements
# , le nombre de bobos en vie et leur age chaque jour. Le nombre initial de bobos et de bobo food est paramétrable.
# Le bobo est un être vivant qui:y
# a un age qui va de 0 a 100 ans. Il meurt à cent ans. Quand le bobo meurt, il genere 100 de bobo food.y
# un bobo consomme 1 de bobo food par jour.y
# un bobo genere 2.5 de bobo food par jour quand son age est entre 15 et 50 ansy
# deux bobos entre 25 et 50 ans ont une chance de 0.25 par jour de se reproduire et de creer un nouveau bobo.n
# n'importe quel bobo a une probilité de 0.1 de mourir chaque jour d'un accident malheureux.y
# Le but est de coder le simulateur de la ville de Paris qui démarre avec 10 bobos (20a)n
# , 300 de bobo_food et donne les evénementsn
# , le nombre de bobos en vie et leur age chaque jour. Le nombre initial de bobos et de bobo food est paramétrable.n

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

    def bobo_birth(self):
        bobos_list.append(self)

    def get_bobo_age(self):
        age = range(0,100)
        age = age =+ 1

    # un bobo consomme 1 de bobo food par jour.
    def bobo_eats(self):
        if bobofood > 0:

            bobofood -= 1
    # un bobo genere 2.5 de bobo food par jour quand son age est entre 15 et 50 ans
    def bobo_generates_food(self):
        if self.age >= 15 <= 50:
            bobofood += 2.5
        else:

# liste des morts possibles:

    # a un age qui va de 0 a 100 ans. Il meurt à cent ans. Quand le bobo meurt, il genere 100 de bobo food.
    def bobo_dies_old_age(self):
        if age == 100:
            alive is False

    def bobo_dies_starving(self):
        if bobofood < 1:
            alive is False

            self.alive = False
            bobofood += 100

    def bobo_dies_starving(self):
        if bobofood < 1:
            self.alive = False

    # n'importe quel bobo a une probilité de 0.1 de mourir chaque jour d'un accident malheureux.
    def bobo_dies_sad_accident(self):
        random.choice
        sad_accident = random.randint(0,100) < 10
        if sad_accident is True:
            print("bobo died from a sad accident!")
        else:
            pass

    # reproduction des bobos

    # def bobos_reproduction(self):

# Création de la populaaaace (liste des bobos):

bobos_list = []

# Création du temps

day = 0

# Création du simulateur qui donne le résultat. Les paramètres sont le nombre initial et la bobo-food

# def bobo_simulator(bobo_people,bobofood)

def bobo_simulator(bobo_people, bobofood):
    while day <= 361:
        day +=1
        



if __name__ == "bobo_simulator":
    bobo_simulator()