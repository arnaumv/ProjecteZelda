
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
    "hyrule" : [
        f"\n* Hyrule  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *",
        f"\n*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *",
        f"\n*                  C                      ~~~~~~    ~~~~~~*                   *",
        f"\n*    T                                                 ~~~*                   *",
        f"\n*                                 E9                      *                   *",
        f"\n*                                          {sanctuary_value0}            *                   *",
        f"\n*                                                         *                   *",
        f"\n*           {x}                                   T         *                   *",  # La X es el personaje (cambiar posiblemente)
        f"\n* OO    OOOOO       E1        {sanctuary_value1}             T M   F     *                   *",
        f"\n*OOOOOOOOOOO                                              *                   *",
        f"\n* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * *"
    ],
    "death mountain" : [
        f"\n* Death Mountain  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n* O                OOOO                                   *                   *",
        f"\n* O                 OOOO      F                           *                   *",
        f"\n* ~~  {sanctuary_value2}            OOOO                          E2     *                   *",
        f"\n* ~~~        E2      OOOO      OOOO                       *                   *",
        f"\n* O~~~~~~~~            OOOO  OO    OOOOOOOO               *                   *",
        f"\n* ~~~~~~~~~             OOOOOO           OOOO             *                   *",
        f"\n*    ~~~           T        OOOO           OO             *                   *",
        f"\n*                 T          OO     M                     *                   *",
        f"\n* {x}   C           T          OO                  {sanctuary_value3}      *                   *",
        f"\n*                                                         *                   *",
        f"\n* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * *"  
    ],
    "gerudo" : [
        f"\n* Gerudo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*OOOOOOOOOOOOOOOO                                   M     *                   *",
        f"\n*  OOOOO  OOOOO              TTT                          *                   *",
        f"\n*                              TT             {sanctuary_value4}         O*                   *",
        f"\n*  E1          C                                        OO*                   *",
        f"\n*                                                       OO*                   *",
        f"\n*             AAAAAA                  E2                  *                   *",
        f"\n*             AAAAAAAA                                    *                   *",
        f"\n*    T       AAAAAAA                 OOOOO      F       ~~*                   *",
        f"\n* {x}     M      AAA        OOOOO    OOOOO              ~~~~*                   *",
        f"\n* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * *"
    ],
    "necluda" : [
        f"\n* Necluda * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*                     M                                   *                   *",
        f"\n* !       E1                         TT            M      *                   *",
        f"\n*OO                C               TT                ~~~~~*                   *",
        f"\n*OOOOO                                           ~~~~~~~~~*                   *",
        f"\n*OOOO                                              ~~~~~~~*                   *",
        f"\n*              T                      E2           {sanctuary_value5}~~~~~*                   *",
        f"\n*     F       T9                                ~~~~~~~~~~*                   *",
        f"\n*~~            T6                                  ~~~~~~~*                   *",
        f"\n*~~~~~~~~              M         {sanctuary_value6}          ~~~~~~~~~~~~~*                   *",
        f"\n*~~~~~~~~~~~~                           ~~~~~~~~~~~~~~~~~~*                   *",
        f"\n* Exit, Attack, Go, Equip, Unequip, Eat, Cook, Fish, Open * * * * * * * * * * *"
    ]
}

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