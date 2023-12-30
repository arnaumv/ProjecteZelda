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
            "wood sword": {"uses": 4, "count": 1, "equipped": True},
            "sword": {"uses": 0, "count": 0, "equipped": False},
            "wood shield": {"uses": 5, "count": 1, "equipped": True},
            "shield": {"uses": 0, "count": 0, "equipped": False}
        },
        "food": {
            "vegetables": {"count":1, "hearts":1},
            "fish": {"count": 2, "hearts":0},
            "meat": {"count": 0, "hearts":0},
            "salads": {"count": 0, "hearts":2},
            "pescatarian": {"count": 0, "hearts":3},
            "roasted": {"count": 2, "hearts":4}
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
foods = [4, 2, 2, 2, 1, 1]
uses = {
    "wood sword": 5,
    "sword": 9,
    "wood shield": 5,
    "shield": 9
}
count = {
    "wood sword": 2,
    "sword": 1,
    "wood shield": 0,
    "shield": 2
}
equipped = {
    "wood sword": True,
    "sword": False,
    "wood shield": True,
    "shield": False
}


########################################### INVENTARI #####################################################





def inventoryMain(santuarios, player_name, playerInfo):
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
        f" {player_name}  ♥ {playerInfo[0]}/{playerInfo[1]}",
        f" Blood moon in {playerInfo[2]}",
        f"                   *",
        f" Equipment         *",
        f"       {playerInfo[3]} ",
        f"       {playerInfo[4]} ",
        f" Food            {playerInfo[5]} ",
        f" Weapons         {playerInfo[6]} ",
        f"* * * * * * * * * *"
    ]

    for i in range(len(map)):
        print(map[i], inventory[i])










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

    inventory = [
        f"* * * * * Foods *",
        f"                  *",
        f"                  *",
        f"Vegetables      {str(foods[0]).rjust(1)} *",
        f"Fish            {str(foods[1]).rjust(1)} *",
        f"Meat            {str(foods[2]).rjust(1)} *",
        f"                  *",
        f"Salads          {str(foods[3]).rjust(1)} *",
        f"Pescatarian     {str(foods[4]).rjust(1)} *",
        f"Roasted         {str(foods[5]).rjust(1)} *",
        f"                  *",
        f"* * * * * * * * * *"
    ]

    for i in range(len(map)):
        print(map[i], inventory[i])


def inventoryWeapons(santuarios, uses, count, equipped):
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
