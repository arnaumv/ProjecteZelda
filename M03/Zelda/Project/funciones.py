from datetime import datetime
from menus import *
import random
import os




###############################  OPCIONES MENU INICIO ##############################

# Lista de funciones de menú disponibles
menus = [menu1, menu2, menu3]

def mostrar_menu_aleatorio():
    menu_aleatorio = random.choice(menus)
    menu_aleatorio()

def prompt_usuari():
    opcions_valides = ["continue", "new game", "help", "about", "exit"]
    accio = input("What to do now? ").lower()
    
    while accio not in opcions_valides:
        print("Invalid action")
        accio = input("What to do now? ").lower()

    # Realitzar accions segons l'opció escollida
    if accio == "continue":
        # Acció per a "Continue"
        pass
    elif accio == "new game":
        newGameMenu()
        pass
    elif accio == "help":

         # Acción para "Help"
        helpMainMenu()
        while True:  
            aboutInput = input("What to do now? ").lower()
            if aboutInput == 'back':
                mostrar_menu_aleatorio()
                prompt_usuari()
                break  
            else:
                print("Invalid action")
        
        
    elif accio == "about":
         # Acción para "About"
        aboutMenu()
        while True:  
            aboutInput = input("What to do now? ").lower()
            if aboutInput == 'back':
                
                mostrar_menu_aleatorio()
                prompt_usuari()
                break  
            else:
                print("Invalid action")
    elif accio == "exit":
        # Acció per a "Exit"
        pass


##################################################################################

