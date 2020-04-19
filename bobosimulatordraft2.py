# importing required modules

import random

# coding initial bobo population

bobos_list = ["bobo1" + "bobo2" + "bobo3" + "bobo4"]

# coding time (example for 3 years here)

simulate_nb_of_years = 3
day = 1
year = 360*day
while day <= year*simulate_nb_of_years:
    day += 1
    print(bobos_list)
