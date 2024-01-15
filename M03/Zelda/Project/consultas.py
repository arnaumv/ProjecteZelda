from funciones import db_query

query = 'INSERT INTO game (user_name, date_started, hearts_remaining, blood_moon_countdown, blood_moon_appearances, region)'
db_query(query)

from datetime import datetime

def generate_insert_query(user_name, date_started, hearts_remaining=3, blood_moon_countdown=None, blood_moon_appearances=None, region=None):
    if not date_started:
        date_started = datetime.now()

    insert_query = """INSERT INTO game (user_name, date_started, hearts_remaining, blood_moon_countdown, blood_moon_appearances, region)
                      VALUES ('{}', '{}', {}, {}, {}, '{}')""".format(user_name, date_started, hearts_remaining, blood_moon_countdown, blood_moon_appearances, region)

    return insert_query

#EJEMPLO
query = generate_insert_query(user_name="nombre_usuario", date_started="2024-01-15 12:00:00", hearts_remaining=3, blood_moon_countdown=10, blood_moon_appearances=2, region="Nombre_Región")
print(query)


def generate_insert_food_query(game_id, food_name, quantity_remaining=None):
    insert_query = """INSERT INTO game_food (game_id, food_name, quantity_remaining)
                      VALUES ({}, '{}', {})""".format(game_id, food_name, quantity_remaining)

    return insert_query

# Ejemplo
food_query = generate_insert_food_query(game_id=1, food_name="Manzanas", quantity_remaining=5)
print(food_query)


def generate_insert_weapon_query(game_id, weapon_name, equipped=False, lives_remaining=None):
    insert_query = """INSERT INTO game_weapons (game_id, weapon_name, equipped, lives_remaining)
                      VALUES ({}, '{}', {}, {})""".format(game_id, weapon_name, equipped, lives_remaining)

    return insert_query

# Ejemploo
weapon_query = generate_insert_weapon_query(game_id=1, weapon_name="Espada", equipped=True, lives_remaining=3)
print(weapon_query)
