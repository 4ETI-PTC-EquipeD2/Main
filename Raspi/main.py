"""
Fichier main qui permet de commander l'ensemble du robot.
"""
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/orani/OneDrive/Bureau/Key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://projet-pokemon-9145b-default-rtdb.europe-west1.firebasedatabase.app/'
})

#Import ----------------------------------------------------
import math
import Pathfinding
import librairie_STM32 as lST
import serial
import librairie_Serv as lSV

#Variables -------------------------------------------------
#Description matrice du terrain 
# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre, 4 => visité, 5 => murs de la zone de test.
#0,0 en coo en haut à gauche. x de gauche à droite, y de haut en bas, coo formt x,y
terrain =         [[5,5,5,5,5,5],
                   [5,0,0,1,0,5],
                   [5,0,0,1,0,5],
                   [5,1,0,0,0,5],
                   [5,0,0,0,0,5],
                   [5,0,0,0,0,5],
                   [5,2,0,0,0,5],
                   [5,5,5,5,5,5]]

run = True
Flag=False
Pile=[]
qr_code_id=0
#Main -------------------------------------------------------------------------
#à décomenter quand ce sera branché
#Initialisation 

ser = serial.Serial()
COM = input("Entrer le numéro du COM (ex. 3, 4, ...) : ")
lST.init_UART(ser, 19200, 'COM'+COM)
print("UIIII",run)




#Boucle d'actions
while (run) :
    #if attend_rep=False:
    lastMove='u'
    if len(Pile)!=0:
            lastMove=Pile[-1]
    print("je sui")
    #terrain = lST.obstacle_scan(terrain,ser,lastMove) #Scan du terrain devant à gauche et à droite relativement au robot.
    run,terrain,Flag,Pile = lST.avancer_case(ser,terrain,run,Flag,Pile) #Avance d'une case selon le chemin calculer par pathfinding avec les obstacles actuellement connus.
    #ret=lST.capture(ser)
    #print("Cannon: ",ret)

    """
    dirr_obstacle=Pathfinding.obstacle_voisin(terrain) #Cherche si il y a un obstacle proche et recupère sa direction.
    if dirr_obstacle!="n":
        print(dirr_obstacle)
        #Faudra préciser la dirrection et modif la fonction
        #qr_code_id=lSV.live_video() #Récupère le qrCode. à changer
        lSV.send_qr_id(qr_code_id) #Envoie la qrCode à la BDD
        if qr_code_id!=0:
            ordre = lSV.read_qr_action() #Regarde si une action est à faire.
            if ordre !=-1:
                lST.action(ordre,ser) # ici ordre sera un entier qui est des 0 à 3 pour les attaque, 4 pour la capture et 5 pour la fuite. -1 correspond à une valeur non attribuée.
                lSV.send_qr_action(-1)

    """
    
                       
           
    