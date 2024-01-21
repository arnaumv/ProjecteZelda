from datetime import datetime
from menus import *
import random
import pandas as pd
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder


# PROMPT #

prompt = []

def promptAfegir(text):
    global prompt
    prompt.append(text)
    if len(prompt) >= 4:
        prompt.pop(0)


def promptDibuixar():
    global prompt
    for cnt  in range(0, len(prompt)):
        print(prompt[cnt])

###############################  OPCIONES MENU INICIO ##############################

# Lista de funciones de menú disponibles

menus = [gameMenu, gameMenu2, gameMenu3]

menus2 = [menu1, menu2, menu3]

def mostrar_menu_aleatorio():
    clear_terminal()
    menu_aleatorio = random.choice(menus)
    menu_aleatorio()
def mostrar_menu_aleatorio2():
    clear_terminal()
    menu_aleatorio = random.choice(menus2)
    menu_aleatorio()

def prompt_game1():
    opcions_valides = ["new game", "help", "about", "exit", "reports"]
    accio = input("What to do now? ").lower()
    
    while accio not in opcions_valides:
        print("Invalid action")
        accio = input("What to do now? ").lower()

    if accio == "new game":
        newGameMenu()
        pass
    elif accio == "help":

         # Acción para "Help"
        helpMainMenu()
        while True:  
            aboutInput = input("What to do now? ").lower()
            if aboutInput == 'back':
                mostrar_menu_aleatorio()
                prompt_game1()
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
                prompt_game1()
                break  
            else:
                print("Invalid action")

    elif accio == "reports":
        reportsGamesMenu()
        pass

    elif accio == "exit":
        # Acció per a "Exit"
        pass


# Este será el menú principal del juego si hay algun jugador registrado

def prompt_game2():
    opcions_valides = ["continue", "new game", "help", "about", "exit", "reports"]
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
                prompt_game1()
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
                prompt_game1()
                break  
            else:
                print("Invalid action")


    elif accio == "reports":
        reportsGamesMenu()
        pass
    elif accio == "exit":
        # Acció per a "Exit"
        pass

##################################################################################

##########################      INFO PLAYER        #########################
    

    

player = {
    "default": {
       "inventory": {
        "lives": 3,
        "max_lives": 3,
        "timeBlood": 25,
        "weapon1": "Wood Sword",
        "weapon2": "Wood Shield",
        "totalFood": 0,
        "totalWeapons": 2,
        "chests_opened": 0,  # Add this line
      },
        "weapons": {
            "wood sword": {"uses": 5, "count": 2, "equipped": True},
            "sword": {"uses": 9, "count": 1, "equipped": False},
            "wood shield": {"uses": 5, "count": 1, "equipped": True},
            "shield": {"uses": 9, "count": 0, "equipped": False}
        },
        "food": {
            "vegetables": {"count":5, "hearts":1},
            "fish": {"count": 2, "hearts":0},
            "meat": {"count": 2, "hearts":0},
            "salads": {"count": 2, "hearts":2},
            "pescatarian": {"count": 1, "hearts":3},
            "roasted": {"count": 1, "hearts":4}
        },
        "sanctuaries": {
            "S0": {"name": "S0?" , "opened": False} ,
            "S1":  {"name": "S1?" , "opened": False} ,
            "S2":  {"name": "S2?" , "opened": False} ,
            "S3":  {"name": "S3?" , "opened": False} ,
            "S4":  {"name": "S4?" , "opened": False} ,
            "S5":  {"name": "S5?" , "opened": False} ,
            "S6":  {"name": "S6?" , "opened": False} ,
        },
    }
}






########################################### INVENTARI #####################################################



########################################### INVENTARI MAIN #####################################################

jugadores = player.keys()          
ultimo_jugador = list(jugadores)[-1]    #Coje el ultimo jugador añadido en el diccionario 
playerInfo = {
    "inventory": player[ultimo_jugador]["inventory"]
}


santuarios = {
    "sanctuaries": player[ultimo_jugador]["sanctuaries"]   #Coje el valor que hay dentro de "sanctuaries"
}

inventoryM = [
    f" * * * * Inventory *",
    f"                   *",
    f" {player_name}         ♥ {playerInfo['inventory']['lives']}/{playerInfo['inventory']['max_lives']}*",
    f"  Blood moon in {playerInfo['inventory']['timeBlood']} *",
    f"                   *",
    f" Equipment         *",
    f"       {playerInfo['inventory']['weapon1']}  *",
    f"       {playerInfo['inventory']['weapon2']} *",
    f" Food            {playerInfo['inventory']['totalFood']} *",
    f" Weapons         {playerInfo['inventory']['totalWeapons']} *",
    f"                   *"
]
def inventoryMain(inventoryM):
    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios['sanctuaries']['S0']['name']).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios['sanctuaries']['S2']['name']).rjust(3)}                     *",
        f"*        {str(santuarios['sanctuaries']['S1']['name']).rjust(3)}                                    {str(santuarios['sanctuaries']['S3']['name']).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios['sanctuaries']['S4']['name']).rjust(3)}                                 {str(santuarios['sanctuaries']['S5']['name']).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios['sanctuaries']['S6']['name']).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

   

    for i in range(len(map)):
        print(map[i], inventoryM[i])





