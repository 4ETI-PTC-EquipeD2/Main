"""
Auteurs : Audrey Nicolle, ...
Ce fichier contient toutes les fonctions utilisées par le fichier main pour la boucle d'action
du robot.
"""
import Pathfinding as Path

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
def obstacle_scan(terrain,ser,lastMove) :
    for i in range(3): #i est la commande, et se balade entre 0 et 2 compris, pour scan à gauche, puis devant, et enfin à droite, relativement à la direction du robot, donc de la direction de son dernier movement.
        dist=Send_Receive_UART(ser,i) #renvoie la distance selon si la direction demandée est 0, 1 ou 2
        terrain=Path.find_obstacle(terrain, i, dist, lastMove) #Pose l'obstacle à la bonne distance selon la dirrection du capteur, la distance, la direction du robot
    return terrain

def avancer_case(terrain,run,Flag,Pile) :
    """TO DO, Audrey
        Trouver un moyen d'organiser le déplacement
    Args:
        terrain (_type_): _description_
        
    # 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre
terrain = np.array([0000],[0000],[0000],[0000],[0000],[2000])
    """
    return Path.main(terrain,run,Flag,Pile)
    
    
    
#Fonction attaque -------------------------------------------------------------------------

def attaque() :
    """_Boucle d'attaque, ne sort pas de lafonction tant que l'attaque n'est pas fini. 
    """
    
if __name__ == "__main__":
    print("Starting UART...")
    ser = Serial()
    init_UART(ser, 19200, 'COM13')
    while(1):
        cmd = input("appuyer sur une lettre puis ENTRER : ")
        if len(cmd) != 1:
            cmd = 'a'
        print(cmd)

        # print(Send_Receive_UART(ser, cmd))
        ser.write(b'q')
        # ser.write(bytes(cmd,encoding='utf8'))
        while(1):
            print(":",ser.readline())
    ser.close()
