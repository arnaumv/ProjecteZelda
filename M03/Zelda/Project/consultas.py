import mysql.connector
from funciones import db_query


def check_game_records():
    # Establecer la conexión con la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Zelda')

    # Crear un cursor
    cursor = cnx.cursor()

    # Ejecutar la consulta SQL
    query = "SELECT COUNT(*) FROM game"
    cursor.execute(query)

    # Obtener el resultado
    result = cursor.fetchone()

    # Cerrar el cursor y la conexión
    cursor.close()
    cnx.close()

    # Comprobar si hay más de un registro
    if result[0] > 0:
        plays = True
    else:
        plays = False

    # Devolver el valor de plays
    return plays

def create_player_data(player_name):
    db_query()
