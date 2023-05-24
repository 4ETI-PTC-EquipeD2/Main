# Cette fonction permet d'envoyer les données de mouvement à la base de données
# Les mouvement sont simples ( 1 = haut, 2 = bas, 3 = gauche, 4 = droite)
# Ces donnés doivent permettre l'affichage de la position du robot sur la carte
# Cette carte est une grille 4x6 (4 lignes, 6 colonnes)

import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Note: The path to the JSON file is different on your computer

def send_movement(movement, game_id):
    """
    Sends a movement to the Firebase database.

    Args:
        movement (int): The movement to send. 1 = up, 2 = down, 3 = left, 4 = right.
        game_id (str): The ID of the game.
    """

    # Get a reference to the map_movement in the database
    ref = db.reference(f'map_movement/{game_id}')

    # Push the movement data to the database using the game_id as key
    ref.child('movements').push(movement)

def send_movement_sequence(movements, game_id):
    """
    Sends a sequence of movements to the Firebase database.

    Args:
        movements (list of int): The movements to send.
        game_id (str): The ID of the game.
    """

    for movement in movements:
        send_movement(movement, game_id)

def send_obstacle(position, game_id):
    """
    Sends an obstacle position to the Firebase database.

    Args:
        position (list of int): The position of the obstacle (x, y) on the map.
        game_id (str): The ID of the game.
    """

    # Get a reference to the map_movement in the database
    ref = db.reference(f'map_movement/{game_id}')

    # Push the obstacle position to the database using the game_id as key
    ref.child('obstacles').push(position)

# Test the function
# send_movement(3, 'test')

#send_obstacle([2, 4], 'test')
