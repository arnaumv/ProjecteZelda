
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
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 19, "y" :7},]  
    }
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
        player[last_player]["inventory"]["timeBlood"] -= 1
        break
    if player[last_player]["inventory"]["timeBlood"] == 0:
        for element in elements:
            if element["symbol"] == "E":
                element["life"] = element["max_life"]
    return


#Funcion para moverse por el mapa
    

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
                

#Funcion para pescar

def fish(map_data, elements):
    for element in elements:
        if element["symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
        
        if map_data[y_pos + 1][x_pos] == "C" or map_data[y_pos - 1][x_pos] == "~" or map_data[y_pos][x_pos + 1] == "~" or map_data[y_pos][x_pos - 1] == "~" and "pescar" == True:
            numero_aleatorio = random.random()
            if numero_aleatorio < 0.2:
                promptAfegir("You got a fish")
                player[last_player]["food"]["fish"]["count"] += 1
                return
            else:
                promptAfegir("You didn't get a fish")
                return

#Funciones para los cofres y los santuarios

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
                    player[last_player]["sanctuaries"][sanctuary]["name"] = sanctuary
                    player[last_player]["sanctuaries"][sanctuary]["opened"] = True
                    player[last_player]["sanctuaries"][sanctuary]["map"] = map_name  # Guarda el nombre del mapa actual
                    player[last_player]["inventory"]["max_lives"] += 1
                    print(f"You opened {sanctuary}")

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

def attack(map_data, elements):
    for element in elements:
        if element["Symbol"] == "X":
            x_pos, y_pos = element["x"], element["y"]
            if map_data[y_pos - 1][x_pos] == "F" or map_data[y_pos + 1][x_pos] == "F" or map_data[y_pos][x_pos - 1] == "F" or map_data[y_pos][x_pos + 1] == "F":
                for element in elements:
                    if element["symbol"] == "F":
                        fox_x_pos, fox_y_pos = element["x"], element["y"]
                        break
                map_data[fox_x_pos][fox_y_pos] = " "
                promptAfegir("You got meat")
                player[last_player]["food"]["meat"]["count"] += 1
            elif map_data[y_pos - 1][x_pos] == "T" or map_data[y_pos + 1][x_pos] == "T" or map_data[y_pos][x_pos - 1] == "T" or map_data[y_pos][x_pos + 1] == "T":
                if player[last_player]["inventory"]["weapon1"] == "":
                    numero_aleatorio = random.random()
                    if numero_aleatorio <= 0.4 and numero_aleatorio >= 0.1:
                        player[last_player]["food"]["vegetable"]["count"] += 1
                        promptAfegir("You got an apple")
                    elif numero_aleatorio < 0.1:
                        drops = ["wood sword", "wood shield"]
                        item = random.choice(drops)
                        player[last_player]["weapons"][item][count] += 1
                        promptAfegir(f"You got a {item}")
            elif "E" in map_data[y_pos - 1][x_pos] or "E" in map_data[y_pos + 1][x_pos] or "E" in map_data[y_pos][x_pos - 1] or "E" in map_data[y_pos][x_pos + 1]:
                for element in elements:
                    if element["symbol"] == "E":
                        en_x_pos, en_y_pos = element["x"], element["y"]
                        if map_data[en_y_pos - 1][en_x_pos] == "X" or map_data[en_y_pos + 1][en_x_pos] == "X" or map_data[en_y_pos][en_x_pos - 1] == "X" or map_data[en_y_pos][en_x_pos + 1] == "X":
                            element["life"] -= 1
                            if element["life"] < 1:
                                map_data[en_y_pos][en_x_pos] = " "
                            player[last_player]["inventory"]["lives"] -= 1
                            promptAfegir(f"Be careful Link, you only have {player[last_player]["inventory"]["lives"]} hearts")
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
                            promptAfegir("Brave, keep fighting Link")
            else:
                numero_aleatorio = random.random()
                if numero_aleatorio < 0.1:
                    promptAfegir("You got a lizard")
                    player[last_player]["food"]["meat"]["count"] += 1
                else:
                    promptAfegir("You did not anything")
                        
def ganon(elements):
    sentences = [
    "Ganon is powerful, are you sure you can defeat him?",
    "Ganon's strength is supernatural, Zelda fought with bravery.",
    "To Ganon, you are like a fly, find a weak spot and attack.",
    "Ganon will not surrender easily.",
    "Ganon has fought great battles, is an expert fighter.",
    "Link, transform your fears into strengths.",
    "Keep it up, Link, Ganon can't hold out much longer.",
    "Link, history repeats itself, Ganon can be defeated.",
    "Think of all the warriors who have tried before.",
    "You fight for the weaker ones, Link, persevere."
    ]
    if maps["Castle"]["map"][8][18] == "X" or maps["Castle"]["map"][8][19] == "X" or maps["Castle"]["map"][8][20] == "X":
        attack = True
    if not attack:
        promptAfegir("You are not close enough to ganon to attack")
    else:
        sentence = random.choice(sentences)
        promptAfegir(sentence)
        maps["Castle"]["elements"][1]["lifes"] -= 1
        player[last_player]["inventory"]["lives"] -= 1
        if maps["Castle"]["elements"][1]["lifes"] < 1:
            promptAfegir("You have defeated Ganon.")
            return
        
    

