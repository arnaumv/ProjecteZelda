
import os
from funciones import player
import funciones
from consultas import * 

x = "X"

last_player = list(player.keys())[-1]
sanctuary_value0 = player[last_player]["sanctuaries"]["S0"]["name"]
sanctuary_value1 = player[last_player]["sanctuaries"]["S1"]["name"]
sanctuary_value2 = player[last_player]["sanctuaries"]["S2"]["name"]
sanctuary_value3 = player[last_player]["sanctuaries"]["S3"]["name"]
sanctuary_value4 = player[last_player]["sanctuaries"]["S4"]["name"]
sanctuary_value5 = player[last_player]["sanctuaries"]["S5"]["name"]
sanctuary_value6 = player[last_player]["sanctuaries"]["S6"]["name"]


maps = {
    "Hyrule" : {
    
        "map" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","~","O","O","O","O","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"," "," "," ","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" ","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        ],
        "elements" : [
            {"name" : "Cuina" , "symbol" : "C", "x" : 16, "y" : 2},
            {"name" : "Tree" , "symbol" : "T", "x" : 5, "y" : 3, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 35, "y" : 4, "life" : 9,"max_life": 9, "EnemyNumber" : 0},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value0, "x" : 42, "y" : 5, "SanctuaryNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 10, "y" : 7},
            {"name" : "Tree" , "symbol" : "T", "x" : 46, "y" : 7, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 20, "y" : 8, "life" : 1,"max_life": 1,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value1, "x" : 28, "y" : 8, "SanctuaryNumber" : 1},
            {"name" : "Chest" , "symbol" : "M", "x" : 46, "y" : 8,},
            {"name" : "Tree" , "symbol" : "T", "x" : 44, "y" : 8, "hits" : 0},
            {"name" : "Fox" , "symbol" : "F", "x" : 50, "y" : 8, "visible" : False}
        ]
    },

     "Death mountain" : {
        "map" : [
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," ","O","O"," "," "," "," ","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," ","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        ],
        "elements" : [
            {"name" : "Sanctuary" , "symbol" : sanctuary_value2, "x" : 5, "y" : 2, "SanctuaryNumber" : 2},
            {"name" : "Enemy" , "symbol" : "E", "x" : 11, "y" : 3, "life" : 2, "max_life": 2, "EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Cuina" , "symbol" : "C", "x" : 5, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 8, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 7, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 18, "y" : 6, "hits" : 0},
            {"name" : "Fox" , "symbol" : "F", "x" : 29, "y" : 1, "visible" : False},
            {"name" : "Chest" , "symbol" : "M", "x" : 35, "y" : 7,},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value3, "x" : 48, "y" : 8, "SanctuaryNumber" : 3},
            {"name" : "Enemy" , "symbol" : "E", "x" : 50, "y" : 2, "life" : 2,"EnemyNumber" : 1}
        ]
    },

       "Gerudo" : {
        "map" : [
            ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," ","O","O","O","O","O"," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A"," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"]
        ],
        "elements" : [
            {"name" : "Enemy" , "symbol" : "E", "x" : 2, "y" : 3, "life" : 1,"max_life": 1, "EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 4, "y" : 7, "hits" : 0},
            {"name" : "Chest" , "symbol" : "M", "x" : 7, "y" : 8,},
            {"name" : "Cuina" , "symbol" : "C", "x" : 14, "y" : 3},
            {"name" : "Tree" , "symbol" : "T", "x" : 28, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 29, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 31, "y" : 2, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2,"max_life": 2,"EnemyNumber" : 1},
            {"name" : "Fox" , "symbol" : "F", "x" : 47, "y" : 7, "visible" : False},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value4, "x" : 45, "y" : 2, "SanctuaryNumber" : 4},
            {"name" : "Chest" , "symbol" : "M", "x" : 51, "y" : 0,},
        ]
    },

         "Necluda" : {
        "map" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~"],
            ["O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~"],
            ["O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~"],
            ["~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"]
        ],
        "elements" : [
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 1},
            {"name" : "Fox" , "symbol" : "F", "x" : 5, "y" : 6, "visible" : False},
            {"name" : "Enemy" , "symbol" : "E", "x" : 9, "y" : 1, "life" : 1,"max_life": 1, "EnemyNumber" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 13, "y" : 6, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 5, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 7, "hits" : 0},
            {"name" : "Cuina" , "symbol" : "C", "x" : 18, "y" : 2},
            {"name" : "Chest" , "symbol" : "M", "x" : 21, "y" : 0,},
            {"name" : "Chest" , "symbol" : "M", "x" : 22, "y" : 8,},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value6, "x" : 32, "y" : 8, "SanctuaryNumber" : 6},
            {"name" : "Tree" , "symbol" : "T", "x" : 34, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 35, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 36, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 37, "y" : 1, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2, "max_life": 2, "EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value5, "x" : 50, "y" : 5, "SanctuaryNumber" : 5},
            {"name" : "Chest" , "symbol" : "M", "x" : 50, "y" : 1,}
        ]
    },
}



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

