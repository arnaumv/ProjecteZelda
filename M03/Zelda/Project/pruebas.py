import sys
from funciones import *
from maps import *


import os
from funciones import player
from funciones import * 

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
            {"name" : "Enemy" , "symbol" : "E", "x" : 35, "y" : 4, "life" : 9,"EnemyNumber" : 0},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value0, "x" : 42, "y" : 5, "SanctuaryNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 10, "y" : 7},
            {"name" : "Tree" , "symbol" : "T", "x" : 46, "y" : 7, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 20, "y" : 8, "life" : 1,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value1, "x" : 28, "y" : 8, "SanctuaryNumber" : 1},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 46, "y" : 8, "item" : "Sword"},
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
            {"name" : "Enemy" , "symbol" : "E", "x" : 11, "y" : 3, "life" : 2,"EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Cuina" , "symbol" : "C", "x" : 5, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 8, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 7, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 18, "y" : 6, "hits" : 0},
            {"name" : "Fox" , "symbol" : "F", "x" : 29, "y" : 1, "visible" : False},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 35, "y" : 7, "item" : "Shield"},
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
            {"name" : "Enemy" , "symbol" : "E", "x" : 2, "y" : 3, "life" : 1,"EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 4, "y" : 7, "hits" : 0},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 7, "y" : 8, "item" : "Sword"},
            {"name" : "Cuina" , "symbol" : "C", "x" : 14, "y" : 3},
            {"name" : "Tree" , "symbol" : "T", "x" : 28, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 29, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 31, "y" : 2, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2,"EnemyNumber" : 1},
            {"name" : "Fox" , "symbol" : "F", "x" : 47, "y" : 7, "visible" : False},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value4, "x" : 45, "y" : 2, "SanctuaryNumber" : 4},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 51, "y" : 0, "item" : "Sword"},
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
            {"name" : "Enemy" , "symbol" : "E", "x" : 9, "y" : 1, "life" : 1,"EnemyNumber" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 13, "y" : 6, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 5, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 7, "hits" : 0},
            {"name" : "Cuina" , "symbol" : "C", "x" : 18, "y" : 2},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 21, "y" : 0, "item" : "Shield"},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 22, "y" : 8, "item" : "Shield"},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value6, "x" : 32, "y" : 8, "SanctuaryNumber" : 6},
            {"name" : "Tree" , "symbol" : "T", "x" : 34, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 35, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 36, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 37, "y" : 1, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : sanctuary_value5, "x" : 50, "y" : 5, "SanctuaryNumber" : 5},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 50, "y" : 1, "item" : "Shield"}
        ]
    },
}
def print_hyrule(map_data, elements, inventory, map_name="Hyrule"):
    # Colocar los elementos en el mapa en las posiciones indicadas por "x" y "y"
    for element in elements:
        if element["name"] == "Enemy":
            map_data[element["y"]][element["x"]] = element["symbol"] + str(element["life"])
        else:
            map_data[element["y"]][element["x"]] = element["symbol"]

    # Add "*" to the borders
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if i == 0 or i == len(map_data) - 1 or j == 0 or j == len(row) - 1:
                map_data[i][j] = "*"

    # Imprimir borde superior con el nombre del mapa y la primera línea del inventario
    print(f"\n* {map_name}  * * * * * * * * * * * * * * * * * * * * * * * * * *{inventory[0]}")

    # Imprime cada fila de map_data y las líneas restantes de inventory uno al lado del otro
    for i in range(1, len(map_data) - 1):
        print("* " + "".join(map_data[i][1:-1]) + " * " + inventory[i])

    # Imprimir borde inferior con el mensaje
    print("* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open  * * * * * * * * * * *")
    
#print_hyrule(maps["Hyrule"]["map"], maps["Hyrule"]["elements"], inventoryM)
from collections import deque
def find_nearest_valid_position(map_data, elements, target_symbols):
    if isinstance(target_symbols, str):
        target_symbols = [target_symbols]

    if "water" in target_symbols:
        target_symbols.remove("water")
        target_symbols.append("~")

    target_positions = [(element["x"], element["y"]) for element in elements if element["symbol"] in target_symbols]

    if not target_positions:
        return None

    player = next((element for element in elements if element["symbol"] == "X"), None)

    if player is None:
        return None

    player_pos = (player["x"], player["y"])

    # Ordena las posiciones objetivo por distancia a la posición del jugador
    target_positions.sort(key=lambda pos: abs(pos[0] - player_pos[0]) + abs(pos[1] - player_pos[1]))

    for target_pos in target_positions:
        x, y = target_pos

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(map_data[0])
                and 0 <= new_y < len(map_data)
                and map_data[new_y][new_x] not in ["#", "T", "F", "K", "~", "*"]
            ):
                return new_x, new_y

    return None

