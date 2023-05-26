"""
Auteurs : Audrey Nicolle, ...
Ce fichier contient toutes les fonctions utilisées par le fichier main pour la boucle d'action
du robot.
"""
import Pathfinding as Path
from serial import Serial
import copy as c
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

    ser.write(bytes(data,encoding='utf8'))
    line = ser.readline()
    line = line.decode("utf-8")
    return line

#Fonction déplacement -----------------------------------------------------------------
def obstacle_scan(terrain,ser,lastMove) :
    for i in range(3): #i est la commande, et se balade entre 0 et 2 compris, pour scan à gauche, puis devant, et enfin à droite, relativement à la direction du robot, donc de la direction de son dernier movement.
        cmd=c.copy(i)
        dist=Send_Receive_UART(ser,str(cmd)) #renvoie la distance selon si la direction demandée est 0, 1 ou 2
        print("commande obstacle_scan: ",dist)
        terrain=Path.find_obstacle(terrain, i, 250, lastMove) #Pose l'obstacle à la bonne distance selon la dirrection du capteur, la distance, la direction du robot
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

def action(id,ser):
    #id 4 fuite
    print("action id: ",id)
    if id==5:
        capture(ser,id)
    else:
        attaque(ser,id)

def attaque(id,ser) :
    """_Boucle d'attaque, ne sort pas de lafonction tant que l'attaque n'est pas fini.
    """

def capture(ser):
    #Fonction pour tirer avec le cannon
    print("PIOU")
    ret=Send_Receive_UART(ser,"t")
    return ret

    
if __name__ == "__main__":
    ser = Serial()
    COM = input("Entrer le numéro du COM (ex. 3, 4, ...) : ")
    init_UART(ser, 19200, 'COM'+COM)
    while(1):
        cmd = input("appuyer sur une lettre puis ENTRER : ")
        if len(cmd) != 1:
            cmd = 'a'
        print("sent:",cmd)

        received = Send_Receive_UART(ser, cmd)
        print("received:",received)
    ser.close()
