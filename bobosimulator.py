#Le bobo est un être vivant qui:
# a un age qui va de 0 a 100 ans. Il meurt à cent ans. Quand le bobo meurt, il genere 100 de bobo food.
# un bobo consomme 1 de bobo food par jour.
# un bobo genere 2.5 de bobo food par jour quand son age est entre 15 et 50 ans
# deux bobos entre 25 et 50 ans ont une chance de 0.25 par jour de se reproduire et de creer un nouveau bobo.
# n'importe quel bobo a une probilité de 0.1 de mourir chaque jour d'un accident malheureux.
# Le but est de coder le simulateur de la ville de Paris qui démarre avec 10 bobos (20a), 300 de bobo_food et donne les evénements
# , le nombre de bobos en vie et leur age chaque jour. Le nombre initial de bobos et de bobo food est paramétrable.

# Création du bobo

class Bobo:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        self.alive = alive
    pass

    def get_bobo_age(self):
        age = range(0,100)
        age = age =+ 1
    pass

    def bobo_die_old_age(self):
        if age > 100:
            alive is False
    pass

    def bobo_eats(self):



# Création de la bobo food

bobofood = 300

# Création du simulateur qui donne le résultat. Les paramètres sont le nombre initial et la bobo-food

def bobo_simulator(bobo_people,bobofood):