########################################### INVENTARI FOODS #####################################################


foods = {
    "food": player[ultimo_jugador]["food"]
}
# Acceder a los valores de "count" para cada comida
vegetables_count = foods['food']['vegetables']['count']
fish_count = foods['food']['fish']['count']
meat_count = foods['food']['meat']['count']
salads_count = foods['food']['salads']['count']
pescatarian_count = foods['food']['pescatarian']['count']
roasted_count = foods['food']['roasted']['count']
# Incorporar estos valores en tu inventario
inventoryFood = [
        f"* * * * * Foods *",
        f"                  *",
        f"                  *",
        f"Vegetables      {str(vegetables_count).rjust(1)} *",
        f"Fish            {str(fish_count).rjust(1)} *",
        f"Meat            {str(meat_count).rjust(1)} *",
        f"                  *",
        f"Salads          {str(salads_count).rjust(1)} *",
        f"Pescatarian     {str(pescatarian_count).rjust(1)} *",
        f"Roasted         {str(roasted_count).rjust(1)} *",
        f"                  *",
        f"* * * * * * * * * *"
    ]

def inventoryFoods(inventoryFood):
    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios['sanctuaries']['S0']['name']).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios['sanctuaries']['S2']['name']).rjust(3)}                     *",
        f"*        {str(santuarios['sanctuaries']['S1']['name']).rjust(3)}                                    {str(santuarios['sanctuaries']['S3']['name']).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios['sanctuaries']['S4']['name']).rjust(3)}                                 {str(santuarios['sanctuaries']['S5']['name']).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios['sanctuaries']['S6']['name']).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

 

   

    for i in range(len(map)):
        print(map[i], inventoryFood[i])


########################################### INVENTARI WEAPONS #####################################################





jugadores = player.keys()
ultimo_jugador = list(jugadores)[-1]

# Acceder a la información de armas del último jugador
weapons_info = player[ultimo_jugador]['weapons']

# Acceder a los detalles de las armas del último jugador
uses = {weapon: weapons_info[weapon]['uses'] for weapon in weapons_info}
count = {weapon: weapons_info[weapon]['count'] for weapon in weapons_info}
equipped = {weapon: weapons_info[weapon]['equipped'] for weapon in weapons_info}

inventoryWeap = [
            f"* * * * * Weapons *",
            f"                  *",
            f"                  *",
            f"Wood Sword    {uses['wood sword']}/{count['wood sword']} *",
            f"  {'(equipped)' if equipped['wood sword'] else ''}      *",
            f"Sword         {uses['sword']}/{count['sword']} *",
            f"  {'(equipped)' if equipped['sword'] else ''}                *",
            f"Wood Shield   {uses['wood shield']}/{count['wood shield']} *",
            f"  {'(equipped)' if equipped['wood shield'] else ''}      *",
            f"Shield        {uses['shield']}/{count['shield']} *",
            f"  {'(equipped)' if equipped['shield'] else ''}                *",
            f"* * * * * * * * * *",
            f"* * * * * * * * * * *"
        ]

def inventoryWeapons(inventoryWeap):
    

    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios['sanctuaries']['S0']['name']).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios['sanctuaries']['S2']['name']).rjust(3)}                     *",
        f"*        {str(santuarios['sanctuaries']['S1']['name']).rjust(3)}                                    {str(santuarios['sanctuaries']['S3']['name']).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios['sanctuaries']['S4']['name']).rjust(3)}                                 {str(santuarios['sanctuaries']['S5']['name']).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios['sanctuaries']['S6']['name']).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]
   

    for i in range(len(map)):
        print(map[i], inventoryWeap[i])


# Utiliza el método replace y asigna el resultado a la posición 0 de hyrule
#hyrule[0] = hyrule[0].replace(hyrule[0][1], "X")
#print(hyrule[0])
    
                
def print_map(map_data, elements, inventory, map_name="Hyrule"):
    # Colocar los elementos en el mapa en las posiciones indicadas por "x" y "y"
    for element in elements:
        if element["name"] == "Enemy":
            map_data[element["y"]][element["x"]] = element["symbol"] + str(element["life"])
        else:
            map_data[element["y"]][element["x"]] = element["symbol"]

    # Calculate the length of the longest line
    max_length = max(len("".join(row)) for row in map_data)
    max_length = max(max_length, len(map_name))

    # Imprimir borde superior con el nombre del mapa y el título del inventario
    print(f"\n* {map_name}  * * * * * * * * * * * * * * * * * * * * * * * * * *{inventory[0]}")


    # Imprime cada fila de map_data y las líneas restantes de inventory uno al lado del otro
    for i in range(len(map_data)):  # Comenzar desde 0
        # Limit the inventory to 20 characters per line
        inventory_line = inventory[i+1][:20] if i+1 < len(inventory) else ''  # Start from 1 in inventory
        print("*" + "".join(map_data[i]).ljust(max_length) +"*" + inventory_line.ljust(20))  # Pad inventory_line to 20 characters

    # Imprimir borde inferior con el mensaje
    print("* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * * *")






