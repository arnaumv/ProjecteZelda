
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
     "Castle" : {
        "map" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","\\"," ","/"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","-","-"," ","O"," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","G","a","n","o","n"," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","/"," ","\\"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|",">"," "," ","v","-","v","-","v","-","v"," "," "," ","|",">"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",","," "," "," ",","," "," ","/","_","\\"," "," ","|"," "," "," "," "," ","|"," "," ","/","_","\\"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|","\\","_","/","|"," "," ","|"," ","|","'","'","'","'","'","'","'","'","'","'","'","|"," ","|"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","(","q"," ","p",")",",","-","|"," ","|"," ","|","|"," "," ","_"," "," ","|","|"," ","|"," ","|","'","-",".","_"," ","|","\\"," "," "," "," "," "],
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\\","_","/","_","(","/","|"," ","|"," "," "," "," ","|","#","|"," "," "," "," ","|"," ","|"," ",")"," "," ","'","/","/"," "," "," "," "," "],
            ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
        ],
        "elements" : [
            {"name" : "Player" , "symbol" : "X", "x" : 2, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 1, "y" : 8, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 46, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 47, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 48, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 49, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 50, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 51, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 52, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 53, "y" :2, "hits" : 0},
            {"name" : "Ganon" , "symbol" : "G", "x" : 20, "y" :8},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 0, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 1, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 2, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 3, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 4, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 5, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 6, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 7, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 8, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 9, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 10, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 11, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 12, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 13, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 14, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 15, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 16, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 17, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 18, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 19, "y" :7},
        ]
    }
}
prompt = []

def promptAfegir(text):
    global prompt
    prompt.append(text)
    if len(prompt) >= 4:
        prompt.pop(0)


########################################################################################
#### HE MODIFICADO ESTA FUNCION PARA QUE COJIERA LAS FUNCIONES DE LOS INVENTARIOS  #####


def print_map(map_data, elements, player, current_inventory, map_name="Hyrule"):
    
     # Create the inventories
    inventoryM = create_main_inventory(player)
    inventoryFood = create_food_inventory(player)
    inventoryWeap = create_weapons_inventory(player)

    # Choose the current inventory
    inventories = {
        "main": inventoryM,
        "food": inventoryFood,
        "weapons": inventoryWeap
    }
    inventory = inventories[current_inventory]
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





###  HE CREADO ESTA FUNCION PARA QUE EMUESTRE EL INVENTARIO MAIN ACTUALIZADO ####
def create_main_inventory(player):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]
    playerInfo = {
        "inventory": player[ultimo_jugador]["inventory"]
    }

    player_name = ultimo_jugador  # Assuming the player's name is the last key in the player dictionary

    inventoryM = [
        " * * * * Inventory *",
        "                   *",
        f" {player_name:<13}♥ {playerInfo['inventory']['lives']}/{playerInfo['inventory']['max_lives']}*",
        f"  Blood moon in {playerInfo['inventory']['timeBlood']} *",
        "                   *",
        " Equipment         *",
        f"       {playerInfo['inventory']['weapon1']}  *",
        f"       {playerInfo['inventory']['weapon2']} *",
        f" Food            {playerInfo['inventory']['totalFood']} *",
        f" Weapons         {playerInfo['inventory']['totalWeapons']} *",
        "                   *"
    ]

    return inventoryM


###  HE CREADO ESTA FUNCION PARA QUE EMUESTRE EL INVENTARIO WEAPONS ACTUALIZADO ####

def create_weapons_inventory(player):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]

    # Access the weapon information of the last player
    weapons_info = player[ultimo_jugador]['weapons']

    # Access the details of the last player's weapons
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

    return inventoryWeap

###  HE CREADO ESTA FUNCION PARA QUE MUESTRE EL INVENTARIO FOODS ACTUALIZADO ####

