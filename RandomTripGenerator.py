from http.client import responses
from msilib import sequence
from multiprocessing.connection import answer_challenge
from pickle import FALSE
import random
from secrets import choice
from tkinter.messagebox import YES
from urllib import response



food_spots = ['Harney Sushi', 'Fog Harbour', 'Boudin Bakery', 'Poke One n Half']
location_spots = ['San Francisco', 'San Diego', 'Los Angeles', 'Portland']
transportation_sucks = ['Motorcyle','Car', 'Train', 'Airplane']
entertainment_fun = ['A Comedy Show', 'A Movie', 'Playing Mario Party', 'Visiting Family']


typed_response = input

def display_food_options():
    
    random_choice = choice(seq=food_spots)
    print(random_choice)
    response = input("Yes or no? ")   
    if response == "no":
        print('lets try again')
        return choice(seq=food_spots)
    else: 
        response == "yes"
        print(f'Awesome lets go eat, {random_choice}')
       
def continue_on():
    if typed_response == "no":
        print('Lets try again')
        return 



def display_transportation_options():
    
    random_choice = choice(seq=transportation_sucks)
    print(random_choice)
    response = input("Yes or no? ")   
    if response == "no":
        print('lets try again') 
        return random_choice
    else: 
        response == "yes"
        print(f'Awesome lets go by, {random_choice}')
       
        
def display_location_options():
    
    random_choice = choice(seq=location_spots)
    print(random_choice)
    response = input("Yes or no? ")   
    if response == "no":
        print('lets try again') 
        return random_choice
    else: 
        response == "yes"
        print(f'Awesome lets go to, {random_choice}')
       
        
def display_entertainment_options():
    
    random_choice = choice(seq=entertainment_fun)
    print(random_choice)
    response = input("Yes or no? ")   
    if response == "no":
        print('lets try again') 
        return random_choice
    else: 
        response == "yes"
        print(f'Awesome lets try, {random_choice}')
       
# def decided_confirmed()
# for choice in 


continue_on()
display_food_options()
display_entertainment_options()
display_location_options()
display_transportation_options()

def display_completed_trip():
    print(f"You are going to {food_spots} in {location_spots} by {transportation_sucks}. Also, you will get to enjoy {entertainment_fun})!!")


display_completed_trip()


