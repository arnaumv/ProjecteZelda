import mysql.connector
import pandas as pd
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import pymysql

ssh_host = '20.26.234.155'
ssh_username = 'azureuser'
ssh_password = 'proyectozelda2024.'
database_username = 'root'
database_password = 'root'
database_name = 'Zelda'
localhost = '127.0.0.1'

def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    tunnel.start()

def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection
    :return connection: Global MySQL database connection
    """
    global connection
    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )

def mysql_disconnect():
    #Closes the MySQL database connection.
    connection.close()

def close_ssh_tunnel():
    #Closes the SSH tunnel connection.
    global tunnel
    tunnel.close()

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