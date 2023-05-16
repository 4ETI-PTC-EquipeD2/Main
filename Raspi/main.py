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
#import Pathfinding
import librairie_STM32 as lST
#import serial
import librairie_Serv as lSV

#Variables -------------------------------------------------
#Description matrice du terrain 
# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre
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
#Main -------------------------------------------------------------------------
#ser = serial.Serial()
#Initialisation 
#lST.init_UART(ser, 19200,'COM7')




#Boucle d'actions
while (run) : 
    #terrain = lST.obstacle_scan(terrain)
    run,terrain,Flag,Pile = lST.avancer_case(terrain,run,Flag,Pile)
    """
    if lST.detec_QRCode != -1 :
        ordre = lSV.send_qr_id(str(id))
        if ordre == "attaquer" :
           lSV.attaquer() #créer un protocole de communication
        else :
            None
    """
                       
           
    