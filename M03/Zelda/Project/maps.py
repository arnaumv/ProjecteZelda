
import os
from funciones import player
from funciones import * 
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
invalid_positions = ["*", "T", "F", "C", "O","~"]  # Add other invalid positions here

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


    for _ in range(num_steps):
        if direction == "up":
            for i in range(len(hyrule)):
                if x in hyrule[i]:
                    pos = hyrule[i].find("X")
                    if hyrule[i-1][pos] in invalid_positions or hyrule[i-1] == hyrule[0]:
                        input("You can't go there, is not a valid position")
                        break
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
                    if hyrule[i+1][pos] in invalid_positions or hyrule[i+1] == hyrule[11]:
                        input("You can't go there, is not a valid position")
                        break
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
                    if hyrule[i][pos-1] in invalid_positions or hyrule[i][pos-1] == hyrule[i][0]:
                        input("You can't go there, is not a valid position")
                        break
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
                    if hyrule[i][pos+1] in invalid_positions or hyrule[i][pos+1] == hyrule[i][59]:
                        input("You can't go there, is not a valid position")
                        break
                    else:
                        hyrule[i] = hyrule[i].replace("X", " ")
                        linea_anterior = hyrule[i]
                        linea_anterior_modificada = linea_anterior[:pos+1] + x + linea_anterior[pos+2:]
                        hyrule[i] = linea_anterior_modificada
                    break