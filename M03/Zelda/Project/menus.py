from funciones import *
import os
import pymysql
from datetime import datetime
from consultas import *
#conn = pymysql.connect(host="localhost", user="root", password="root", db="Zelda")
#cur = conn.cursor()

def clear_terminal():
    if os.name == 'nt':  # Para sistemas Windows
        _ = os.system('cls')
    else:  # Para sistemas Unix/Linux/MacOS
        _ = os.system('clear')




###################################   MENU PRINCIPAL    ############################################

def gameMenu():
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
        "\n * New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * * * * * * * "
    )

def gameMenu2():
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
        "\n * New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * * * * * * * "
    )

def gameMenu3():
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
        "\n * New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * * * * * * * "
    )


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
        "\n * Continue, New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * *"
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
        "\n * Continue, New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * *"
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
        "\n * Continue, New Game, Help, About, Exit, Reports  * * * * * * * * * * * * * * *"
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
def savedGamesMenu():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root", db="Zelda")
        cur = conn.cursor()

        while True:
            # Query para seleccionar los valores específicos de la tabla game
            select_query = "SELECT game_id,user_name, date_started, hearts_remaining, region FROM game ORDER BY date_started DESC"
            cur.execute(select_query)

            # Obtener los resultados
            resultados = cur.fetchall()

            games = ["".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74), "".ljust(74)]

            # Construir el formato para mostrar los juegos
            for i in range(len(resultados)):
                max_lives_last_player = 3
                games[i] = (f'{i+1}: {resultados[i][1]} - {resultados[i][2]}, {resultados[i][4]}'.ljust(69) + f'♥ {resultados[i][3]}/{max_lives_last_player}')

            show_games = [
                f"\n * Saved Games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
                f"\n *                                                                             *",
                f"\n * {games[0]}  *",
                f"\n * {games[1]}  *",
                f"\n * {games[2]}  *",
                f"\n * {games[3]}  *",
                f"\n * {games[4]}  *",
                f"\n * {games[5]}  *",
                f"\n * {games[6]}  *",
                f"\n * {games[7]}  *",
                f"\n *                                                                             *",
                f"\n * Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * * *"
            ]
            print("".join(show_games))

            # Solicitar al usuario que introduzca una acción
            action = input("What to do now: ")

            # Si la acción es "Erase X", eliminar la fila correspondiente de la base de datos
            if action.lower().startswith("erase "):
                id_to_erase = int(action.split(" ")[1]) - 1  # Restamos 1 porque los índices en Python empiezan en 0
                delete_user = "DELETE FROM game WHERE user_name = %s"
                cur.execute(delete_user, (resultados[id_to_erase][1],))
                conn.commit()
            elif action.lower() == "help":
                helpSavedGamesMenu()
            elif action.lower() == "back":
                from funciones import mostrar_menu_aleatorio, prompt_usuari
                mostrar_menu_aleatorio()
                prompt_usuari()
                break
            else:
                print("Invalid option. Please try again.")

        cur.close()
        conn.close()
    except pymysql.Error as e:
        print(f"Error: {e}")

        
#########################################   HELP SAVED GAMES, MENU    #########################################
                                                                                                              
def helpSavedGamesMenu():    
    clear_terminal()                                                                                 
    print("* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n *                  Type 'play X' to continue playing the game 'X'             * "                 
        "\n *                  Type 'erase X' to erase the game 'X'                       * "                 
        "\n *                  Type 'back' now to go back to the main menu                * "                 
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n *                  Type 'back' now to go back to 'Saved games'                * "                 
        "\n *                                                                             * "                 
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                 
    ) 

    while True:
        action = input("What to do now: ")

        if action.lower() == "back":
            clear_terminal()
            savedGamesMenu()
            
            break
        else:
            print("Invalid option. Please try again.")                                                                                                       
                                                                                                              
###############################################################################################################


   



#########################################   NEW GAME, MENU    ##################################################
player_name = 'Link'    ##prueba###                                                                                                           
current_player_name = None
                                                                                                              