def create_food_inventory(player):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]

    #foods = {
    #    "food": player[ultimo_jugador]["food"]
    #}

   # Access the "count" values for each food
    vegetables_count = player[ultimo_jugador]['food']['vegetables']['count']
    fish_count = player[ultimo_jugador]['food']['fish']['count']
    meat_count = player[ultimo_jugador]['food']['meat']['count']
    salads_count = player[ultimo_jugador]['food']['salads']['count']
    pescatarian_count = player[ultimo_jugador]['food']['pescatarian']['count']
    roasted_count = player[ultimo_jugador]['food']['roasted']['count']

    # Incorporate these values into your inventory
    inventoryFood = [
        f" * * * * * * Foods *",
        f"                   *",
        f"                   *",
        f" Vegetables     {str(vegetables_count).rjust(1)}  *",
        f" Fish           {str(fish_count).rjust(1)}  *",
        f" Meat           {str(meat_count).rjust(1)}  *",
        f"                   *",
        f" Salads         {str(salads_count).rjust(1)}  *",
        f" Pescatarian    {str(pescatarian_count).rjust(1)}  *",
        f" Roasted        {str(roasted_count).rjust(1)}  *",
        f"                   *",
        f"* * * * * * * * * *"
    ]

    return inventoryFood

##########################################



###### FUNCION QUE AL ESCRIBIR "SHOW MAP" MUESTRA EL MAPA ###### 
def inventoryMain(player, player_name):
    jugadores = player.keys()          
    ultimo_jugador = list(jugadores)[-1]    #Coje el ultimo jugador añadido en el diccionario 
    playerInfo = {
        "inventory": player[ultimo_jugador]["inventory"]
    }

    santuarios = {
        "sanctuaries": player[ultimo_jugador]["sanctuaries"]   #Coje el valor que hay dentro de "sanctuaries"
    }

    inventoryM = [
        f"* * * * * Inventory *",
        f"                    *",
        f" {player_name}         ♥ {playerInfo['inventory']['lives']}/{playerInfo['inventory']['max_lives']} *",
        f"  Blood moon in {playerInfo['inventory']['timeBlood']}  *",
        f"                    *",
        f" Equipment          *",
        f"       {playerInfo['inventory']['weapon1']}   *",
        f"       {playerInfo['inventory']['weapon2']}  *",
        f" Food            {playerInfo['inventory']['totalFood']}  *",
        f" Weapons         {playerInfo['inventory']['totalWeapons']}  *",
        f"                    *"
        
        
    ]

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
        f"* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    for i in range(len(map)):
        inventory_line = inventoryM[i] if i < len(inventoryM) else ''
        print(map[i], inventory_line)
        
        
        
#### FUNCION PARA EQUIPAR ARMAS ###
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
            print("You can't equip this item")
        return


### FUNCION PARA DESEQUIPAR ARMAS ###
def unequip(item):
        if item in player[last_player]["weapons"] and player[last_player]["weapons"][item]["equipped"] == True:
            if "sword" in item:
                player[last_player]["inventory"]["weapon1"] = None
                player[last_player]["weapons"][item]["equipped"] = False
            elif "shield" in item:
                player[last_player]["inventory"]["weapon2"] = None
                player[last_player]["weapons"][item]["equipped"] = False
            else:
                print("You can't unequip this item")
            return


  
  
#### FUNCION PARA MOVERSE POR EL MAPA ####
def move_player(map_data, elements, direction, num_steps):
    valid_positions = [" "]  # Añade aquí cualquier otro símbolo que represente una posición inválida
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
            for _ in range(num_steps):
                new_x_pos = x_pos + (1 if direction == "right" else -1) if direction in ["left", "right"] else x_pos
                new_y_pos = y_pos + (1 if direction == "down" else -1) if direction in ["up", "down"] else y_pos

                if new_x_pos < 0 or new_y_pos < 0 or new_y_pos >= len(map_data) or new_x_pos >= len(map_data[new_y_pos]) or map_data[new_y_pos][new_x_pos] not in valid_positions:
                    return False

                # Set the old position to empty
                map_data[y_pos][x_pos] = " "

                # Update the player's position
                x_pos, y_pos = new_x_pos, new_y_pos

            # Set the new position to "X"
            map_data[y_pos][x_pos] = "X"
            element["x"], element["y"] = x_pos, y_pos
    return True

            
#cocinar y comer
        