#Funcion para equipar y desequipar objetos
    
def equip(item):
    if item in player[last_player]["weapons"] and player[last_player]["weapons"][item]["equipped"] == False:
        if "sword" in item:
            old_item = player[last_player]["inventory"]["weapon1"]
            player[last_player]["weapons"][old_item]["equipped"] = False
            player[last_player]["inventory"]["weapon1"] = item
            player[last_player]["weapons"][item]["equipped"] = True
        elif "shield" in item:
            old_item = player[last_player]["inventory"]["weapon2"]
            player[last_player]["weapons"][old_item]["equipped"] = False
            player[last_player]["inventory"]["weapon2"] = item
            player[last_player]["weapons"][item]["equipped"] = True
        else:
            promptAfegir("You can't equip this item")
        return

def unequip(item):
        if item in player[last_player]["weapons"] and player[last_player]["weapons"][item]["equipped"] == True:
            if "sword" in item:
                player[last_player]["inventory"]["weapon1"] = None
                player[last_player]["weapons"][item]["equipped"] = False
            elif "shield" in item:
                player[last_player]["inventory"]["weapon2"] = None
                player[last_player]["weapons"][item]["equipped"] = False
            else:
                promptAfegir("You can't unequip this item")
            return
#Funcion para el Timeblood
                
def timeblood(elements):
    while player[last_player]["inventory"]["timeBlood"] > 0:
        player[last_player]["inventory"]["timeBlood"] =- 1
        break
    if player[last_player]["inventory"]["timeBlood"] == 0:
        for element in elements:
            if element["symbol"] == "E":
                element["life"] = element["max_life"]
    return


#Funcion para moverse por el mapa
    
  
def move_player(map_data, elements, direction, num_steps):
    valid_position = [" "]
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
            for _ in range(num_steps):
                new_x_pos = x_pos + (1 if direction == "right" else -1) if direction in ["left", "right"] else x_pos
                new_y_pos = y_pos + (1 if direction == "down" else -1) if direction in ["up", "down"] else y_pos

                if new_x_pos < 0 or new_y_pos < 0 or new_y_pos >= len(map_data) or new_x_pos >= len(map_data[new_y_pos]) or map_data[new_y_pos][new_x_pos] not in valid_position:
                    return False

                # Set the old position to empty
                map_data[y_pos][x_pos] = " "

                # Update the player's position
                x_pos, y_pos = new_x_pos, new_y_pos

            # Set the new position to "X"
            map_data[y_pos][x_pos] = "X"
            element["x"], element["y"] = x_pos, y_pos
    return True

