import mysql.connector

def check_game_records():
    # Open SSH tunnel
    open_ssh_tunnel()

    # Connect to MySQL server
    mysql_connect()

    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL query
    query = "SELECT COUNT(*) FROM game"
    cursor.execute(query)

    # Get the result
    result = cursor.fetchone()

    # Close the cursor and the connection
    cursor.close()
    mysql_disconnect()

    # Close SSH tunnel
    close_ssh_tunnel()

    # Check if there are more than one record
    if result[0] > 0:
        plays = True
    else:
        plays = False

    # Return the value of plays
    return plays