
import os
from funciones import player
x = "X"


last_player = list(player.keys())[-1]
sanctuary_value0 = player[last_player]["sanctuaries"]["S0"]["name"]
sanctuary_value1 = player[last_player]["sanctuaries"]["S1"]["name"]
hyrule = [
    f"\n* Hyrule  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
    f"\n*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *",
    f"\n*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *",
    f"\n*                  C                      ~~~~~~    ~~~~~~*                   *",
    f"\n*    T                                                 ~~~*                   *",
    f"\n*                                 E9                      *                   *",
    f"\n*                                          {sanctuary_value0}            *                   *",
    f"\n*                                                         *                   *",
    f"\n*          !{x}                                   T         *                   *",  # La X es el personaje (cambiar posiblemente)
    f"\n* OO    OOOOO       E1        {sanctuary_value1}             T M   F     *                   *",
    f"\n*OOOOOOOOOOO                                              *                   *",
    f"\n* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * *"
]

# Utiliza el método replace y asigna el resultado a la posición 0 de hyrule
#hyrule[0] = hyrule[0].replace(hyrule[0][1], "X")
#print(hyrule[0])

lp = True
while lp:
    sistema_operativo = os.name
    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':
        os.system('cls')
    print("".join(hyrule))
    direction = input("Enter the direction to move (up, down, left, right): ")



    if direction == "up":
        for i in range(len(hyrule)):
            if x in hyrule[i]:
                pos = hyrule[i].find("X")
                if hyrule[i-1][pos] != " " or hyrule[i-1] == hyrule[0]:
                    input("You can't go there")
                else:
                    hyrule[i] = hyrule[i].replace("X", " ")
                    linea_anterior = hyrule[i-1]
                    linea_anterior_modificada = linea_anterior[:pos] + x + linea_anterior[pos + 1:]
                    hyrule[i-1] = linea_anterior_modificada
                break
    elif direction == "down":
        for i in range(len(hyrule)):
            if x in hyrule[i]:
                pos = hyrule[i].find("X")
                if hyrule[i+1][pos] != " " or hyrule[i+1] == hyrule[11]:
                    input("You can't go there")
                else:
                    hyrule[i] = hyrule[i].replace("X", " ")
                    linea_anterior = hyrule[i+1]
                    linea_anterior_modificada = linea_anterior[:pos] + x + linea_anterior[pos + 1:]
                    hyrule[i+1] = linea_anterior_modificada
                break
    elif direction == "left":
        for i in range(len(hyrule)):
            if x in hyrule[i]:
                pos = hyrule[i].find("X")
                
                if hyrule[i][pos-1] != " " or hyrule[i][pos-1] == hyrule[i][0]:
                    input("You can't go there")
                else:
                    hyrule[i] = hyrule[i].replace("X", " ")
                    linea_anterior = hyrule[i]
                    linea_anterior_modificada = linea_anterior[:pos-1] + x + linea_anterior[pos:]
                    hyrule[i] = linea_anterior_modificada
                break
    elif direction == "right":
        for i in range(len(hyrule)):
            if x in hyrule[i]:
                pos = hyrule[i].find("X")
                
                if hyrule[i][pos+1] != " " or hyrule[i][pos+1] == hyrule[i][59]:
                    input("You can't go there")
                else:
                    hyrule[i] = hyrule[i].replace("X", " ")
                    linea_anterior = hyrule[i]
                    linea_anterior_modificada = linea_anterior[:pos+1] + x + linea_anterior[pos+2:]
                    hyrule[i] = linea_anterior_modificada
                break
