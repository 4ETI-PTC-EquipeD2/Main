"""
Mathis Gorvien
"""
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import base64
from pyzbar.pyzbar import decode

# Note: The path to the JSON file is different on your computer

cred = credentials.Certificate("/home/admin/key/projet-pokemon-9145b-firebase-adminsdk-pyblk-c58d839000.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://projet-pokemon-9145b-default-rtdb.europe-west1.firebasedatabase.app/'
})

def send_qr_id(qr_code_id):
    '''
    Envoie la valeur du dernier QR code scanné à la base de données Firebase.

    Args:
        qr_code_id (str) : L'ID du QR code qui a été scanné.
    '''

    # Get a reference to the database
    ref = db.reference('qr_code_request')

    # Set the value of the last scanned QR code
    ref.set(qr_code_id)

def read_qr_action():
    ref=db.reference('action/attaque')
    return ref.get()

# Test the function
def send_movement(movement, game_id):
    '''
    Envoie un mouvement à la base de données Firebase.

    Args:
        movement (int): Le mouvement à envoyer. 1 = haut, 2 = bas, 3 = gauche, 4 = droite.
        game_id (str): L'ID du jeu.
    '''


    # Get a reference to the map_movement in the database
    ref = db.reference(f'map_movement/{game_id}')

    # Push the movement data to the database using the game_id as key
    ref.child('movements').push(movement)

def send_obstacle(position, game_id):
    '''
    Envoie une position d'obstacle à la base de données Firebase.

    Args:
        position (list of int): La position de l'obstacle (x, y) sur la carte.
        game_id (str): L'ID du jeu.
    '''

    # Get a reference to the map_movement in the database
    ref = db.reference(f'map_movement/{game_id}')

    # Push the obstacle position to the database using the game_id as key
    ref.child('obstacles').push(position)

def live_video():
    '''
    Lance la diffusion de la vidéo en direct sur la base de données Firebase. La vidéo est capturée à partir de la webcam. Les anciennes images sont supprimées si plus de 100 images sont stockées.

    Cette fonction se charge aussi de la lecture des QR codes. Lorsqu'un QR code est détecté, la fonction 'send_qr_id' est appelée.

    Note: Cette fonction est bloquante. Elle ne se termine pas tant que la diffusion de la vidéo n'est pas terminée.
    '''

    # Get a reference to the Firebase Realtime Database
    db_ref = db.reference('video')
    video_state_ref = db.reference('video_state')

    # Timer
    qr_detected_at = None

    # Function to set the video state
    def set_video_state(state):
        video_state_ref.set(state)

    class VideoStateContext:
        def __enter__(self):
            set_video_state(1)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            set_video_state(0)

    with VideoStateContext():
        # Delete the contents of video
        db_ref.delete()

        # Start capturing video from the webcam
        camera = cv2.VideoCapture(0)

        # Set the resolution
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320/4)  # width
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240/4)  # height

        frame_count = 0

        while True:
            # Read a frame from the camera
            success, frame = camera.read()

            # Nos opérations sur le cadre viennent ici
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            codes = decode(gray)

            for code in codes:
                x, y, w, h = code.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                code_data = code.data.decode('utf-8')
                cv2.putText(frame, code_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

                # print(f"QR Code Detected: {code_data}")
                send_qr_id(code_data)

                if qr_detected_at is None:  # Enregistrez l'heure de la détection du QR code si ce n'est pas déjà fait
                    qr_detected_at = time.time()
            
            if qr_detected_at is not None and time.time() - qr_detected_at >= 10:  # Vérifiez si 10 secondes se sont écoulées depuis la détection du QR code
                break
            

            # # Affichage du cadre résultant
            # cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            if success:
                # Convert the frame to bytes
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                frame_bytes = buffer.tobytes()

                frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
                # Save the frame to the database
                # Encode the frame as base64
                frame_base64 = base64.b64encode(frame_bytes).decode('utf-8')

                # Store the frame in Firebase
                db_ref.push({'frame': frame_base64})
                frame_count += 1

                # Remove old frames if there are more than max_frames
                if frame_count > 100:
                    frame_count -= 1
                    oldest_frame = db_ref.order_by_key().limit_to_first(1).get()
                    oldest_key = list(oldest_frame.keys())[0]
                    db_ref.child(oldest_key).delete()

        # Lorsque tout est fait, libérez la capture
        camera.release()
        cv2.destroyAllWindows()

def action_id_listener():
    '''
    Lance un écouteur sur 'action_id' dans la base de données Firebase. Chaque fois que 'action_id' change, la fonction 'listener' est appelée.
    '''

    action_id_ref = db.reference('action_id')
    action_id_ref.listen(listener)

def listener(event):
    '''
    Cette fonction est appelée chaque fois que 'action_id' change dans la base de données Firebase. Elle imprime la nouvelle valeur de 'action_id'.

    Args:
        event: Un objet événement qui contient les données de l'événement de la base de données Firebase.
    '''

    # This function will be called every time `action_id` changes
    print(event.data)  # `event.data` contains the new value of `action_id`