def cook(map_data, elements, item, last_player):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]
    x_pos, y_pos = None, None
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
    if x_pos is not None and y_pos is not None:
        if map_data[y_pos + 1][x_pos] == "C" or map_data[y_pos - 1][x_pos] == "C" or map_data[y_pos][x_pos + 1] == "C" or map_data[y_pos][x_pos - 1] == "C":
            if item == "salads":
                if "vegetables" in player[ultimo_jugador]["food"] and player[ultimo_jugador]["food"]["vegetables"]["count"] >= 2:
                    player[ultimo_jugador]["food"]["salads"]["count"] += 1
                    player[ultimo_jugador]["food"]["vegetables"]["count"] -= 2
                else:
                    print("Not enough vegetables")
            elif item == "pescatarian":
                if "vegetables" in player[ultimo_jugador]["food"] and "fish" in player[ultimo_jugador]["food"] and player[ultimo_jugador]["food"]["vegetables"]["count"] >= 1 and player[ultimo_jugador]["food"]["fish"]["count"] >= 1:
                    player[ultimo_jugador]["food"]["pescatarian"]["count"] += 1
                    player[ultimo_jugador]["food"]["vegetables"]["count"] -= 1
                    player[ultimo_jugador]["food"]["fish"]["count"] -= 1
                else:
                    print("Not enough vegetables and fish")
            elif item == "roasted":
                if "vegetables" in player[ultimo_jugador]["food"] and "meat" in player[ultimo_jugador]["food"] and player[ultimo_jugador]["food"]["vegetables"]["count"] >= 1 and player[ultimo_jugador]["food"]["meat"]["count"] >= 1:
                    player[ultimo_jugador]["food"]["roasted"]["count"] += 1
                    player[ultimo_jugador]["food"]["vegetables"]["count"] -= 1
                    player[ultimo_jugador]["food"]["meat"]["count"] -= 1
                else:
                    print("Not enough vegetables and meat")
        else:
            print("You are not next to a 'C'.")
    else:
        print("Player position not found.")


def eat(item):
    jugadores = player.keys()
    ultimo_jugador = list(jugadores)[-1]
    if player[ultimo_jugador]["inventory"]["lives"] < player[ultimo_jugador]["inventory"]["max_lives"]:
        if player[ultimo_jugador]["food"][item]["count"] > 0:
            if item == "vegetal":
                player[ultimo_jugador]["inventory"]["lives"] += 1
            elif item == "amanida":
                player[ultimo_jugador]["inventory"]["lives"] += 2
            elif item == "pescatarian":
                player[ultimo_jugador]["inventory"]["lives"] += 3
            elif item == "rostit":
                player[ultimo_jugador]["inventory"]["lives"] += 4
            player[ultimo_jugador]["food"][item]["count"] -= 1
            if player[ultimo_jugador]["inventory"]["lives"] > player[ultimo_jugador]["inventory"]["max_lives"]:
                player[ultimo_jugador]["inventory"]["lives"] = player[ultimo_jugador]["inventory"]["max_lives"]
        else:
            promptAfegir(f"No tens {item}")
    else:
        promptAfegir("Ja estàs ple de salut")


#### FUNCION PARA MOVERSE A UNA POSICION CONCRETA ####
def go_by(x, map_data, elements):
    valid_position = [" "]
    place = x.lower()
    x_pos, y_pos = None, None  # Initialize x_pos and y_pos
    prev_x, prev_y = None, None  # Initialize prev_x and prev_y
    for element in elements:
        if element["name"].lower() == place or element["symbol"].lower() == x:
            x_pos, y_pos = element["x"], element["y"]
            break  # Break the loop once the element is found
    if x_pos is None or y_pos is None:
        print("This element doesn't exist")
        return  # Return from the function if the element does not exist
    for element in elements:
        if element["symbol"] == "X":
            prev_x, prev_y = element["x"], element["y"]  # Store the player's current position before moving
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
        print("Error, the element you are trying to go to has no valid positions")
        return
    map_data[prev_y][prev_x] = " "  # Remove the player's previous position from the map
             

### time blood ###
def timeblood(elements, player, last_player):
    player[last_player]["inventory"]["timeBlood"] -= 1
    if player[last_player]["inventory"]["timeBlood"] == 0:
        for element in elements:
            if element["symbol"] == "E" and element["name"] != "GANON":
                element["life"] = element["max_life"]
        player[last_player]["inventory"]["timeBlood"] = 25
        print('The Blood moon rises once again. Please be careful, Link.')
       
             