def move_player(map_data, elements, direction, num_steps):
    invalid_positions = ["#", "T", "F", "K", "~", "*"]
    player = None

    for element in elements:
        if element["symbol"] == "X":
            player = element
            break

    if player is None:
        return False

    x_pos, y_pos = player["x"], player["y"]

    if direction == "by":
        target_symbols = num_steps.split()  # Extraer todos los símbolos objetivo de la cadena de texto
        new_pos = find_nearest_valid_position(map_data, elements, target_symbols)
        if new_pos is None:
            print(f"No valid position next to {num_steps} found.")
            return False
        new_x_pos, new_y_pos = new_pos
        map_data[y_pos][x_pos] = " "
        map_data[new_y_pos][new_x_pos] = "X"
        player["x"], player["y"] = new_x_pos, new_y_pos
    else:
        for _ in range(num_steps):
            new_x_pos = x_pos + (1 if direction == "right" else -1) if direction in ["left", "right"] else x_pos
            new_y_pos = y_pos + (1 if direction == "down" else -1) if direction in ["up", "down"] else y_pos

            if new_x_pos < 0 or new_y_pos < 0 or new_y_pos >= len(map_data) or new_x_pos >= len(map_data[new_y_pos]) or map_data[new_y_pos][new_x_pos] in invalid_positions:
                return False

            map_data[y_pos][x_pos] = " "
            x_pos, y_pos = new_x_pos, new_y_pos

        map_data[y_pos][x_pos] = "X"
        player["x"], player["y"] = x_pos, y_pos

    return True


while True:
    print_hyrule(maps["Hyrule"]["map"], maps["Hyrule"]["elements"], inventoryM)
    
    while True:
        command = input("What to do now? (ex: 'go up 3'): ").lower().split()

        if len(command) < 2:
            print("Invalid command. Please enter a command in the format 'go [direction] [number of steps]'.")
            continue

        direction = command[1]
        try:
            if direction == "by":
                num_steps = " ".join(command[2:])
            else:
                num_steps = int(command[2])
        except ValueError:
            print("You can't go there, it's not a valid position")
            continue

        if move_player(maps["Hyrule"]["map"], maps["Hyrule"]["elements"], direction, num_steps):
            break
        else:
            print("You can't go there, it's not a valid position")

            
""" lp = True
invalid_positions = ["*", "T", "F", "C", "O","~"]  # Add other invalid positions here
def move_player():
    for _ in range(num_steps):
        can_move = True
        for i in range(len(hyrule)):
            if x in hyrule[i]:
                pos = hyrule[i].find("X")
                if direction == "up" and (hyrule[i-1][pos] in invalid_positions or hyrule[i-1] == hyrule[0]):
                    can_move = False
                elif direction == "down" and (hyrule[i+1][pos] in invalid_positions or hyrule[i+1] == hyrule[11]):
                    can_move = False
                elif direction == "left" and (hyrule[i][pos-1] in invalid_positions or hyrule[i][pos-1] == hyrule[i][0]):
                    can_move = False
                elif direction == "right" and (hyrule[i][pos+1] in invalid_positions or hyrule[i][pos+1] == hyrule[i][59]):
                    can_move = False

                if can_move:
                    hyrule[i] = hyrule[i].replace("X", " ")
                    if direction == "up":
                        hyrule[i-1] = hyrule[i-1][:pos] + x + hyrule[i-1][pos + 1:]
                    elif direction == "down":
                        hyrule[i+1] = hyrule[i+1][:pos] + x + hyrule[i+1][pos + 1:]
                    elif direction == "left":
                        hyrule[i] = hyrule[i][:pos-1] + x + hyrule[i][pos:]
                    elif direction == "right":
                        hyrule[i] = hyrule[i][:pos+1] + x + hyrule[i][pos+2:]
                else:
                    print("You can't go there, is not a valid position")
                break
        if not can_move:
            break

while lp:
    print("".join(hyrule))
    command = input("What to do now? (ex: 'go up 3'): ").lower().split()

    if len(command) < 3:
        print("Invalid command. Please enter a command in the format 'go [direction] [number of steps]'.")
        continue

    direction = command[1]
    try:
        num_steps = int(command[2])
    except ValueError:
        print("You can't go there, is not a valid position")
        continue

    move_player() """