def newGameMenu():
    global current_player_name
    from funciones import player

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
            from funciones import mainMenu  # Importación local
            mainMenu()
            break

        # Verificar si se ha ingresado un nombre
        if not player_name:
            player_name = 'Link'  # Asignar 'Link' si no se ingresa un nombre

        # Verificar validez del nombre
        if player_name.isalnum() or ' ' in player_name:

            # Validar que solo contiene letras, números y espacios
            print(f"Welcome to the game, {player_name}")
            
            current_player_name = player_name  # Asignar el valor a la variable global

            # Guardo informacion del juagdor en el diccionario player para poder usarlo en otras funciones durante la partida
            new_player_data = {
                "inventory": {
                    "lives": 3,
                    "max_lives": 3,
                    "timeBlood": 25,
                    "weapon1": "Wood Sword",
                    "weapon2": "Wood Shield",
                    "totalFood": 0,
                    "totalWeapons": 2,
                    "openedchest": 0,  

                },
                "weapons": {
                    "wood sword": {"uses": 5, "count": 2, "equipped": True},
                    "sword": {"uses": 9, "count": 1, "equipped": False},
                    "wood shield": {"uses": 5, "count": 1, "equipped": True},
                    "shield": {"uses": 9, "count": 0, "equipped": False}
                },
                "food": {
                    "vegetables": {"count": 5, "hearts": 1},
                    "fish": {"count": 2, "hearts": 0},
                    "meat": {"count": 2, "hearts": 0},
                    "salads": {"count": 2, "hearts": 2},
                    "pescatarian": {"count": 1, "hearts": 3},
                    "roasted": {"count": 1, "hearts": 4}
                },
                "sanctuaries": {
                    "S0": {"name": "S0?", "opened": False},
                    "S1": {"name": "S1?", "opened": False},
                    "S2": {"name": "S2?", "opened": False},
                    "S3": {"name": "S3?", "opened": False},
                    "S4": {"name": "S4?", "opened": False},
                    "S5": {"name": "S5?", "opened": False},
                    "S6": {"name": "S6?", "opened": False},
                },
                "actions_with_sword": 0
            }
            
            # Agregar al nuevo jugador al diccionario player
            player[player_name] = new_player_data
           
            
            # Ir a la sección 'Legend'
            legendMenu(player_name)  # Pasar player_name a legendMenu()

            # INSERT en la base de datos
                # Open SSH tunnel
            open_ssh_tunnel()

            # Connect to MySQL server
            mysql_connect()

            # Create a cursor
            cursor = connection.cursor()

            # Obtener la fecha y hora actual
            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


            # Valores por defecto para hearts_remaining y region
            hearts_remaining = 3
            default_region = 'Hyrule'

            # Consulta para insertar en la tabla game
            insert_query = "INSTERT INTO game (user_name, date_started, hearts_remaining, region) VALUES (%s, %s, %s, %s)"
            values = (player_name, current_datetime, hearts_remaining, default_region)
            cursor.execute(insert_query, values)
            connection.commit()
            # Close the cursor and the connection
            cursor.close()
            mysql_disconnect()

            # Close SSH tunnel
            close_ssh_tunnel()
            break  # Salir del bucle al completar la inserción

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
        "\n *             Mohamed El Baraka                                               * "                   #
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
                clear_terminal()

                plotMenu(player_name)
                break
            else:
                print("Invalid action.")

#################################################################################################################
     



################################################  PLOT, MENU    #################################################
                                                                                                                
def plotMenu(player_name):
    clear_terminal()
    from funciones import player
    spaces = ' ' * (49 - len(player_name))
    print(" * Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
          "\n *                                                                            * "
          "\n *                                                                            * "
         f"\n *   Now history is repeating itself, and Princess Zelda has been captured by * "
          "\n *   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  * "
          "\n *                                                                            * "
          "\n *                                                                            * "
         f"\n *   But a young man named '{player_name}'{spaces}* "
          "\n *   must reclaim the Guardians to defeat Ganon and save Hyrule.              * "
          "\n *                                                                            * "
          "\n *                                                                            * "
          "\n * Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    )
    while True:
        user_input = input("Type 'continue' to continue: ")

        if user_input.lower() == 'continue':
            print("The adventure begins")
            clear_terminal()
            from maps import game_logic
            game_logic()  # Call the game logic function here

            break
        
        else:
            print("Invalid action")
                                                                                                          
#################################################################################################################



################################################  DEAD    #######################################################
                                                                                                                
def deadMenu():
     clear_terminal()                                                                                 
                                                                                                
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
     while True:
        action = input("What to do now: ")

        if action.lower() == "continue":
            clear_terminal()
            from funciones import mainMenu  # Importación local
            mainMenu()
            break
        else:
            print("Invalid option. Please try again.")      

#################################################################################################################


################################################  ZELDA SAVED    ##################################################
     

def zeldaSavedMenu():                                                                                                 
     print("* Zelda Saved  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *    Congratulations, Link has saved Princess Zelda.                         * "
        "\n *    Thanks for playing!                                                     * "
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    
    )

#################################################################################################################


#########################################   REPORTS GAMES, MENU    #########################################
                                                                                                              
def reportsGamesMenu():    
    clear_terminal()                                                                                 
    print(" * Reports Games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n *                  1. Usuaris que han jugat                                   * "                 
        "\n *                  2. Quantitat de partides jugades per usuari                * "                 
        "\n *                  3. Armes usades per cada usuari i dades de la partida      * "                 
        "\n *                     on n’ha gastat més                                      * "                 
        "\n *                  4. Menjar consumit per cada usuari i dades de la partida   * "                 
        "\n *                     on n’ha consumit més                                    * "                 
        "\n *                  5. Estadística de “blood moons”                            * "                 
        "\n *                                                                             * "                 
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                 
    )  

    while True:
        action = input("What to do now: ")

        if action.lower() == "back":
            clear_terminal()
            from funciones import mainMenu  # Importación local
            mainMenu()
            break
        else:
            print("Invalid option. Please try again.")                                                                                                       
                                                                                                              
###############################################################################################################



#########################################   HELP, INVENTORY, MENU    #########################################
                                                                                                              
def helpInventoryMenu():    
    clear_terminal()                                                                                 
    print(" * Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                  
        "\n *       Type 'show inventory main' to show the main inventory                 * "                 
        "\n *             (main, weapons, Food)                                           * "                 
        "\n *       Type 'eat X' to eat X, where X is a Food item                         * "                 
        "\n *       Type 'Cook X' to Cook X, where X is a Food item                       * "                 
        "\n *       Type 'equip X' to equip X, where X is a weapon                        * "                 
        "\n *       Type 'unequip X' to unequip X, where X is a weapon                    * "                 
        "\n *       Type 'back' now to go back to the 'Game'                              * "                 
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n *                                                                             * "                 
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                 
    )  

    while True:
        action = input("What to do now: ")

        if action.lower() == "back":
            clear_terminal()
           
           
            break
        else:
            print("Invalid option. Please try again.")                                                                                                       
                                                       












######## ESTO ERAN PRUEBAS  ##########  



def rellenarEspacios(string):
    spaces = 79 - len(string)
    if spaces > 0:
        string += " " * spaces
    elif spaces < 0:
        string = string[:79]
    string += "*"
    return string



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