### FUNCION PARA ATACAR ###           
def attack(map_data, elements):
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
            player[last_player]["inventory"]["lives"] -= 1
            promptAfegir(f'Be careful Link, you only have {player[last_player]["inventory"]["lives"]} hearts')
            if map_data[y_pos - 1][x_pos] == "F" or map_data[y_pos + 1][x_pos] == "F" or map_data[y_pos][x_pos - 1] == "F" or map_data[y_pos][x_pos + 1] == "F":
                for element in elements:
                    if element["symbol"] == "F":
                        fox_x_pos, fox_y_pos = element["x"], element["y"]
                        break
                map_data[fox_x_pos][fox_y_pos] = " "
                print("You got meat")
                player[last_player]["food"]["meat"]["count"] += 1
            elif map_data[y_pos - 1][x_pos] == "T" or map_data[y_pos + 1][x_pos] == "T" or map_data[y_pos][x_pos - 1] == "T" or map_data[y_pos][x_pos + 1] == "T":
                if player[last_player]["inventory"]["weapon1"] == "":
                    numero_aleatorio = random.random()
                    if numero_aleatorio <= 0.4 and numero_aleatorio >= 0.1:
                        player[last_player]["food"]["vegetable"]["count"] += 1
                        print("You got an apple")
                    elif numero_aleatorio < 0.1:
                        drops = ["wood sword", "wood shield"]
                        item = random.choice(drops)
                        player[last_player]["weapons"][item][count] += 1
                        print(f"You got a {item}")
            elif "E" in map_data[y_pos - 1][x_pos] or "E" in map_data[y_pos + 1][x_pos] or "E" in map_data[y_pos][x_pos - 1] or "E" in map_data[y_pos][x_pos + 1]:
                for element in elements:
                    if element["symbol"] == "E":
                        en_x_pos, en_y_pos = element["x"], element["y"]
                        if map_data[en_y_pos - 1][en_x_pos] == "X" or map_data[en_y_pos + 1][en_x_pos] == "X" or map_data[en_y_pos][en_x_pos - 1] == "X" or map_data[en_y_pos][en_x_pos + 1] == "X":
                            element["life"] -= 1
                            if element["life"] < 1:
                                map_data[en_y_pos][en_x_pos] = " "
                            position_valid = False
                            while not position_valid:
                                valid_position = [" "]
                                directions = ["up", "right", "down","left"]
                                direction = random.choice(directions)
                                new_en_x_pos = en_x_pos + (1 if direction == "right" else -1) if direction in ["left", "right"] else en_x_pos
                                new_en_y_pos = en_y_pos + (1 if direction == "down" else -1) if direction in ["up", "down"] else en_y_pos 
                                if map_data[new_en_y_pos][new_en_x_pos] in valid_position:
                                    position_valid = True
                                else:
                                    continue
                            element["x"], element["y"] = new_en_x_pos, new_en_y_pos
                            print("Brave, keep fighting Link")
            else:
                numero_aleatorio = random.random()
                if numero_aleatorio < 0.1:
                    print("You got a lizard")
                    player[last_player]["food"]["meat"]["count"] += 1
                else:
                    print("You did not anything")



### FUNCION PARA ABRIR COFRES ###   

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
        
                            
def open(map_data, elements, place, map_name):
    if place.capitalize() == "Sanctuary":
        for element in elements:
            if element["name"] == "Sanctuary":
                x_pos, y_pos = element["x"], element["y"]
                if map_data[y_pos - 1][x_pos] == "X" or map_data[y_pos + 1][x_pos] == "X" or map_data[y_pos][x_pos - 1] == "X" or map_data[y_pos][x_pos + 1] == "X":
                    sanctuary = element["symbol"].replace("?","")
                    if player[last_player]["sanctuaries"][sanctuary]["opened"]:
                        print('You already opened this sanctuary')
                    else:
                        player[last_player]["sanctuaries"][sanctuary]["name"] = sanctuary
                        player[last_player]["sanctuaries"][sanctuary]["opened"] = True
                        player[last_player]["sanctuaries"][sanctuary]["map"] = map_name  # Guarda el nombre del mapa actual
                        player[last_player]["inventory"]["max_lives"] += 1
                        print('You opened the sanctuary, your maximum health has increased by 1')
                        element["symbol"] = sanctuary  # Update the sanctuary name in the elements list

    elif place.capitalize() == "Chest":
        for element in elements:
            if element["symbol"] == "M":
                x_pos, y_pos = element["x"], element["y"]
                if map_data[y_pos - 1][x_pos] == "X" or map_data[y_pos + 1][x_pos] == "X" or map_data[y_pos][x_pos - 1] == "X" or map_data[y_pos][x_pos + 1] == "X":
                    map_swords = ["Hyrule", "Gerudo"]
                    map_shields = ["Death mountain", "Necluda"]
                    if map_name in map_swords:
                        swords = ["sword", "wood sword"]
                        item = random.choice(swords)
                        player[last_player]["weapons"][item]["count"] += 1
                        print(f"You obtained a {item}")
                    elif map_name in map_shields:
                        shields = ["shield", "wood shield"]
                        item = random.choice(shields)
                        player[last_player]["weapons"][item]["count"] += 1
                        print(f"You obtained a {item}")
                    element["symbol"] = "W"
                    element["opened"] = True  # Marca el cofre como abierto
                else:
                    print("This chest has alredy been opened")