def go_by(x, map_data, elements):
    valid_position = [" "]
    place = x.lower()
    for element in elements:
        if element["name"].lower() == place or element["symbol"] == element:
            x_pos, y_pos = element["x"], element["y"]
        else:
            promptAfegir("This element doesn't exist")
        if map_data[y_pos - 1][x_pos] in valid_position:
            for element in elements:
                if element["symbol"] == "X":
                    element["x"] = x_pos
                    element["y"] = y_pos - 1
        elif map_data[y_pos + 1][x_pos] in valid_position:
            for element in elements:
                if element["symbol"] == "X":
                    element["x"] = x_pos
                    element["y"] = y_pos + 1
        elif map_data[y_pos][x_pos - 1] in valid_position:
            for element in elements:
                if element["symbol"] == "X":
                    element["x"] = x_pos - 1
                    element["y"] = y_pos
        elif map_data[y_pos][x_pos + 1] in valid_position:
            for element in elements:
                if element["symbol"] == "X":
                    element["x"] = x_pos + 1
                    element["y"] = y_pos
        else:
            promptAfegir("Error, the element you are trying to go to has no valid positions")
            break
            


#Funcion para pescar y cazar

def fish(map_data, elements):
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
        
        if map_data[y_pos + 1][x_pos] == "~" or map_data[y_pos - 1][x_pos] == "~" or map_data[y_pos][x_pos + 1] == "~" or map_data[y_pos][x_pos - 1] == "~" and "pescar" == True:
            probabilidad = 0.2
            numero_aleatorio = random.random()
            if numero_aleatorio < 0.2:
                promptAfegir("You got a fish")
                player[last_player]["food"]["fish"]["count"] =+ 1
                return
            else:
                promptAfegir("You didn't get a fish")
                return

def close_chests(map_data, elements):
    for element in elements:
        if element["symbol"] == "W":
            element["symbol"] = "M"

def all_chests_open(map_data, elements):
    cnt = 0
    for element in elements:
        if element["symbol"] == "M":
            cnt += 1
    if cnt == 0:
        close_chests(map_data, elements)

def count_opened_sanctuaries():
    # Initialize a dictionary to store the count for each map
    opened_sanctuaries_count = {}

    # Loop through all the sanctuaries
    for sanctuary in player[last_player]["sanctuaries"].values():
        # If the sanctuary is opened
        if sanctuary["opened"]:
            # Get the map name
            map_name = sanctuary["map"]

            # If the map name is not in the dictionary, add it with a count of 1
            if map_name not in opened_sanctuaries_count:
                opened_sanctuaries_count[map_name] = 1
            # If the map name is already in the dictionary, increment the count
            else:
                opened_sanctuaries_count[map_name] += 1

    # Return the dictionary of opened sanctuaries count for each map
    return opened_sanctuaries_count

   
def open(map_data, elements, place, map_name):
    if place.lower() == "sanctuary":
        for element in elements:
            if element["name"] == "Sanctuary":
                x_pos, y_pos = element["x"], element["y"]
                if map_data[y_pos - 1][x_pos] == "X" or map_data[y_pos + 1][x_pos] == "X" or map_data[y_pos][x_pos - 1] == "X" or map_data[y_pos][x_pos + 1] == "X":
                    sanctuary = element["symbol"]
                    player[last_player]["sanctuaries"][sanctuary]["name"].replace("?","")
                    player[last_player]["sanctuaries"][sanctuary]["opened"] = True
                    player[last_player]["sanctuaries"][sanctuary]["map"] = map_name  # Guarda el nombre del mapa actual
                    player[last_player]["inventory"]["max_lives"] += 1
                    promptAfegir(f"You opened {sanctuary}")
                    count_opened_sanctuaries = count_opened_sanctuaries()  # Cuenta los santuarios abiertos

    elif place.lower() == "chest":
        for element in elements:
            if element["symbol"] == "M":
                x_pos, y_pos = element["x"], element["y"]
                if map_data[y_pos - 1][x_pos] == "X" or map_data[y_pos + 1][x_pos] == "X" or map_data[y_pos][x_pos - 1] == "X" or map_data[y_pos][x_pos + 1] == "X":
                    map_swords = ["hyrule", "gerudo"]
                    map_shields = ["death mountain", "necluda"]
                    if map_data.lower() in map_swords:
                        swords = ["sword", "wood sword"]
                        item = random.choice(swords)
                        player[last_player]["weapons"][item]["count"] += 1
                        promptAfegir(f"You obtained a {item}")
                    elif map_data.lower() in map_shields:
                        shields = ["shield", "wood shield"]
                        item = random.choice(shields)
                        player[last_player]["weapons"][item]["count"] += 1
                        promptAfegir(f"You obtained a {item}")
                    element["symbol"] = "W"
                    element["opened"] = True  # Marca el cofre como abierto
                    player[last_player]["inventory"]["chests_opened"] += 1  # Suma 1 a cofres abiertos
                    all_chests_open(map_data, elements)
                    opened_chests_count = count_opened_chests(map_name)  # Cuenta los cofres abiertos
                    print(f"Number of opened chests: {opened_chests_count}")
                else:
                    promptAfegir("This chest has alredy been opened")

