
from funciones import *



def insert_into_database(player_name):
    # INSERT into the database
    try:
        # Open SSH tunnel and connect to the MySQL server
        open_ssh_tunnel()
        mysql_connect()

        # Get the current date and time
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Default values for hearts_remaining and region
        hearts_remaining = 3
        default_region = 'Hyrule'

        # Query to insert into the game table
        insert_query = f"INSERT INTO game (user_name, date_started, hearts_remaining, region) " \
                    f"VALUES ('{player_name}', '{current_datetime}', {hearts_remaining}, '{default_region}')"

        with connection.cursor() as cur:
            cur.execute(insert_query)
            connection.commit()

        # Close the MySQL connection and the SSH tunnel
        mysql_disconnect()
        close_ssh_tunnel()
    except Exception as e:
        print(f"An error occurred: {e}")

def check_game_records():
    # Open SSH tunnel
    open_ssh_tunnel()

    # Establish the connection with the database
    mysql_connect()

    # Use the global connection object
    global connection

    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL query
    query = "SELECT COUNT(*) FROM game"
    cursor.execute(query)

    # Get the result
    result = cursor.fetchone()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Close SSH tunnel
    close_ssh_tunnel()

    # Check if there is more than one record
    if result[0] > 0:
        plays = True
    else:
        plays = False

    # Return the value of plays
    return plays


from datetime import datetime

def save_game_state_to_db(game_state, user_name):
    last_player = list(player.keys())[-1]
    open_ssh_tunnel()
    mysql_connect()

    # Use the global connection object
    global connection

    # Create a cursor object
    cur = connection.cursor()

    # Update the last added user's game state in the table
    cur.execute('''
        UPDATE game 
        SET date_started = %s, hearts_remaining = %s, blood_moon_countdown = %s, region = %s
        WHERE user_name = (SELECT user_name FROM game ORDER BY date_started DESC LIMIT 1)
    ''', (datetime.now(), game_state['hearts_remaining'], game_state['blood_moon_countdown'], game_state['region']))

    # Commit the changes
    connection.commit()

    # Get the game_id of the last updated game
    cur.execute("SELECT game_id FROM game WHERE user_name = %s ORDER BY date_started DESC LIMIT 1", (user_name,))
    game_id = cur.fetchone()[0]

    # Get the opened chests and the map name
    opened_chests_count = count_opened_chests(game_state['region'])
    map_name = game_state['region']

    # Insert the map name and the count of opened chests into the game_chests_opened table
    cur.execute('''
        INSERT INTO game_chests_opened (game_id, region, num)
        VALUES (%s, %s, %s)
    ''', (game_id, map_name, opened_chests_count))

    # Commit the changes
    connection.commit()

    # Get the opened sanctuaries and the map name
    opened_sanctuaries_count = count_opened_sanctuaries()

    # Insert the map name and the count of opened sanctuaries into the game_sanctuaries_opened table
    for map_name, count in opened_sanctuaries_count.items():
        cur.execute('''
            INSERT INTO game_sanctuaries_opened (game_id, region, num)
            VALUES (%s, %s, %s)
        ''', (game_id, map_name, count))

    # Commit the changes
    connection.commit()

    # Insert the food information into the game_food table
    for food_name, food_info in player[last_player]['food'].items():
        cur.execute('''
            INSERT INTO game_food (game_id, food_name, quantity_remaining)
            VALUES (%s, %s, %s)
        ''', (game_id, food_name, food_info['count']))

    # Commit the changes
    connection.commit()

    mysql_disconnect()
    close_ssh_tunnel()




