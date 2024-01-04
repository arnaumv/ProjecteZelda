from datetime import datetime
from menus import *
from menus import current_player_name
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

##########################      INFO PLAYER        #########################
    

    

player = {
    "default": {
        "inventory": {
            "lives": 3,
            "max_lives": 3,
            "timeBlood": 60,
            "weapon1": "Wood Sword",
            "weapon2": "Wood Shield",
            "totalFood": 0,
            "totalWeapons": 2,
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
            "S0": False,
            "S1": False,
            "S2": False,
            "S3": False,
            "S4": False,
            "S5": False,
            "S6": False
        },
    }
}

santuarios = ["S0", "S1", "S2", "S3", "S4", "S5", "S6"] 




########################################### INVENTARI #####################################################



########################################### INVENTARI MAIN #####################################################

jugadores = player.keys()
ultimo_jugador = list(jugadores)[-1]
playerInfo = {
    "inventory": player[ultimo_jugador]["inventory"]
}



def inventoryMain(santuarios, playerInfo):
    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios[0]).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios[2]).rjust(3)}                     *",
        f"*        {str(santuarios[1]).rjust(3)}                                    {str(santuarios[3]).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios[4]).rjust(3)}                                 {str(santuarios[5]).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios[6]).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    inventory = [
        f"* * * * Inventory *",
        f"                  *",
        f"                  *",
        f" {current_player_name}  ♥ {playerInfo['inventory']['lives']}/{playerInfo['inventory']['max_lives']}      *",
        f" Blood moon in {playerInfo['inventory']['timeBlood']} *",
        f"                  *",
        f" Equipment        *",
        f"       {playerInfo['inventory']['weapon1']} *",
        f"       {playerInfo['inventory']['weapon2']}*",
        f" Food            {playerInfo['inventory']['totalFood']}*",
        f" Weapons         {playerInfo['inventory']['totalWeapons']}*",
        f"* * * * * * * * * *"
    ]

    for i in range(len(map)):
        print(map[i], inventory[i])





########################################### INVENTARI FOODS #####################################################


foods = {
    "food": player[ultimo_jugador]["food"]
}

def inventoryFoods(santuarios, foods):
    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios[0]).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios[2]).rjust(3)}                     *",
        f"*        {str(santuarios[1]).rjust(3)}                                    {str(santuarios[3]).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios[4]).rjust(3)}                                 {str(santuarios[5]).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios[6]).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    # Acceder a los valores de "count" para cada comida
    vegetables_count = foods['food']['vegetables']['count']
    fish_count = foods['food']['fish']['count']
    meat_count = foods['food']['meat']['count']
    salads_count = foods['food']['salads']['count']
    pescatarian_count = foods['food']['pescatarian']['count']
    roasted_count = foods['food']['roasted']['count']

    # Incorporar estos valores en tu inventario
    inventory = [
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

    for i in range(len(map)):
        print(map[i], inventory[i])


########################################### INVENTARI WEAPONS #####################################################

def inventoryWeapons(santuarios, player):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]

    # Acceder a la información de armas del último jugador
    weapons_info = player[ultimo_jugador]['weapons']

    # Acceder a los detalles de las armas del último jugador
    uses = {weapon: weapons_info[weapon]['uses'] for weapon in weapons_info}
    count = {weapon: weapons_info[weapon]['count'] for weapon in weapons_info}
    equipped = {weapon: weapons_info[weapon]['equipped'] for weapon in weapons_info}

    map = [
        f"* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"*                                                         *",
        f"*  Hyrule        {str(santuarios[0]).rjust(3)}                       Death Mountain *",
        f"*                                 {str(santuarios[2]).rjust(3)}                     *",
        f"*        {str(santuarios[1]).rjust(3)}                                    {str(santuarios[3]).rjust(3)}       *",
        f"*                                                         *",
        f"*                         Castle                          *",
        f"*                                                         *",
        f"*                {str(santuarios[4]).rjust(3)}                                 {str(santuarios[5]).rjust(3)}  *",
        f"*  Gerudo                             {str(santuarios[6]).rjust(3)}        Necluda  *",
        f"*                                                         *",
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        ]
    inventory = [
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

    for i in range(len(map)):
        print(map[i], inventory[i])