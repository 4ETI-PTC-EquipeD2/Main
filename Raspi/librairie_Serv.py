"""
Mathis Gorvien
"""
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Note: The path to the JSON file is different on your computer


def send_point(x, y, ref_str):
    """
    Adds a new point to the Firebase database.
    Args:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
        ref_str (str): The reference string for the Firebase database.
    """

    ref = db.reference('points/' + ref_str + '/points')

    # Get the latest key from the database
    if  ref.get() != None:
        num_points = len(ref.get())
    else:
        num_points = 0
    
    # Set the data to add
    point = {
        'x': x,
        'y': y
    }

    # Push the data to the database
    ref.child(str(num_points)).set(point)


def init_map():
    """
    Initializes a new map by generating a unique name based on the current date and time.
    Returns:
        str: A string containing the name of the new map.
    """
    
    now = datetime.datetime.now()
    name = 'Trace_' + now.strftime('%d_%m_%Y_%H_%M_%S')

    return name

def send_qr_id(qr_code_id):
    """
    Writes the value of the last scanned QR code to the 'qr_code_request' field in the Firebase Realtime Database.
    Args:
        qr_code_id (str): The ID of the QR code that was scanned.
    """
    
    # Get a reference to the database
    ref = db.reference('qr_code_request')

    # Set the value of the last scanned QR code
    ref.set(qr_code_id)

# Test the function

# # Initialize the map
# ref1 = init_map()

# # Send the points to the database
# sendpoint(1, 2, ref1)

send_qr_id(8)