"""
Auteurs : Audrey Nicolle, ...
Ce fichier contient toutes les fonctions utilisées par le fichier main pour la boucle d'action
du robot.
"""

#Fonctions UART ---------------------------------------------------------------------------------------------------------------------

def init_UART (ser, baudrate, port) :
    """ Permet d'initialiser l'uart. On doit recevoir "UART initialized 
    depuis la STM32.

    Args:
        ser (Serial): liaison série créee.
        baudrate (int): valeur du baudrate.
        port (str): numéro du port utilisé sur l'ordi.

    Returns:
        boolean : permet de savoir si l'uart est initialisé correctement
    """
    ser.baudrate = baudrate 
    ser.port = port
    ser.bytesize=8
    ser.parity='N'
    ser.stopbits=1
    ser.timeout=None
    ser.xonxoff=0
    ser.rtscts=0
    ser.open()
    
    if ser.is_open :
        print("connected to", ser, "\n")
        line = ser.readline()
        line = line.decode("utf-8")
        if line :
            print(line,'\n')
        return True
    else :
        return False
    
def Send_Receive_UART (ser,data) :
    """Envoie la commande et reçois la réponse du robot. 
    Le plus souvent ACK ou NACK.

    Args:
        ser (Serial): liaison UART
        data (str): commande 

    Returns:
        str: réponse
    """

    ser.write(bytes(data))
    line = ser.readline()
    line = line.decode("utf-8")
    return line

#Fonction déplacement -----------------------------------------------------------------
def obstacle_scan(terrain) :
    """TO DO, Seb

    Args:
        terrain (_type_): _description_
    """

def avancer_case(terrain) :
    """TO DO, Audrey
        Trouver un moyen d'organiser le déplacement
    Args:
        terrain (_type_): _description_
    """
    
#Fonction attaque -------------------------------------------------------------------------

def attaque() :
    """_Boucle d'attaque, ne sort pas de lafonction tant que l'attaque n'est pas fini. 
    """
    