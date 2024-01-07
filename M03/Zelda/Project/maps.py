
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

    move_player()