from funciones import *
import os

def clear_terminal():
    if os.name == 'nt':  # Para sistemas Windows
        _ = os.system('cls')
    else:  # Para sistemas Unix/Linux/MacOS
        _ = os.system('clear')

###################################   MENU PRINCIPAL    ############################################
def menu1():
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             ##              * "
        "\n *                                                             ##              * "
        "\n *                                                          ##~~~              * "
        "\n *                                                          ##~~~O             * "
        "\n *    Zelda, Breath of the Wild                            ###~~~ \            * "
        "\n *                                                           |@@@| \           * "
        "\n *                                                           |   |  \          * "
        "\n *                                                           =   ==            * "
        "\n *                                                       %%%%%%%%%%%%          * "
        "\n *                                                    %%%%%%%%%%%%%%%          * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )

def menu2():
     print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             &&              * "
        "\n *                                                            oo &             * "
        "\n *                                                    $       -- &##           * "
        "\n *                                                    $$    <<OO####           * "
        "\n *    Zelda, Breath of the Wild                        $$  //OOO####           * "
        "\n *                                                      $$// OO#####           * "
        "\n *                                                       **  OOO###            * "
        "\n *                                                        &  @@@@\             * "
        "\n *                                                            Q  Q             * "
        "\n *                                                            Q  Q             * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )

def menu3():
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             &&              * "
        "\n *                                                            ####             * "
        "\n *                                                           ||                * "
        "\n *                                                        @@@@@@@@@@@@         * "
        "\n *    Zelda, Breath of the Wild                          @     ||@@@           * "
        "\n *                                                             |@@@            * "
        "\n *                                                            @@@              * "
        "\n *                                                         @@@@||     @        * "
        "\n *                                                      @@@@@@@@@@@@@          * "
        "\n *                                                             ||              * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )



#############################################################################################################


#########################################   HELP, MAIN MENU    ##############################################


def helpMainMenu():
     print("* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                                             * "
        "\n *                                                                             * "
        "\n *                 Type 'continue' to continue a saved game                    * "
        "\n *                 Type 'new game' to start a new game                         * "
        "\n *                 Type 'about' to see information about the game              * "
        "\n *                 Type 'exit' to exit the game                                * "
        "\n *                                                                             * "
        "\n *                 Type 'back' now to go back to the 'Main menu'               * "
        "\n *                                                                             * "
        "\n *                                                                             * "
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "
    )



#########################################   SAVED GAMES, MENU    ##############################################
                                                                                                              #
def savedGamesMenu():                                                                                         #
     print("* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n * Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
    )                                                                                                         #
                                                                                                              #
                                                                                                              #
#########################################   HELP SAVED GAMES, MENU    #########################################
                                                                                                              #
def helpSavedGamesMenu():                                                                                     #
     print("* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                  Type 'play X' to continue playing the game 'X'             * "                 #
        "\n *                  Type 'erase X' to erase the game 'X'                       * "                 #
        "\n *                  Type 'back' now to go back to the main menu                * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                  Type 'back' now to go back to 'Saved games'                * "                 #
        "\n *                                                                             * "                 #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                 #
    )                                                                                                         #
                                                                                                              #
###############################################################################################################