def count_opened_chests(map_name):
    elements = maps[map_name]['elements']
    opened_chests = [element for element in elements if element['name'] == 'Chest' and element['opened'] == True]
    return len(opened_chests)


## Definir las conexiones entre los mapas
map_connections = {
    "Hyrule": ["Gerudo", "Death mountain", "Castle"],
    "Death mountain": ["Hyrule", "Necluda", "Castle"],
    "Gerudo": ["Hyrule", "Necluda", "Castle"],
    "Necluda": ["Death mountain", "Gerudo", "Castle"]
}
# Diccionario de inventarios
inventories = {
    "main": inventoryM,
    "weapons": inventoryWeap,
    "food": inventoryFood
}

# Iniciar en el mapa "Hyrule"
current_map = "Hyrule"
current_inventory = "main"  # Iniciar con el inventario principal




# Logica del Juego

while True:
    clear_terminal()
    print_map(maps[current_map]["map"], maps[current_map]["elements"], inventories[current_inventory], map_name=current_map)
    
    while True:
        command = input("What to do now? (ex: 'go up 3' or 'go to Castle' or 'show inventory [main/weapons/food/help]'): ").lower().split()

        if len(command) < 2:
            promptAfegir("Invalid command. Please enter a command in the format 'go [direction] [number of steps]' or 'go to [map]' or 'show inventory [main/weapons/food/help]'.")
            continue

        if command[0] == "show" and command[1] == "inventory":
            if command[2] == "help":
                # Llamar a la función helpInventoryMenu
                from maps import helpInventoryMenu
                helpInventoryMenu()
                break
            else:
                # Cambiar de inventario
                new_inventory = command[2]
                if new_inventory in inventories:
                    current_inventory = new_inventory
                    break
                else:
                    promptAfegir(f"You can't show {new_inventory} inventory.")
                    continue

        if command[0] == "go" and command[1] == "to":
            # Save game state before changing sections
            user_name = last_player
            game_state = {
                'hearts_remaining': player[last_player]["inventory"]["lives"],
                'blood_moon_countdown': player[last_player]["inventory"]["timeBlood"],
                'region': current_map
            }
            save_game_state_to_db(game_state, user_name)
            # Change map
            new_map = " ".join(command[2:]).capitalize()
            if new_map in map_connections[current_map]:
                current_map = new_map
            else:
                promptAfegir(f"You can't go to {new_map} from {current_map}.")
                continue

        direction = command[1]
        try:
            num_steps = int(command[2])
        except ValueError:
            promptAfegir("You can't go there, it's not a valid position")
            continue

        if move_player(maps[current_map]["map"], maps[current_map]["elements"], direction, num_steps):
            break
        else:
            promptAfegir("You can't go there, it's not a valid position")