## Definir las conexiones entre los mapas
map_connections = {
    "Hyrule": ["Gerudo", "Death mountain", "Castle"],
    "Death mountain": ["Hyrule", "Necluda", "Castle"],
    "Gerudo": ["Hyrule", "Necluda", "Castle"],
    "Necluda": ["Death mountain", "Gerudo", "Castle"],
    "Castle": ["Hyrule", "Death mountain", "Gerudo", "Necluda"]  # Add this line
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




### Logica del Juego ###
def game_logic():
    
    global current_map
    global current_inventory
    directions = ["up", "down", "left", "right"]
    while True:
        # Get the keys from the player dictionary
        jugadores = player.keys()

        # Get the last player added to the dictionary
        ultimo_jugador = list(jugadores)[-1]

        # Check if player is dead
        if player[ultimo_jugador]['inventory']['lives'] <= 0:
            deadMenu()
            break
        print_map(maps[current_map]["map"], maps[current_map]["elements"], player, current_inventory, map_name=current_map)
        
        while True:
            command = input("What to do now? ").lower().split()
            if command[0] == "show" and command[1] == "map":
                # Display the map and the inventory
                inventoryMain(player, player_name)
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
                        print(f"You can't show {new_inventory} inventory.")
                        continue

            if command[0] == "go" and command[1] == "to":
                # Cambiar de mapa
                new_map = " ".join(command[2:]).capitalize()
                if new_map in map_connections[current_map]:
                    current_map = new_map
                    break
                else:
                    print(f"You can't go to {new_map} from {current_map}.")
                    continue
            if command[0] == "go" and command[1] == "by":
                go_by(command[2], maps[current_map]["map"], maps[current_map]["elements"])
                break

            if command[0] == "go" and command[1] in directions:
                direction = command[1]
                try:
                    num_steps = int(command[2])
                except ValueError:
                    print("You can't go there, it's not a valid position")
                    continue

                if move_player(maps[current_map]["map"], maps[current_map]["elements"], direction, num_steps):
                    timeblood(maps[current_map]["elements"], player, ultimo_jugador)

                    break
                else:
                    print("You can't go there, it's not a valid position")

            if command[0] == "attack":
                attack(maps[current_map]["map"], maps[current_map]["elements"])
                break
            
            
            ### ESTO DEBERIA DE ABRIR LOS COFRES ##
            if command[0] == "open" and command[1] == "chest":
                open(maps[current_map]["map"], maps[current_map]["elements"], "Chest", current_map)
                break
            
            ### ABRIR SANTUARIO ###
            if command[0] == "open" and command[1] == "sanctuary":
                open(maps[current_map]["map"], maps[current_map]["elements"], "Sanctuary", current_map)
                break
            ### cocinar ###
            if command[0] == "cook":
                if len(command) < 2:
                    print("You need to specify what you want to cook.")
                    continue
                item_to_cook = command[1]
                cook(maps[current_map]["map"], maps[current_map]["elements"], item_to_cook, last_player)
                break
             ### comer ###
            if command[0] == "eat":
                if len(command) < 2:
                    print("You need to specify what you want to eat.")
                    continue
                item_to_eat = command[1]
                
                eat(item_to_eat)
                print(player)
                break

                
game_logic()