from msilib import sequence
from pickle import FALSE
import random
from secrets import choice



food_spots = ['Harney Sushi', 'Fog Harbour', 'Budin Bakery', 'Poke One n Half']
location_spots = ['San Francisco', 'San Diego', 'Los Angeles', 'Portland']
transportation_sucks = ['Motorcyle','Car', 'Train', 'Airplane']
entertainment_fun = ['Comedy Show', 'Movies', 'Play Mario Party', 'Visit Family']




def display_food_options():
    
    random_choice = choice(seq=food_spots)
    print(random_choice)
    response = input("Yes or no? ")   
    if response == "no":
        print('lets try again') 
        return random_choice
    else: 
        response == "yes"
        print(f'Awesome lets go eat, {random_choice}')
       
        

        

display_food_options()