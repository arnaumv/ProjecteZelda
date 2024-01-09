from datetime import datetime
from menus import *
from menus import current_player_name
import random
import os
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", db="Zelda")
cur = conn.cursor()



###############################  OPCIONES MENU INICIO ##############################

# Lista de funciones de menú disponibles
menus = [menu1, menu2, menu3]

def mostrar_menu_aleatorio():
    clear_terminal()
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
            "S0": {"name": "S0?" , "oppened": False} ,
            "S1":  {"name": "S1?" , "oppened": False} ,
            "S2":  {"name": "S2?" , "oppened": False} ,
            "S3":  {"name": "S3?" , "oppened": False} ,
            "S4":  {"name": "S4?" , "oppened": False} ,
            "S5":  {"name": "S5?" , "oppened": False} ,
            "S6":  {"name": "S6?" , "oppened": False} ,
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
def inventoryMain(santuarios, playerInfo):
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

    inventoryM = [
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
        print(map[i], inventoryM[i])





########################################### INVENTARI FOODS #####################################################


foods = {
    "food": player[ultimo_jugador]["food"]
}

def inventoryFoods(santuarios, foods):
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

    for i in range(len(map)):
        print(map[i], inventoryFood[i])


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

    for i in range(len(map)):
        print(map[i], inventoryWeap[i])










def show_games():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", db="Zelda")
        cur = conn.cursor()

        # Query para seleccionar los valores específicos de la tabla game
        select_query = "SELECT game_id, user_name, date_started, hearts_remaining, region FROM game"
        cur.execute(select_query)

        # Obtener los resultados
        resultados = cur.fetchall()

        games = ["".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74)]

        # Construir el formato para mostrar los juegos
        for i in range(len(resultados)):
            games[i] = (f'{resultados[i][0]}: {resultados[i][1]} - {resultados[i][2]}'.ljust(68) +
                         f'♥ {resultados[i][3]}/{resultados[i][4]}')

        show_games = [
            f"\n* Saved Games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
            f"\n*                                                                             *",
            f"\n* {games[0]}  *",
            f"\n* {games[1]}  *",
            f"\n* {games[2]}  *",
            f"\n* {games[3]}  *",
            f"\n* {games[4]}  *",
            f"\n* {games[5]}  *",
            f"\n* {games[6]}  *",
            f"\n* {games[7]}  *",
            f"\n*                                                                             *",
            f"\n* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"
        ]
        print("".join(show_games))

        cur.close()
        conn.close()
    except pymysql.Error as e:
        print(f"Error: {e}")















def showStartedGames():
    import mysql.connector
    try:
        conexion = mysql.connector.connect(
        user = "root",
        password = "",
        host = "localhost",
        database = "zelda",
        port=3306
        )

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    cursor = conexion.cursor()

    tabla = "datosplayer"

    consulta = f"SELECT * FROM {tabla}"
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    games = ["".ljust(74), "".ljust(74), "".ljust(74),"".ljust(74),"".ljust(74),"".ljust(74), "".ljust(74),"".ljust(74),]

    for i in range(len(resultados)):
        games[i] = (f'{resultados[i][0]}: {resultados[i][1]} - {resultados[i][2]}'.ljust(68) + f'♥ {resultados[i][4]}/{resultados[i][5]}') 

    showGames = [
        f"\n* Saved Games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*                                                                             *",
        f"\n* {games[0]}  *",
        f"\n* {games[1]}  *",
        f"\n* {games[2]}  *",
        f"\n* {games[3]}  *",
        f"\n* {games[4]}  *",
        f"\n* {games[5]}  *",
        f"\n* {games[6]}  *",
        f"\n* {games[7]}  *",
        f"\n*                                                                             *",
        f"\n* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]
    print("".join(showGames))