#########################################   NEW GAME, MENU    ##################################################
                                                                                                               
                                                                                                               
def newGameMenu():
    clear_terminal()

    print(" * New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                  Set your name ?                                            * "
          "\n *                                                                             * "
          "\n *                  Type 'back' now to go back to 'Main Menu'                  * "
          "\n *                                                                             * "
          "\n * Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    )

    while True:
        player_name = input("What's your name (Link)? ").strip()  # Elimina espacios al inicio y final

        if player_name.lower() == 'back':
            mostrar_menu_aleatorio()
            prompt_usuari()
            break

        # Verificar si se ha ingresado un nombre
        if not player_name:
            player_name = 'Link'  # Asignar 'Link' si no se ingresa un nombre

        # Verificar validez del nombre
        if player_name.isalnum() or ' ' in player_name:
            # Validar que solo contiene letras, números y espacios
            print(f"Welcome to the game, {player_name}")
            # Ir a la sección 'Legend'
            legendMenu(player_name)  # Pasar player_name a legendMenu()
            break
        else:
            print(f'"{player_name}" is not a valid name')   
            
                                                                                                                 
                                                                                                               
#########################################   HELP NEW GAME, MENU    #############################################
                                                                                                               #     
                                                                                                               #
def helpNewGameMenu():                                                                                             #
     print("* Help, New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                   #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *       When asked, type your name and press enter                            * "                  #
        "\n *       if 'Link' is fine for you, just press enter                           * "                  #
        "\n *                                                                             * "                  #
        "\n *       Name must be between 3 and 10 characters long and only                * "                  #
        "\n *       letters, numbers and spaces are allowed                               * "                  #
        "\n *                                                                             * "                  #
        "\n *       Type 'back' now to go back to 'Set Your Name'                         * "                  #
        "\n *                                                                             * "                  #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                  #
    )                                                                                                          #
                                                                                                               #
################################################################################################################
     


##############################################  ABOUT, MENU    ##################################################
                                                                                                                #
def aboutMenu():                                                                                                #
     print("* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                    #
        "\n *                                                                             * "                   #
        "\n *       Game developed by ‘Team 2, The hometown bugs’ :                       * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n *             Arnau Mestre                                                    * "                   #
        "\n *             Adria Martinez                                                  * "                   #
        "\n *             Moha  El Amine                                                  * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                   #
    )                                                                                                           #
                                                                                                                #
#################################################################################################################
     

##############################################  LEGEND, MENU    #################################################
                                                                                                                
def legendMenu(player_name):
        clear_terminal()
        print(" * Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
              "\n *    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah * "
              "\n *    tribe. The Sheikah were a tribe of warriors who protected the Triforce, * "
              "\n *    a sacred relic that granted wishes.                                     * "
              "\n *                                                                            * "
              "\n *    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began  * "
              "\n *    to rule Hyrule with an iron fist.                                       * "
              "\n *                                                                            * "
              "\n *    The princess, with the help of a heroic young man, managed to defeat    * "
              "\n *    Ganondorf and recover the Triforce.                                     * "
              "\n *                                                                            * "
              "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        )

        while True:
            user_input = input("Type 'continue' to continue: ")

            if user_input.lower() == 'continue':
                
                plotMenu(player_name)
                break
            else:
                print("Invalid action.")

#################################################################################################################
     



################################################  PLOT, MENU    #################################################
                                                                                                                
def plotMenu(player_name):
    clear_terminal()

    print(" * Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
          "\n *                                                                            * "
          "\n *                                                                            * "
         f"\n *   Now history is repeating itself, and Princess Zelda has been captured by * "
          "\n *   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  * "
          "\n *                                                                            * "
          "\n *                                                                            * "
          f"\n *   But a young man named '{player_name}' has just awakened and                        * "
          "\n *   must reclaim the Guardians to defeat Ganon and save Hyrule.              * "
          "\n *                                                                            * "
          "\n *                                                                            * "
          "\n * Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    )
    while True:
        user_input = input("Type 'continue' to continue: ")

        if user_input.lower() == 'continue':
            print("The adventure begins")
            # Start the game section
            break
        
        else:
            print("Invalid action")
                                                                                                          
#################################################################################################################



################################################  DEAD    #######################################################
                                                                                                                
def deadMenu():                                                                                                 
     print("* Link Dead  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *      Game Over                                                             * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    
    )

#################################################################################################################



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
foods = [1, 2, 0, 0, 0, 2]



def rellenarEspacios(string):
    spaces = 79 - len(string)
    if spaces > 0:
        string += " " * spaces
    elif spaces < 0:
        string = string[:79]
    string += "*"
    return string

def showingMain(player_name, playerInfo):
    inventory = [
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * Inventory *",
        f"\n*                                                         * {player_name}  ♥ {playerInfo[0]}/{playerInfo[1]}",
        f"\n*                                                         * Blood moon in {playerInfo[2]}",
        f"\n*                                                         *                   *",
        f"\n*                                                         * Equipment         *",
        f"\n*                                                         *       {playerInfo[3]} ",
        f"\n*                                                         *       {playerInfo[4]} ",
        f"\n*                                                         *                   *",
        f"\n*                                                         * Food            {playerInfo[5]} ",
        f"\n*                                                         * Weapons         {playerInfo[6]} ",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    inventory = [rellenarEspacios(line) for line in inventory]
    print("".join(inventory))
    
    
    
    
# Funcion que imprime el inventario -- Weapons
def showingWeapons(uses, count, equipped):
    inventory = [
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * Weapons *",
        f"\n*                                                         *                   *",
        f"\n*                                                         *                   *",
        f"\n*                                                         * Wood Sword    {uses[0]}/{count[0]}  *",
        f"\n*                                                         * {equipped[0]}   ",
        f"\n*                                                         * Sword         {uses[1]}/{count[1]}  *",
        f"\n*                                                         * {equipped[1]}        ",
        f"\n*                                                         * Wood Shield   {uses[2]}/{count[2]} *",
        f"\n*                                                         * {equipped[2]}        ",
        f"\n*                                                         * Shield        {uses[3]}/{count[3]} *",
        f"\n*                                                         * {equipped[3]}       ",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    inventory = [rellenarEspacios(line) for line in inventory]
    print("".join(inventory))
    
    
def showingFoods(foods):
    inventory = [
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * Foods *",
        f"\n*                                                         *                   *",
        f"\n*                                                         *                   *",
        f"\n*                                                         * Vegetables    {foods[0]} ",
        f"\n*                                                         * Fish          {foods[1]} ",
        f"\n*                                                         * Meat          {foods[2]} ",
        f"\n*                                                         *                   *",
        f"\n*                                                         * Salads        {foods[3]} ",
        f"\n*                                                         * Pescatarian   {foods[4]} ",
        f"\n*                                                         * Roasted       {foods[5]} ",
        f"\n*                                                         *                   *",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    inventory = [rellenarEspacios(line) for line in inventory]
    print("".join(inventory))

def showAllInventory(player_name, playerInfo, uses , count, equipped, foods):
    inventory = [
        f"\n* * * * * Inventory * * * * * * Weapons * * * * * *  Food *",
        f"\n* {player_name.ljust(12)}♥{str(playerInfo[0]).rjust(2)}/{str(playerInfo[1])} * {''.ljust(17)} * {''.ljust(15)} *", 
        f"\n* {''.ljust(17)} * Wood Sword    {uses[0]}/{count[0]} * Vegetables    {foods[0]} *",
        f"\n* Equipment         * {equipped[0].ljust(17)} * Fish          {foods[1]} *",
        f"\n*    {playerInfo[3].rjust(14)} * Sword         {uses[1]}/{count[1]} * Meat          {foods[2]} *",
        f"\n*    {playerInfo[4].rjust(14)} * {equipped[1].ljust(17)} *                 *",
        f"\n* {''.ljust(17)} * Wood Shield   {uses[2]}/{count[2]} * Salads        {foods[3]} *",
        f"\n* Food           {str(playerInfo[5]).rjust(2)} * {equipped[2].ljust(17)} * Pescatarian   {foods[4]} *",
        f"\n* Weapons        {str(playerInfo[6]).rjust(2)} * Shield        {uses[3]}/{count[3]} * Roasted       {foods[5]} *",
        f"\n* {''.ljust(17)} * {equipped[3].ljust(17)} *                 *",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    print("".join(inventory))

def map(santuarios):
    map = [
        f"\n* Map * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*                                                         *                   *",
        f"\n*  Hyrule        {str(santuarios[0]).rjust(3)}                       Death Mountain *                   *",
        f"\n*                                 {str(santuarios[2]).rjust(3)}                     *                   *",
        f"\n*        {str(santuarios[1]).rjust(3)}                                    {str(santuarios[3]).rjust(3)}       *                   *",
        f"\n*                                                         *                   *",
        f"\n*                         Castle                          *                   *",
        f"\n*                                                         *                   *",
        f"\n*                {str(santuarios[4]).rjust(3)}                                 {str(santuarios[5]).rjust(3)}  *                   *",
        f"\n*  Gerudo                             {str(santuarios[6]).rjust(3)}        Necluda  *                   *",
        f"\n*                                                         *                   *",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    print("".join(map))

def juntarInfo(santuarios, foods):
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

def separarWeapons(equipment):
    uses = []
    count = []
    equipped = []

    for i in equipment:
        uses.append(i["uses"])
        count.append(i["count"])
        if i["equipped"] == True:
            equipped.append("  (equipped)")
        else:
            equipped.append("")
    return uses, count, equipped

def separarFood(foods):
    count = []
    hearts = []

    for i in foods:
        count.append(i["count"])
        hearts.append(i["hearts"])
    return count, hearts

def separarSantuarios(player_name):
    santuarios = []

    for clave, i in player[player_name]["sanctuaries"].items():
        if i == True:
            santuarios.append(clave + "?")
        else:
            santuarios.append(clave)
    return santuarios

def separarPlayer(equipment):
    listas = [[], [], [], []]  

    for clave,i in equipment.items():
        count = -1    

        for j in i.values():
            count += 1
            for k in j.values():
                listas[count].append(k)

    return clave, listas




